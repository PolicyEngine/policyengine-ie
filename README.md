# PolicyEngine Ireland

[![PyPI](https://img.shields.io/pypi/v/policyengine-ie)](https://pypi.org/project/policyengine-ie/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/policyengine-ie)](https://pypi.org/project/policyengine-ie/)
[![License](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Tests](https://github.com/PolicyEngine/policyengine-ie/actions/workflows/test.yml/badge.svg)](https://github.com/PolicyEngine/policyengine-ie/actions/workflows/test.yml)

PolicyEngine's microsimulation model for the Irish tax and benefit system. This model enables researchers, policymakers, and citizens to analyze the impacts of tax and benefit reforms in Ireland.

## Features

- **Comprehensive Tax System**: Income tax, USC (Universal Social Charge), PRSI (Pay Related Social Insurance), and VAT
- **Social Security Benefits**: Jobseeker's Allowance/Benefit, State Pension, Child Benefit, Working Family Payment, HAP, and more
- **Tax Credits System**: Personal, employee, and other tax credits
- **State-Level Modeling**: Support for different local authorities and rates
- **Reform Modeling**: Analyze the impact of policy changes on households and society

## Installation

### Prerequisites

- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`

### Install from PyPI

```bash
pip install policyengine-ie
```

### Development Installation

```bash
git clone https://github.com/PolicyEngine/policyengine-ie.git
cd policyengine-ie
make install
```

## Quick Start

```python
from policyengine_ie import IrishTaxBenefitSystem

# Create a tax-benefit system
system = IrishTaxBenefitSystem()

# Create a household
from policyengine_core.simulations import Simulation

simulation = Simulation(system=system)

# Add people
simulation.add_person(
    person_id="person_1",
    age=35,
    employment_income=50000,  # €50,000 annual income
)

simulation.add_person(
    person_id="person_2", 
    age=8,  # Child
)

# Define household structure
simulation.add_tax_unit(
    tax_unit_id="tax_unit_1",
    adults=["person_1"],
    children=["person_2"],
)

simulation.add_household(
    household_id="household_1",
    members=["person_1", "person_2"],
)

# Calculate tax and benefit variables
income_tax = simulation.calculate("income_tax", period="2024")
usc = simulation.calculate("usc", period="2024")
child_benefit = simulation.calculate("child_benefit", period="2024")

print(f"Income Tax: €{income_tax['person_1']:.2f}")
print(f"USC: €{usc['person_1']:.2f}")
print(f"Child Benefit: €{child_benefit['person_2']:.2f}")
```

## Tax System Coverage

### Taxes
- **Income Tax**: Progressive rates (20% standard, 40% higher)
- **Universal Social Charge (USC)**: Surcharge on income
- **PRSI (Pay Related Social Insurance)**: Social insurance contributions
- **VAT**: Value Added Tax (23% standard, 13.5% and 9% reduced rates)

### Benefits & Social Protection
- **Jobseeker's Allowance/Benefit**: Unemployment support
- **State Pension (Contributory)**: Contributory old-age pension  
- **State Pension (Non-Contributory)**: Non-contributory old-age pension
- **Child Benefit**: Universal child payment
- **Working Family Payment**: In-work family support
- **Housing Assistance Payment (HAP)**: Housing support
- **Disability Allowance**: Support for disabled individuals
- **One-Parent Family Payment**: Support for single parents
- **Carer's Allowance**: Support for carers

### Tax Credits
- **Personal Tax Credit**: Basic personal allowance
- **PAYE Tax Credit**: Employee tax credit
- **Age Tax Credit**: Additional credit for older taxpayers
- **Incapacitated Child Tax Credit**: Support for families with disabled children

## System Architecture

PolicyEngine Ireland follows the same high-quality architecture as other PolicyEngine models:

```
policyengine_ie/
├── entities.py              # Person, TaxUnit, BenefitUnit, Family, Household
├── system.py               # Main system class
├── parameters/             # Policy parameters (YAML files)
│   └── gov/               # Organized by government department
│       ├── revenue/       # Revenue Commissioners (taxes)
│       ├── dsp/          # Dept of Social Protection (benefits)
│       └── housing/      # Dept of Housing (HAP, etc.)
├── variables/             # Policy calculations (Python files)
│   └── gov/              # Same organization as parameters
├── reforms/              # Pre-defined policy reforms
└── tests/                # Comprehensive test suite
```

## Data Sources

All parameters and calculations are based on official Irish government sources:

- **Revenue Commissioners**: [revenue.ie](https://revenue.ie) - Tax rates, credits, and thresholds
- **Citizens Information**: [citizensinformation.ie](https://citizensinformation.ie) - Benefit eligibility and rates
- **Department of Social Protection**: [gov.ie/dsp](https://gov.ie/dsp) - Social welfare payments
- **Department of Housing**: [gov.ie/housing](https://gov.ie/housing) - Housing supports
- **Central Statistics Office**: [cso.ie](https://cso.ie) - Economic indicators

## Testing

We use comprehensive test-driven development:

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run only policy tests
make test-lite
```

## Documentation

Full documentation is available at [policyengine.org/ie/api](https://policyengine.org/ie/api).

Build documentation locally:

```bash
make documentation
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Write tests for your changes
4. Implement your changes
5. Run tests and formatting: `make format test`
6. Submit a pull request

## License

This project is licensed under the GNU Affero General Public License v3.0 - see [LICENSE](LICENSE) for details.

## Citation

If you use PolicyEngine Ireland in academic research, please cite:

```bibtex
@software{policyengine_ireland,
  title = {PolicyEngine Ireland: A microsimulation model of the Irish tax and benefit system},
  author = {{PolicyEngine}},
  url = {https://github.com/PolicyEngine/policyengine-ie},
  version = {0.1.0},
  year = {2024}
}
```

## Contact

- Website: [policyengine.org](https://policyengine.org)
- Email: hello@policyengine.org
- GitHub Issues: [Issues](https://github.com/PolicyEngine/policyengine-ie/issues)