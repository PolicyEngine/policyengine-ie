"""Gross income for USC calculation."""

from policyengine_ie.model_api import *


class gross_income_for_usc(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gross income for USC"
    documentation = """
    Total gross income subject to USC.
    This includes all income sources: employment, self-employment, 
    investment, rental, pension, and unearned income.
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/jobs-and-pensions/usc/calculating-usc.aspx"
    
    def formula(person, period, parameters):
        employment_income = person("employment_income", period)
        self_employment_income = person("self_employment_income", period)
        investment_income = person("investment_income", period, options=[0])
        rental_income = person("rental_income", period, options=[0])
        pension_income = person("pension_income", period, options=[0])
        
        # USC applies to gross income before any deductions
        gross_income = (
            employment_income + 
            self_employment_income + 
            investment_income + 
            rental_income + 
            pension_income
        )
        
        return gross_income