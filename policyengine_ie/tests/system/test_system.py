"""Test the Irish tax-benefit system initialization and basic functionality."""

import pytest
from policyengine_ie import IrishTaxBenefitSystem
from policyengine_core.simulations import Simulation


class TestIrishTaxBenefitSystem:
    """Test cases for the IrishTaxBenefitSystem class."""

    def test_system_initialization(self):
        """Test that the system initializes correctly."""
        system = IrishTaxBenefitSystem()

        # Check that entities are properly defined
        assert "person" in system.entities
        assert "tax_unit" in system.entities
        assert "benefit_unit" in system.entities
        assert "family" in system.entities
        assert "household" in system.entities

        # Check that system has parameters and variables directories
        assert system.parameters_dir is not None
        assert system.variables_dir is not None

    def test_basic_simulation(self):
        """Test that a basic simulation can be created and run."""
        system = IrishTaxBenefitSystem()
        simulation = Simulation(system=system)

        # Add a person
        simulation.add_person(
            person_id="person_1", age=35, employment_income=50000
        )

        # Add household structure
        simulation.add_tax_unit(tax_unit_id="tax_unit_1", adults=["person_1"])

        simulation.add_household(
            household_id="household_1", members=["person_1"]
        )

        # Test basic calculations
        age = simulation.calculate("age", period="2024")
        employment_income = simulation.calculate(
            "employment_income", period="2024"
        )

        assert age["person_1"] == 35
        assert employment_income["person_1"] == 50000

    def test_entities_properties(self):
        """Test that entity properties work correctly."""
        system = IrishTaxBenefitSystem()

        assert system.person_entity.key == "person"
        assert system.household_entity.key == "household"
        assert system.tax_unit_entity.key == "tax_unit"
        assert system.benefit_unit_entity.key == "benefit_unit"
        assert system.family_entity.key == "family"

    def test_system_with_reform(self):
        """Test that the system can accept a reform parameter."""
        # This is a placeholder test - would need to implement actual reforms
        system = IrishTaxBenefitSystem(reform=None)
        assert system is not None

    def test_basic_inputs_defined(self):
        """Test that basic input variables are defined in the system."""
        system = IrishTaxBenefitSystem()

        expected_inputs = [
            "age",
            "employment_income",
            "self_employment_income",
        ]

        # Check that basic inputs are in the system's basic_inputs list
        for input_var in expected_inputs:
            assert input_var in system.basic_inputs
