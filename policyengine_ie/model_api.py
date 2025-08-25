"""
API for PolicyEngine Ireland model.

This module provides the main imports needed for defining variables and parameters
in the Irish tax and benefit system model.
"""

# Core imports from policyengine-core
from policyengine_core.variables import Variable
from policyengine_core.parameters import Parameter
from policyengine_core.periods import YEAR, MONTH, ETERNITY, period
from policyengine_core.holders import set_input_dispatch_by_period
from policyengine_core.reforms import Reform
from policyengine_core.simulations import Simulation
from numpy import (
    maximum as max_,
    minimum as min_,
    round as round_,
    where,
    select,
    logical_and,
    logical_or,
    logical_not,
)

# Entity imports
from policyengine_ie.entities import (
    Person,
    TaxUnit,
    BenefitUnit,
    Family,
    Household,
    entities,
)

# Currency and unit definitions
EUR = "currency-EUR"