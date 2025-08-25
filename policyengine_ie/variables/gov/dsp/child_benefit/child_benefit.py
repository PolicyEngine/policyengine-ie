"""Child Benefit calculation."""

from policyengine_ie.model_api import *


class child_benefit(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Child Benefit"
    documentation = """
    Child Benefit is a universal payment made to the parents or guardians of children.
    Different rates apply for children under 12 and those aged 12 and over.
    Special rates apply for twins and multiple births.
    Paid monthly but calculated annually here.
    """
    unit = EUR
    reference = "https://www.citizensinformation.ie/en/social-welfare/social-welfare-payments/families-and-children/child-benefit/"
    
    def formula(person, period, parameters):
        age = person("age", period)
        is_twin = person("is_twin", period, options=[False])
        is_multiple_birth = person("is_multiple_birth", period, options=[False])  # Triplet or higher
        
        p = parameters(period).gov.dsp.child_benefit.rates
        
        # Determine if eligible (under 18, or under 22 if in full-time education)
        is_in_education = person("is_in_full_time_education", period, options=[False])
        eligible = logical_or(
            age < p.upper_age_limit,
            logical_and(age < p.upper_age_limit_education, is_in_education)
        )
        
        # Determine rate based on age
        monthly_rate = where(
            age < p.age_threshold_12,
            p.child_under_12,
            p.child_12_and_over
        )
        
        # Apply multipliers for multiple births
        final_rate = select(
            [is_multiple_birth, is_twin],
            [monthly_rate * p.multiple_births_multiplier, monthly_rate * p.twins_multiplier],
            default=monthly_rate
        )
        
        # Convert monthly to annual and apply eligibility
        annual_benefit = where(eligible, final_rate * 12, 0)
        
        return annual_benefit