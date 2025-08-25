"""Marital status variable."""

from policyengine_ie.model_api import *


class is_married(Variable):
    value_type = bool
    entity = TaxUnit
    definition_period = YEAR
    label = "Is married"
    documentation = """
    Whether the tax unit represents a married couple or civil partnership.
    Used for determining tax bands and credits.
    """

    def formula(tax_unit, period, parameters):
        # Count adults in tax unit
        adults = tax_unit.members("age", period) >= 18
        num_adults = tax_unit.sum(adults)

        # Tax unit is married if it has 2 adults
        return num_adults == 2
