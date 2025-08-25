"""Net income tax after credits."""

from policyengine_ie.model_api import *


class income_tax_net(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net income tax"
    documentation = """
    Income tax liability after deducting tax credits.
    This is the actual amount of income tax owed.
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/index.aspx"
    
    def formula(person, period, parameters):
        gross_income_tax = person("income_tax", period)
        tax_credits = person("income_tax_credits", period)
        
        # Net tax is gross tax minus credits, but cannot be negative
        net_tax = max_(0, gross_income_tax - tax_credits)
        
        return net_tax