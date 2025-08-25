"""Employment income."""

from policyengine_ie.model_api import *


class employment_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Employment income"
    documentation = """
    Gross employment income from wages, salary, and other PAYE income.
    This is income subject to PAYE, PRSI, and USC.
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/jobs-and-pensions/index.aspx"
