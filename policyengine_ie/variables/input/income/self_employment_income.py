"""Self-employment income."""

from policyengine_ie.model_api import *


class self_employment_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Self-employment income"
    documentation = """
    Net profit from self-employment, trade, or profession.
    Subject to income tax, USC, and PRSI Class S.
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/self-employed/index.aspx"
