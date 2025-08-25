# PolicyEngine Ireland

Welcome to the documentation for PolicyEngine Ireland, a comprehensive microsimulation model of the Irish tax and benefit system.

## About

PolicyEngine Ireland enables researchers, policymakers, and citizens to analyze the impacts of tax and benefit reforms in Ireland. The model implements Ireland's complex fiscal system with high fidelity, including:

- **Income Tax**: Progressive rates (20% standard, 40% higher) with various tax credits
- **Universal Social Charge (USC)**: Progressive surcharge on income 
- **PRSI**: Pay Related Social Insurance contributions for employees and employers
- **Social Protection**: Jobseeker's payments, State Pension, Child Benefit, and family supports
- **Housing Supports**: Housing Assistance Payment (HAP) and related schemes

## Key Features

```{admonition} Production-Ready Model
:class: tip
PolicyEngine Ireland follows the same high-quality architecture as other PolicyEngine models, with comprehensive testing, official parameter sources, and rigorous validation.
```

- **EUR Currency**: All calculations in Euro with official Irish government rates
- **Official Sources**: Parameters sourced from Revenue.ie, Citizens Information, and Department of Social Protection
- **Entity Structure**: Person, TaxUnit, BenefitUnit, Family, and Household entities
- **Test-Driven Development**: Comprehensive test suite with policy scenario validation
- **Reform Modeling**: Analyze impacts of policy changes on households and society
- **API Compatibility**: Works with PolicyEngine's web application and API

## Quick Example

```python
from policyengine_ie import IrishTaxBenefitSystem
from policyengine_core.simulations import Simulation

# Create system and simulation
system = IrishTaxBenefitSystem()
simulation = Simulation(system=system)

# Add a person earning €50,000
simulation.add_person(
    person_id="person_1",
    age=35,
    employment_income=50000
)

# Calculate taxes and benefits
income_tax = simulation.calculate("income_tax", "2024")
usc = simulation.calculate("usc", "2024")
employee_prsi = simulation.calculate("employee_prsi", "2024")

print(f"Income Tax: €{income_tax['person_1']:.2f}")
print(f"USC: €{usc['person_1']:.2f}")  
print(f"Employee PRSI: €{employee_prsi['person_1']:.2f}")
```

## System Coverage

### Taxes Implemented
- Income Tax with progressive rates and tax credits
- Universal Social Charge (USC) with age and medical card exemptions
- PRSI employee and employer contributions
- VAT (parameter structure ready for implementation)

### Benefits Implemented  
- Child Benefit (universal payment with age-based rates)
- Jobseeker's Allowance (means-tested unemployment support)
- State Pension (contributory and non-contributory)
- Working Family Payment (in-work family support)
- Housing Assistance Payment (HAP) - structure ready

### Key Differentiators
- **Irish Specificity**: Captures unique aspects like USC, PRSI classes, and Irish benefit structure
- **County-Level Modeling**: Support for 32 counties and local authority variations
- **Family Structure**: Sophisticated modeling of Irish family assessment units
- **Means Testing**: Accurate implementation of Irish social protection means tests

## Getting Started

Ready to start using PolicyEngine Ireland? Check out the [installation guide](installation.md) and [quickstart tutorial](quickstart.md).

## Government Sources

All parameters are sourced from official Irish government websites:

- **Revenue Commissioners**: [revenue.ie](https://revenue.ie) - Tax rates and credits
- **Citizens Information**: [citizensinformation.ie](https://citizensinformation.ie) - Benefit rates and eligibility
- **Department of Social Protection**: [gov.ie/dsp](https://gov.ie/dsp) - Social welfare policy
- **Department of Housing**: [gov.ie/housing](https://gov.ie/housing) - Housing supports

---

*PolicyEngine Ireland is part of the [PolicyEngine](https://policyengine.org) ecosystem, making tax and benefit policy analysis accessible to everyone.*