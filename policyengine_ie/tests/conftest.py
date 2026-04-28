"""
Pytest configuration for PolicyEngine Ireland tests.

This file configures pytest to discover and run YAML-based policy tests.
"""

import pytest
import yaml
import re
import numpy as np
from policyengine_ie import IrishTaxBenefitSystem
from policyengine_core.simulations import Simulation


PERIOD_PATTERN = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")


def is_period_key(key):
    return str(key) == "ETERNITY" or bool(PERIOD_PATTERN.match(str(key)))


def normalize_input_values(value, period):
    if isinstance(value, dict):
        if value and all(is_period_key(key) for key in value):
            return value
        return {
            key: normalize_input_values(child, period) for key, child in value.items()
        }
    if isinstance(value, list):
        return value
    return {period: value}


def pytest_collect_file(parent, path):
    """Custom collector for YAML test files."""
    if path.ext == ".yaml" and path.basename.startswith("test_"):
        return YamlFile.from_parent(parent, fspath=path)


class YamlFile(pytest.File):
    """Custom file collector for YAML tests."""

    def collect(self):
        """Collect test items from YAML file."""
        with open(self.fspath) as f:
            test_cases = yaml.safe_load(f)

        for i, test_case in enumerate(test_cases):
            name = test_case.get("name", f"test_{i}")
            yield YamlTestItem.from_parent(self, name=name, spec=test_case)


class YamlTestItem(pytest.Item):
    """Custom test item for YAML test cases."""

    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.spec = spec

    def runtest(self):
        """Run the YAML test case."""
        system = IrishTaxBenefitSystem()

        # Build situation from input
        situation = self.spec.get("input", {})
        period = str(self.spec.get("period", "2024"))
        situation = normalize_input_values(situation, period)

        # Create simulation
        simulation = Simulation(tax_benefit_system=system, situation=situation)

        # Check outputs
        expected_outputs = self.spec.get("output", {})
        person_ids = list(situation.get("people", {}).keys())

        for output_key, expected_value in expected_outputs.items():
            if output_key in system.variables:
                if isinstance(expected_value, dict):
                    for entity_name, entity_expected in expected_value.items():
                        self.assert_variable(
                            simulation,
                            output_key,
                            period,
                            entity_expected,
                            index=person_ids.index(entity_name),
                        )
                else:
                    self.assert_variable(simulation, output_key, period, expected_value)
            elif isinstance(expected_value, dict) and output_key in person_ids:
                for variable_name, entity_expected in expected_value.items():
                    self.assert_variable(
                        simulation,
                        variable_name,
                        period,
                        entity_expected,
                        index=person_ids.index(output_key),
                    )
            else:
                raise AssertionError(f"Unknown output target: {output_key}")

    def assert_variable(
        self, simulation, variable_name, period, expected_value, index=0
    ):
        calculated = simulation.calculate(variable_name, period)
        if isinstance(calculated, np.ndarray):
            calculated = calculated[index]
        elif hasattr(calculated, "__len__") and not isinstance(
            calculated, (str, bytes)
        ):
            calculated = calculated[index]

        if isinstance(expected_value, bool):
            assert bool(calculated) is expected_value, (
                f"{variable_name}: expected {expected_value}, got {calculated}"
            )
        elif isinstance(expected_value, (int, float)):
            assert abs(calculated - expected_value) < 0.01, (
                f"{variable_name}: expected {expected_value}, got {calculated}"
            )
        else:
            assert calculated == expected_value, (
                f"{variable_name}: expected {expected_value}, got {calculated}"
            )

    def reportinfo(self):
        """Report test location."""
        return self.fspath, 0, f"[{self.name}]"
