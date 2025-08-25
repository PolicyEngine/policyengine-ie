"""
Entity definitions for the Irish tax and benefit system.

References:
- Revenue Commissioners: https://revenue.ie/
- Citizens Information: https://citizensinformation.ie/
- Department of Social Protection: https://gov.ie/dsp/
"""

from policyengine_core.entities import build_entity


Person = build_entity(
    key="person",
    plural="people",
    label="Person",
    doc="""
    An individual person in Ireland.
    
    This is the base entity for all individual-level calculations including
    income tax, USC, PRSI, and individual social protection payments.
    """,
    is_person=True,
)


TaxUnit = build_entity(
    key="tax_unit",
    plural="tax_units",
    label="Tax unit",
    doc="""
    An Irish tax assessment unit.
    
    In Ireland, individuals are generally assessed separately for tax purposes,
    but married couples can opt for joint assessment. This entity represents
    a tax assessment unit which can be either:
    - Single person assessment
    - Married couple joint assessment
    - Married couple separate assessment
    
    Reference: https://revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/marital-status/joint-assessment/index.aspx
    """,
    containing_entities=["household"],
    roles=[
        {
            "key": "adult",
            "plural": "adults",
            "label": "Adult",
            "doc": "Adult member of the tax unit",
            "max": 2,
        },
        {
            "key": "child",
            "plural": "children",
            "label": "Child",
            "doc": "Dependent child for tax purposes",
        },
    ],
)


BenefitUnit = build_entity(
    key="benefit_unit",
    plural="benefit_units",
    label="Benefit unit",
    doc="""
    A social protection assessment unit for Irish welfare payments.
    
    This represents the unit used to assess eligibility and calculate payments
    for Irish social protection schemes. It typically includes:
    - Single person, or
    - Couple (married/cohabiting), and
    - Any qualified dependent children
    
    The means test considers the combined income and assets of the benefit unit.
    
    Reference: https://citizensinformation.ie/en/social-welfare/irish-social-welfare-system/means-test-for-social-welfare-payments/
    """,
    containing_entities=["household"],
    roles=[
        {
            "key": "adult",
            "plural": "adults",
            "label": "Adult",
            "doc": "Adult member of the benefit unit",
            "max": 2,
        },
        {
            "key": "child",
            "plural": "children",
            "label": "Child",
            "doc": "Qualified child for social protection purposes",
        },
    ],
)


Family = build_entity(
    key="family",
    plural="families",
    label="Family",
    doc="""
    A family unit for child-related payments and supports.
    
    Used primarily for:
    - Child Benefit (universal payment for all children)
    - Working Family Payment (in-work support for families)
    - Back to School Clothing and Footwear Allowance
    - Other family-related payments
    
    Includes parents/guardians and their dependent children under 18 
    (or under 22 if in full-time education).
    
    Reference: https://citizensinformation.ie/en/social-welfare/social-welfare-payments/families-and-children/
    """,
    containing_entities=["household"],
    roles=[
        {
            "key": "parent",
            "plural": "parents",
            "label": "Parent",
            "doc": "Parent or guardian in the family",
            "max": 2,
        },
        {
            "key": "child",
            "plural": "children",
            "label": "Child",
            "doc": "Dependent child in the family",
        },
    ],
)


Household = build_entity(
    key="household",
    plural="households",
    label="Household",
    doc="""
    A physical household in Ireland.
    
    This represents all people living at the same address, used for:
    - Housing Assistance Payment (HAP) calculations
    - Household composition analysis
    - Some means testing that considers household income
    - Local Property Tax assessments
    
    Reference: https://citizensinformation.ie/en/housing/housing-supports/housing-assistance-payment/
    """,
    roles=[
        {
            "key": "member",
            "plural": "members",
            "label": "Member",
            "doc": "A person living in the household",
        },
    ],
)


entities = [Person, TaxUnit, BenefitUnit, Family, Household]
