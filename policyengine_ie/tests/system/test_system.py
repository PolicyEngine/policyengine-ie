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
        entity_keys = [entity.key for entity in system.entities]
        assert "person" in entity_keys
        assert "tax_unit" in entity_keys
        assert "benefit_unit" in entity_keys
        assert "family" in entity_keys
        assert "household" in entity_keys

        # Check that system has parameters and variables directories
        assert system.parameters_dir is not None
        assert system.variables_dir is not None

    def test_basic_simulation(self):
        """Test that a basic simulation can be created and run."""
        system = IrishTaxBenefitSystem()
        simulation = Simulation(
            tax_benefit_system=system,
            situation={
                "people": {
                    "person_1": {
                        "age": {"2024": 35},
                        "employment_income": {"2024": 50000},
                    },
                },
                "tax_units": {"tax_unit_1": {"adults": ["person_1"]}},
                "households": {"household_1": {"members": ["person_1"]}},
            },
        )

        # Test basic calculations
        age = simulation.calculate("age", period="2024")
        employment_income = simulation.calculate("employment_income", period="2024")

        assert age[0] == 35
        assert employment_income[0] == 50000

    def test_entities_properties(self):
        """Test that entity properties work correctly."""
        system = IrishTaxBenefitSystem()

        entities = {entity.key: entity for entity in system.entities}
        assert entities["person"].key == "person"
        assert entities["household"].key == "household"
        assert entities["tax_unit"].key == "tax_unit"
        assert entities["benefit_unit"].key == "benefit_unit"
        assert entities["family"].key == "family"

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
