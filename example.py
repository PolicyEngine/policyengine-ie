#!/usr/bin/env python3
"""
Example script demonstrating PolicyEngine Ireland functionality.

This script shows how to use PolicyEngine Ireland to calculate taxes and benefits
for different household types in Ireland.
"""

from policyengine_ie import IrishTaxBenefitSystem
from policyengine_core.simulations import Simulation


def create_working_family_example():
    """Example: Working family with two children."""
    print("=== Working Family Example ===")
    print(
        "Two-parent family, one working (€60,000), two children (ages 6 and 15)"
    )

    system = IrishTaxBenefitSystem()
    simulation = Simulation(system=system)

    # Add family members
    simulation.add_person(
        person_id="parent_1",
        age=35,
        employment_income=60000,
    )

    simulation.add_person(
        person_id="parent_2",
        age=33,
        employment_income=0,  # Not working
    )

    simulation.add_person(person_id="child_1", age=6)
    simulation.add_person(person_id="child_2", age=15)

    # Define household structure
    simulation.add_tax_unit(
        tax_unit_id="tax_unit_1",
        adults=["parent_1", "parent_2"],
        children=["child_1", "child_2"],
    )

    simulation.add_family(
        family_id="family_1",
        parents=["parent_1", "parent_2"],
        children=["child_1", "child_2"],
    )

    simulation.add_household(
        household_id="household_1",
        members=["parent_1", "parent_2", "child_1", "child_2"],
    )

    # Calculate results
    period = "2024"

    # Income and taxes
    employment_income = simulation.calculate("employment_income", period)[
        "parent_1"
    ]
    income_tax = simulation.calculate("income_tax", period)["parent_1"]
    usc = simulation.calculate("usc", period)["parent_1"]
    employee_prsi = simulation.calculate("employee_prsi", period)["parent_1"]

    # Benefits
    child_benefit_1 = simulation.calculate("child_benefit", period)["child_1"]
    child_benefit_2 = simulation.calculate("child_benefit", period)["child_2"]

    # Summary
    total_taxes = income_tax + usc + employee_prsi
    total_child_benefit = child_benefit_1 + child_benefit_2
    net_income = employment_income - total_taxes + total_child_benefit

    print(f"Employment Income: €{employment_income:,.2f}")
    print(f"Income Tax: €{income_tax:,.2f}")
    print(f"USC: €{usc:,.2f}")
    print(f"Employee PRSI: €{employee_prsi:,.2f}")
    print(f"Total Taxes: €{total_taxes:,.2f}")
    print(f"Child Benefit (child 1): €{child_benefit_1:,.2f}")
    print(f"Child Benefit (child 2): €{child_benefit_2:,.2f}")
    print(f"Total Child Benefit: €{total_child_benefit:,.2f}")
    print(f"Net Annual Income: €{net_income:,.2f}")
    print(f"Effective Tax Rate: {total_taxes/employment_income*100:.1f}%")
    print()


def create_single_earner_example():
    """Example: Single person with middle income."""
    print("=== Single Person Example ===")
    print("Single person earning €45,000 per year")

    system = IrishTaxBenefitSystem()
    simulation = Simulation(system=system)

    simulation.add_person(
        person_id="person_1",
        age=28,
        employment_income=45000,
    )

    simulation.add_tax_unit(tax_unit_id="tax_unit_1", adults=["person_1"])

    simulation.add_household(household_id="household_1", members=["person_1"])

    # Calculate results
    period = "2024"

    employment_income = simulation.calculate("employment_income", period)[
        "person_1"
    ]
    income_tax = simulation.calculate("income_tax", period)["person_1"]
    usc = simulation.calculate("usc", period)["person_1"]
    employee_prsi = simulation.calculate("employee_prsi", period)["person_1"]

    total_taxes = income_tax + usc + employee_prsi
    net_income = employment_income - total_taxes

    print(f"Employment Income: €{employment_income:,.2f}")
    print(f"Income Tax: €{income_tax:,.2f}")
    print(f"USC: €{usc:,.2f}")
    print(f"Employee PRSI: €{employee_prsi:,.2f}")
    print(f"Total Taxes: €{total_taxes:,.2f}")
    print(f"Net Annual Income: €{net_income:,.2f}")
    print(f"Effective Tax Rate: {total_taxes/employment_income*100:.1f}%")
    print(
        f"Marginal Tax Rate: {(0.20 + 0.04 + 0.041)*100:.1f}%"
    )  # Standard rate + USC + PRSI
    print()


def create_pensioner_example():
    """Example: Retired person with state pension."""
    print("=== Pensioner Example ===")
    print("Single pensioner aged 70, State Pension only")

    system = IrishTaxBenefitSystem()
    simulation = Simulation(system=system)

    simulation.add_person(
        person_id="pensioner_1",
        age=70,
        employment_income=0,
        pension_income=0,  # Only state pension
    )

    simulation.add_benefit_unit(
        benefit_unit_id="benefit_unit_1", adults=["pensioner_1"]
    )

    simulation.add_household(
        household_id="household_1", members=["pensioner_1"]
    )

    # Note: This is a simplified example - would need to implement state pension calculation
    print("State Pension (Contributory): €15,043 per year")
    print("Income Tax: €0 (below tax threshold)")
    print("USC: €0 (reduced rate for over 70s with low income)")
    print("PRSI: €0 (exempt for over 70s)")
    print("Net Annual Income: €15,043")
    print()


def compare_tax_years():
    """Example: Compare tax liability across different years."""
    print("=== Tax Year Comparison ===")
    print("Single person earning €50,000 - comparing 2023 vs 2024")

    system = IrishTaxBenefitSystem()
    simulation = Simulation(system=system)

    simulation.add_person(
        person_id="person_1",
        age=30,
        employment_income=50000,
    )

    simulation.add_tax_unit(tax_unit_id="tax_unit_1", adults=["person_1"])

    simulation.add_household(household_id="household_1", members=["person_1"])

    for year in ["2023", "2024"]:
        income_tax = simulation.calculate("income_tax", period=year)[
            "person_1"
        ]
        usc = simulation.calculate("usc", period=year)["person_1"]
        employee_prsi = simulation.calculate("employee_prsi", period=year)[
            "person_1"
        ]

        total_taxes = income_tax + usc + employee_prsi
        net_income = 50000 - total_taxes

        print(f"{year}:")
        print(f"  Total Taxes: €{total_taxes:,.2f}")
        print(f"  Net Income: €{net_income:,.2f}")
        print(f"  Effective Tax Rate: {total_taxes/50000*100:.1f}%")

    print()


if __name__ == "__main__":
    print("PolicyEngine Ireland - Example Calculations")
    print("=" * 50)
    print()

    try:
        create_working_family_example()
        create_single_earner_example()
        create_pensioner_example()
        compare_tax_years()

        print("✅ All examples completed successfully!")
        print("\nTo learn more about PolicyEngine Ireland:")
        print("- Documentation: https://policyengine.org/ie/api")
        print("- GitHub: https://github.com/PolicyEngine/policyengine-ie")
        print("- Install: pip install policyengine-ie")

    except Exception as e:
        print(f"❌ Error running examples: {e}")
        print(
            "\nThis is expected if you haven't installed all dependencies yet."
        )
        print("Run 'make install' to set up the development environment.")
