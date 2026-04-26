"""Default input variables used by Irish policy formulas."""

from policyengine_ie.model_api import *


class investment_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Investment income"
    unit = EUR
    default_value = 0


class rental_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Rental income"
    unit = EUR
    default_value = 0


class pension_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Pension income"
    unit = EUR
    default_value = 0


class total_deductions(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total deductions"
    unit = EUR
    default_value = 0


class is_twin(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is a twin"
    default_value = False


class is_multiple_birth(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is from a multiple birth"
    default_value = False


class is_in_full_time_education(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is in full-time education"
    default_value = False


class is_unemployed(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is unemployed"
    default_value = False


class is_available_for_work(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is available for work"
    default_value = True


class is_genuinely_seeking_work(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is genuinely seeking work"
    default_value = True


class is_living_independently(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is living independently"
    default_value = False


class has_housing_support(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Has housing support"
    default_value = False


class has_medical_card(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Has medical card"
    default_value = False


class is_renting(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is renting"
    default_value = False


class has_child_carer_credit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Has child carer credit"
    default_value = False


class has_spouse_income(Variable):
    value_type = bool
    entity = TaxUnit
    definition_period = YEAR
    label = "Has spouse income"
    default_value = False


class prsi_class(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "PRSI class"
    default_value = "A"
