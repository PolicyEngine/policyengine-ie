"""Taxable income calculation for Irish residents."""

from policyengine_ie.model_api import *


class taxable_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Taxable income"
    documentation = """
    Total taxable income for Irish income tax purposes.
    This includes employment income, self-employment income, investment income,
    rental income, and pension income, less allowable deductions.
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/index.aspx"
    
    def formula(person, period, parameters):
        employment_income = person("employment_income", period)
        self_employment_income = person("self_employment_income", period)
        investment_income = person("investment_income", period, options=[0])
        rental_income = person("rental_income", period, options=[0])
        pension_income = person("pension_income", period, options=[0])
        
        # Total gross income
        gross_income = (
            employment_income + 
            self_employment_income + 
            investment_income + 
            rental_income + 
            pension_income
        )
        
        # Deduct allowable deductions (simplified - would need to implement specific deductions)
        total_deductions = person("total_deductions", period, options=[0])
        
        taxable_income = max_(0, gross_income - total_deductions)
        
        return taxable_income