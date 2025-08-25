"""Irish income tax credits calculation."""

from policyengine_ie.model_api import *


class income_tax_credits(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income tax credits"
    documentation = """
    Total income tax credits available to reduce tax liability.
    Includes personal credit, PAYE credit, and other applicable credits.
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-credits/"

    def formula(person, period, parameters):
        tax_unit = person.tax_unit

        is_married = tax_unit("is_married", period)
        has_employment = person("employment_income", period) > 0
        age = person("age", period)
        is_renting = person("is_renting", period, options=[False])

        p = parameters(period).gov.revenue.income_tax.credits

        # Personal tax credit
        personal_credit = where(
            is_married, p.personal.married, p.personal.single
        )

        # PAYE credit (if has employment income)
        paye_credit = where(has_employment, p.paye, 0)

        # Age credit (for those 65 and over)
        age_credit = where(age >= 65, p.age, 0)

        # Rent credit (if renting)
        rent_credit = where(
            is_renting, where(is_married, p.rent.married, p.rent.single), 0
        )

        total_credits = (
            personal_credit + paye_credit + age_credit + rent_credit
        )

        return total_credits
