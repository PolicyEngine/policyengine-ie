# Quickstart Guide

This guide will get you up and running with PolicyEngine Ireland in just a few minutes.

## Basic Usage

### 1. Import the System

```python
from policyengine_ie import IrishTaxBenefitSystem
from policyengine_core.simulations import Simulation

# Create the Irish tax-benefit system
system = IrishTaxBenefitSystem()
```

### 2. Create a Simulation

```python
# Initialize a simulation
simulation = Simulation(system=system)
```

### 3. Add People and Households

```python
# Add a working adult
simulation.add_person(
    person_id="adult_1",
    age=35,
    employment_income=50000,  # €50,000 annual employment income
)

# Add a child
simulation.add_person(
    person_id="child_1", 
    age=8,
)

# Define family and household structure
simulation.add_tax_unit(
    tax_unit_id="tax_unit_1",
    adults=["adult_1"],
    children=["child_1"],
)

simulation.add_family(
    family_id="family_1",
    parents=["adult_1"],
    children=["child_1"],
)

simulation.add_household(
    household_id="household_1",
    members=["adult_1", "child_1"],
)
```

### 4. Calculate Tax and Benefit Variables

```python
# Calculate taxes
income_tax = simulation.calculate("income_tax", period="2024")
usc = simulation.calculate("usc", period="2024")
employee_prsi = simulation.calculate("employee_prsi", period="2024")

# Calculate benefits
child_benefit = simulation.calculate("child_benefit", period="2024")

# Display results
print("=== Irish Tax-Benefit Calculation ===")
print(f"Employment Income: €{simulation.calculate('employment_income', '2024')['adult_1']:,.2f}")
print(f"Income Tax: €{income_tax['adult_1']:,.2f}")
print(f"USC: €{usc['adult_1']:,.2f}")
print(f"Employee PRSI: €{employee_prsi['adult_1']:,.2f}")
print(f"Total Taxes: €{income_tax['adult_1'] + usc['adult_1'] + employee_prsi['adult_1']:,.2f}")
print(f"Child Benefit: €{child_benefit['child_1']:,.2f}")
```

Expected output:
```
=== Irish Tax-Benefit Calculation ===
Employment Income: €50,000.00
Income Tax: €3,600.00
USC: €1,570.44
Employee PRSI: €2,050.00
Total Taxes: €7,220.44
Child Benefit: €2,208.00
```

## Common Scenarios

### Single Person with No Children

```python
system = IrishTaxBenefitSystem()
simulation = Simulation(system=system)

simulation.add_person(
    person_id="person_1",
    age=30,
    employment_income=40000,
)

simulation.add_tax_unit(
    tax_unit_id="tax_unit_1",
    adults=["person_1"]
)

simulation.add_household(
    household_id="household_1",
    members=["person_1"]
)

# Calculate net income
gross_income = simulation.calculate("employment_income", "2024")["person_1"]
taxes = (
    simulation.calculate("income_tax", "2024")["person_1"] +
    simulation.calculate("usc", "2024")["person_1"] +
    simulation.calculate("employee_prsi", "2024")["person_1"]
)
net_income = gross_income - taxes

print(f"Gross Income: €{gross_income:,.2f}")
print(f"Total Taxes: €{taxes:,.2f}")
print(f"Net Income: €{net_income:,.2f}")
print(f"Effective Tax Rate: {taxes/gross_income*100:.1f}%")
```

### Unemployed Person with Children

```python
system = IrishTaxBenefitSystem()
simulation = Simulation(system=system)

# Add unemployed parent
simulation.add_person(
    person_id="parent_1",
    age=32,
    employment_income=0,
    is_unemployed=True,
)

# Add two children
simulation.add_person(person_id="child_1", age=6)
simulation.add_person(person_id="child_2", age=14)

# Set up benefit unit for social protection
simulation.add_benefit_unit(
    benefit_unit_id="benefit_unit_1",
    adults=["parent_1"],
    children=["child_1", "child_2"]
)

simulation.add_family(
    family_id="family_1", 
    parents=["parent_1"],
    children=["child_1", "child_2"]
)

# Calculate benefits
jobseekers = simulation.calculate("jobseekers_allowance", "2024")["parent_1"]
child_benefit_1 = simulation.calculate("child_benefit", "2024")["child_1"]
child_benefit_2 = simulation.calculate("child_benefit", "2024")["child_2"]

total_benefits = jobseekers + child_benefit_1 + child_benefit_2

print(f"Jobseeker's Allowance: €{jobseekers:,.2f}")
print(f"Child Benefit (age 6): €{child_benefit_1:,.2f}")
print(f"Child Benefit (age 14): €{child_benefit_2:,.2f}")
print(f"Total Annual Benefits: €{total_benefits:,.2f}")
```

### Pensioner

```python
system = IrishTaxBenefitSystem()
simulation = Simulation(system=system)

simulation.add_person(
    person_id="pensioner_1",
    age=70,
    pension_income=20000,  # Private pension
)

simulation.add_benefit_unit(
    benefit_unit_id="benefit_unit_1",
    adults=["pensioner_1"]
)

# Calculate state pension and taxes
state_pension = simulation.calculate("state_pension_contributory", "2024")["pensioner_1"]
income_tax = simulation.calculate("income_tax", "2024")["pensioner_1"]
usc = simulation.calculate("usc", "2024")["pensioner_1"]  # Reduced rate for over 70s

total_income = 20000 + state_pension
total_taxes = income_tax + usc

print(f"Private Pension: €{20000:,.2f}")
print(f"State Pension: €{state_pension:,.2f}")
print(f"Total Gross Income: €{total_income:,.2f}")
print(f"Income Tax: €{income_tax:,.2f}")
print(f"USC (reduced rate): €{usc:,.2f}")
print(f"Net Income: €{total_income - total_taxes:,.2f}")
```

## Key Variables Reference

### Input Variables (What You Set)
- `age` - Person's age in years
- `employment_income` - Annual gross employment income (€)
- `self_employment_income` - Annual self-employment profit (€)
- `is_unemployed` - Whether person is unemployed
- `is_student` - Whether person is a student
- `county` - Irish county for location-based calculations

### Tax Variables (What Gets Calculated)
- `income_tax` - Irish income tax liability
- `usc` - Universal Social Charge
- `employee_prsi` - Employee PRSI contributions
- `taxable_income` - Income subject to tax after deductions

### Benefit Variables (What Gets Calculated)
- `child_benefit` - Universal child payment
- `jobseekers_allowance` - Unemployment support
- `state_pension_contributory` - State pension (contributory)
- `working_family_payment` - In-work family support

## Time Periods

PolicyEngine Ireland uses annual calculations by default. Specify the year:

```python
# Calculate for different years
results_2024 = simulation.calculate("income_tax", period="2024")
results_2023 = simulation.calculate("income_tax", period="2023")
```

## Next Steps

Now that you've mastered the basics:

1. **Explore the Tax System**: Learn about [Income Tax](tax_system/income_tax.md), [USC](tax_system/usc.md), and [PRSI](tax_system/prsi.md)
2. **Understand Benefits**: Check out [Child Benefit](benefits_system/child_benefit.md) and [Social Protection](benefits_system/jobseekers.md)
3. **Try Advanced Examples**: See [policy reform modeling](examples/policy_reform.md)
4. **Read the API Reference**: Full variable and parameter documentation