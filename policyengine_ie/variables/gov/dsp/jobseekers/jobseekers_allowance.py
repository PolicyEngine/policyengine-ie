"""Jobseeker's Allowance calculation."""

from policyengine_ie.model_api import *


class jobseekers_allowance(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jobseeker's Allowance"
    documentation = """
    Jobseeker's Allowance is a means-tested payment for people who are unemployed.
    The rate varies by age, with reduced rates for those aged 18-24 unless living independently.
    Includes increases for qualified adults and children.
    """
    unit = EUR
    reference = "https://www.citizensinformation.ie/en/social-welfare/unemployed-people/jobseekers-allowance/"

    def formula(person, period, parameters):
        age = person("age", period)
        is_unemployed = person("is_unemployed", period, options=[False])
        is_available_for_work = person(
            "is_available_for_work", period, options=[True]
        )
        is_genuinely_seeking_work = person(
            "is_genuinely_seeking_work", period, options=[True]
        )

        # Means test
        assessable_income = person(
            "assessable_income_jobseekers", period, options=[0]
        )
        means_test_passed = person("jobseekers_means_test", period)

        # Living independently check for under 25s
        is_living_independently = person(
            "is_living_independently", period, options=[False]
        )
        has_housing_support = person(
            "has_housing_support", period, options=[False]
        )

        benefit_unit = person.benefit_unit
        qualified_adults = benefit_unit("qualified_adults_jobseekers", period)
        qualified_children = benefit_unit(
            "qualified_children_jobseekers", period
        )

        p = parameters(period).gov.dsp.jobseekers.rates

        # Check basic eligibility
        eligible = logical_and(
            logical_and(is_unemployed, is_available_for_work),
            logical_and(is_genuinely_seeking_work, means_test_passed),
        )

        # Determine personal rate based on age and circumstances
        personal_rate = select(
            [
                # Under 25 and living independently with housing support
                logical_and(
                    age < 25,
                    logical_and(is_living_independently, has_housing_support),
                ),
                # Under 25 but not living independently
                age < 25,
                # 25 and over
                age >= 25,
            ],
            [p.age_18_24_independent, p.age_18_24, p.age_25_plus],
            default=0,
        )

        # Add qualified adult and child increases
        qualified_adult_increase = qualified_adults * p.qualified_adult
        qualified_child_increase = qualified_children * p.qualified_child

        # Calculate total weekly payment
        weekly_payment = (
            personal_rate + qualified_adult_increase + qualified_child_increase
        )

        # Convert to annual and apply eligibility
        annual_payment = where(eligible, weekly_payment * 52, 0)

        return annual_payment
