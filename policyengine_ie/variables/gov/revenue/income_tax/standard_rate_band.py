"""Standard rate band calculation for Irish income tax."""

from policyengine_ie.model_api import *


class standard_rate_band(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Standard rate band"
    documentation = """
    The amount of income taxed at the standard rate (20%) before the higher rate (40%) applies.
    This varies based on marital status and whether there are dependent children.
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/jobs-and-pensions/calculating-your-income-tax/tax-rate-band.aspx"
    
    def formula(person, period, parameters):
        tax_unit = person.tax_unit
        
        # Get marital status and other circumstances
        is_married = tax_unit("is_married", period)
        has_spouse_income = tax_unit("has_spouse_income", period)
        has_child_carer_credit = person("has_child_carer_credit", period, options=[False])
        
        p = parameters(period).gov.revenue.income_tax.bands
        
        # Determine the standard rate band
        standard_band = select(
            [
                # Single person with child carer credit
                logical_and(logical_not(is_married), has_child_carer_credit),
                # Married couple with one income
                logical_and(is_married, logical_not(has_spouse_income)),
                # Married couple with two incomes (complex calculation - simplified here)
                logical_and(is_married, has_spouse_income),
                # Single person (default)
                logical_not(is_married)
            ],
            [
                p.single_with_child,
                p.married_one_income,
                p.married_one_income,  # Simplified - should calculate based on spouse income
                p.single
            ],
            default=p.single
        )
        
        return standard_band