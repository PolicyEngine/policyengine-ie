"""
Type definitions for PolicyEngine Ireland.

This module provides type hints and constants used throughout
the Irish tax-benefit system model.
"""

from typing import Union, Dict, Any, List, Optional
from enum import Enum


# County definitions for Ireland
class County(Enum):
    """Irish counties for location-based calculations."""

    # Leinster
    DUBLIN = "dublin"
    KILDARE = "kildare"
    LAOIS = "laois"
    LONGFORD = "longford"
    LOUTH = "louth"
    MEATH = "meath"
    OFFALY = "offaly"
    WESTMEATH = "westmeath"
    WEXFORD = "wexford"
    WICKLOW = "wicklow"
    CARLOW = "carlow"
    KILKENNY = "kilkenny"

    # Munster
    CORK = "cork"
    KERRY = "kerry"
    LIMERICK = "limerick"
    TIPPERARY = "tipperary"
    WATERFORD = "waterford"
    CLARE = "clare"

    # Connacht
    GALWAY = "galway"
    MAYO = "mayo"
    ROSCOMMON = "roscommon"
    SLIGO = "sligo"
    LEITRIM = "leitrim"

    # Ulster (in Republic of Ireland)
    CAVAN = "cavan"
    DONEGAL = "donegal"
    MONAGHAN = "monaghan"


class MaritalStatus(Enum):
    """Marital status for tax and benefit calculations."""

    SINGLE = "single"
    MARRIED = "married"
    SEPARATED = "separated"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    CIVIL_PARTNERSHIP = "civil_partnership"


class PRSIClass(Enum):
    """PRSI contribution classes."""

    CLASS_A = "A"  # Most employees
    CLASS_B = "B"  # Public servants recruited before 6 April 1995
    CLASS_D = "D"  # Public servants recruited on or after 6 April 1995
    CLASS_H = "H"  # Uninsured employees
    CLASS_J = "J"  # Employees under 16 or over 66
    CLASS_K = "K"  # Employees in certain community schemes
    CLASS_M = "M"  # Employees with income under €38 per week
    CLASS_S = "S"  # Self-employed


class LocalAuthority(Enum):
    """Local authorities for housing calculations."""

    # Cities
    DUBLIN_CITY = "dublin_city"
    CORK_CITY = "cork_city"
    GALWAY_CITY = "galway_city"
    LIMERICK_CITY = "limerick_city"
    WATERFORD_CITY = "waterford_city"

    # Counties (sample - would include all 31)
    DUN_LAOGHAIRE_RATHDOWN = "dun_laoghaire_rathdown"
    FINGAL = "fingal"
    SOUTH_DUBLIN = "south_dublin"
    CORK_COUNTY = "cork_county"
    # ... (would include all local authorities)


# Type aliases
Amount = Union[int, float]
Rate = Union[int, float]
Threshold = Union[int, float]
Year = int
Period = str
