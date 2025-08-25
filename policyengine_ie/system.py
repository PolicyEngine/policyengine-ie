"""
Irish tax and benefit system implementation.

This module defines the main tax-benefit system class that loads all
parameters and variables for Ireland's social and fiscal policies.
"""

from policyengine_core.taxbenefitsystems import TaxBenefitSystem
from policyengine_ie.entities import entities
from pathlib import Path
import os


COUNTRY_DIR = Path(__file__).parent


class IrishTaxBenefitSystem(TaxBenefitSystem):
    """
    The Irish tax and benefit system.
    
    This class represents the complete Irish tax and benefit system,
    including income tax, USC, PRSI, social protection payments,
    family supports, and housing assistance.
    
    The system follows Irish fiscal years (January to December) and
    uses Euro (EUR) as the base currency.
    """
    
    entities = entities
    parameters_dir = COUNTRY_DIR / "parameters"
    variables_dir = COUNTRY_DIR / "variables"
    auto_carry_over_input_variables = True
    basic_inputs = [
        # Demographics
        "age",
        "is_citizen",
        "is_resident",
        "county",
        
        # Employment and income
        "employment_income", 
        "self_employment_income",
        "investment_income",
        "rental_income",
        "pension_income",
        "social_protection_income",
        
        # Personal circumstances
        "is_disabled",
        "is_carer",
        "is_student",
        "is_lone_parent",
        "marital_status",
        
        # Housing
        "rent",
        "mortgage_interest",
        "property_value",
        "local_authority",
        
        # Assets
        "savings",
        "investments_value",
        "other_assets",
        
        # PRSI
        "prsi_class",
        "prsi_contributions",
        
        # Children
        "number_of_children",
        "childcare_costs",
    ]
    
    def __init__(self, reform=None):
        """
        Initialize the Irish tax-benefit system.
        
        Args:
            reform: Optional reform to apply to the baseline system
        """
        super().__init__(entities)
        
        # Apply reform if provided
        if reform is not None:
            self.apply_reform(reform)
    
    # Entity properties are handled by parent class