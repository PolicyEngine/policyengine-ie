# Changelog

All notable changes to PolicyEngine Ireland will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-08-24

### Added

- Initial implementation of PolicyEngine Ireland microsimulation model
- Irish tax system including Income Tax, USC, and PRSI
- Social protection benefits including Jobseeker's Allowance, State Pension, and Child Benefit
- Tax credits system with personal, PAYE, and other credits
- Housing Assistance Payment (HAP) calculations
- Working Family Payment and family supports
- Comprehensive test suite with TDD approach
- CI/CD pipeline with GitHub Actions
- Documentation using Jupyter Book 2.0 (MyST-NB)
- Support for EUR currency throughout
- Entity definitions for Person, TaxUnit, BenefitUnit, Family, and Household
- Parameters organized by Irish government departments (Revenue, DSP, Housing)
- Variables implementing official Irish tax and benefit calculations