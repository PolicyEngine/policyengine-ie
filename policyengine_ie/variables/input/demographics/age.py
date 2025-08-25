"""Age of person."""

from policyengine_ie.model_api import *


class age(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Age"
    documentation = "Age of the person in years"
    unit = "year"