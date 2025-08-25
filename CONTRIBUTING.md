# Contributing to PolicyEngine Ireland

Thank you for your interest in contributing to PolicyEngine Ireland! This document provides guidelines and information for contributors.

## Code of Conduct

By participating in this project, you agree to abide by the [PolicyEngine Code of Conduct](https://policyengine.org/code-of-conduct).

## How to Contribute

### 1. Reporting Issues

- Use the [GitHub Issues](https://github.com/PolicyEngine/policyengine-ie/issues) page
- Check if the issue already exists before creating a new one
- Provide clear, detailed descriptions with examples
- Include information about your environment (Python version, OS, etc.)

### 2. Suggesting Enhancements

- Open an issue with the "enhancement" label
- Clearly describe the proposed feature and its benefits
- Include examples of how it would be used
- Reference official Irish government sources where applicable

### 3. Contributing Code

#### Setup Development Environment

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/policyengine-ie.git
   cd policyengine-ie
   ```

3. Install in development mode:
   ```bash
   make install
   ```

4. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Development Workflow

1. **Make changes** following the coding standards below
2. **Add tests** for any new functionality
3. **Run tests** to ensure nothing is broken:
   ```bash
   make test
   ```
4. **Format code** before committing:
   ```bash
   make format
   ```
5. **Commit changes** with clear, descriptive messages
6. **Push to your fork** and create a pull request

## Coding Standards

### Python Code Style

- **Formatter**: Use Black with 79-character line length
- **Import organization**: stdlib, third-party, local (alphabetized within groups)
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Type hints**: Use where helpful, especially for public APIs
- **Docstrings**: Required for all public functions and classes

Example:
```python
"""Module for calculating Irish income tax."""

from policyengine_ie.model_api import *


class income_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income tax"
    documentation = """
    Total income tax liability before tax credits.
    Ireland has two rates: 20% (standard rate) and 40% (higher rate).
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx"
    
    def formula(person, period, parameters):
        # Implementation here
        pass
```

### Parameter Files (YAML)

- Use lowercase, descriptive names
- Include official government references
- Organize by Irish government department structure
- Include metadata (unit, currency, period)

Example:
```yaml
description: Irish income tax rates by bracket
reference:
  - title: Tax rates, bands and reliefs
    href: https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx
metadata:
  unit: /1
  label: Income tax rates
  currency: EUR

standard_rate:
  description: Standard rate of income tax (first bracket)
  values:
    2024-01-01: 0.20
```

### Test Requirements

- Write tests for all new functionality
- Use descriptive test names
- Include both unit tests and policy scenario tests
- Test edge cases and boundary conditions

Example test file structure:
```yaml
- name: Income tax calculation for middle earner
  description: Test income tax for €50,000 employment income
  period: 2024
  input:
    people:
      person_1:
        age: 35
        employment_income: 50000
  output:
    income_tax:
      person_1: 3600  # Expected result with explanation
```

## Parameter and Variable Guidelines

### Adding New Parameters

1. **Source from official government websites**:
   - Revenue.ie for tax parameters
   - Citizens Information for benefit rates
   - Department of Social Protection for social welfare

2. **Include proper references**:
   ```yaml
   reference:
     - title: Official document name
       href: https://official-government-url
   ```

3. **Follow directory structure**:
   ```
   parameters/gov/{department}/{policy_area}/{specific_parameter}.yaml
   ```

### Adding New Variables

1. **One variable per file** (follow recent PolicyEngine patterns)
2. **Include comprehensive documentation**
3. **Reference legislation or official sources**
4. **Use correct entity and time period**

Example directory structure:
```
variables/gov/revenue/income_tax/income_tax.py
variables/gov/dsp/child_benefit/child_benefit.py
```

## Irish Government Structure

Organize parameters and variables by Irish government departments:

- **Revenue** (`gov/revenue/`): Income tax, USC, PRSI, VAT
- **DSP** (`gov/dsp/`): Social protection benefits
- **Housing** (`gov/housing/`): HAP, housing supports
- **Local Government** (`gov/local_gov/`): Local authority variations

## Data Sources and Accuracy

### Primary Sources (in order of preference)

1. **Revenue Commissioners**: [revenue.ie](https://revenue.ie)
2. **Citizens Information**: [citizensinformation.ie](https://citizensinformation.ie)
3. **Department of Social Protection**: [gov.ie/dsp](https://gov.ie/dsp)
4. **Irish Statute Book**: [irishstatutebook.ie](https://irishstatutebook.ie)

### Secondary Sources

- OECD Tax-Benefit models
- Academic research papers
- Professional services firm publications (PWC, KPMG, etc.)

**Always preference official government sources over secondary sources.**

## Pull Request Process

1. **Ensure CI passes**: All tests must pass and code must be properly formatted
2. **Update documentation**: Add or update relevant documentation
3. **Add changelog entry**: Create `changelog_entry.yaml` if needed
4. **Request review**: Tag maintainers for review
5. **Address feedback**: Make requested changes promptly

### Pull Request Template

```markdown
## Description
Brief description of changes

## Changes Made
- List of specific changes
- Reference to issues fixed (e.g., "Fixes #123")

## Testing
- [ ] Tests added for new functionality
- [ ] All existing tests pass
- [ ] Manual testing performed

## Documentation
- [ ] Code is documented
- [ ] User documentation updated if needed

## Government Sources
- [ ] All parameters sourced from official Irish government websites
- [ ] References included in YAML files
```

## Release Process

Releases are handled by maintainers following semantic versioning:
- **Patch** (0.1.1): Bug fixes, parameter updates
- **Minor** (0.2.0): New features, new benefits/taxes
- **Major** (1.0.0): Breaking changes, major restructuring

## Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **PolicyEngine Slack**: For real-time help (contact maintainers for invite)

## Recognition

Contributors are recognized in:
- GitHub contributor graphs
- Release notes for significant contributions
- Project documentation for major features

Thank you for helping make Irish tax-benefit policy analysis more accessible!