"""Irish income tax calculation."""

from policyengine_ie.model_api import *


class income_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income tax"
    documentation = """
    Total income tax liability before tax credits.
    Ireland has two rates: 20% (standard rate) and 40% (higher rate).
    The standard rate band varies by marital status and circumstances.
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx"
    
    def formula(person, period, parameters):
        taxable_income = person("taxable_income", period)
        standard_rate_band = person("standard_rate_band", period)
        
        p = parameters(period).gov.revenue.income_tax
        
        standard_rate = p.rates.standard_rate
        higher_rate = p.rates.higher_rate
        
        # Calculate tax
        # Standard rate on income up to standard rate band
        standard_rate_income = min_(taxable_income, standard_rate_band)
        standard_rate_tax = standard_rate_income * standard_rate
        
        # Higher rate on income above standard rate band
        higher_rate_income = max_(0, taxable_income - standard_rate_band)
        higher_rate_tax = higher_rate_income * higher_rate
        
        total_income_tax = standard_rate_tax + higher_rate_tax
        
        return total_income_tax