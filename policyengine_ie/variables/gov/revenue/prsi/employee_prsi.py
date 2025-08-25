"""Employee PRSI contribution calculation."""

from policyengine_ie.model_api import *


class employee_prsi(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Employee PRSI"
    documentation = """
    Employee PRSI (Pay Related Social Insurance) contributions.
    Rate is 4.1% for Class A employees earning over €352 per week.
    A weekly credit of €12 applies for those earning between €352.01 and €424.
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/prsi.aspx"
    
    def formula(person, period, parameters):
        employment_income = person("employment_income", period)
        prsi_class = person("prsi_class", period, options=["A"])  # Default to Class A
        age = person("age", period)
        
        p = parameters(period).gov.revenue.prsi
        
        # Convert annual to weekly for threshold comparison
        weekly_earnings = employment_income / 52
        
        # Check if exempt (under 16 or over 70 from 2024)
        exempt_age = logical_or(age < 16, age >= 70)
        
        # Check if below minimum earnings threshold
        below_threshold = weekly_earnings <= p.thresholds.employee_weekly_threshold
        
        # Calculate PRSI rate based on class (simplified to Class A)
        employee_rate = p.employee_rates.class_a
        
        # Calculate base PRSI
        base_prsi = employment_income * employee_rate
        
        # Calculate weekly PRSI credit
        weekly_credit_threshold = p.thresholds.tapered_credit_upper_limit
        max_weekly_credit = p.thresholds.weekly_prsi_credit
        min_threshold = p.thresholds.employee_weekly_threshold
        
        # Credit applies for earnings between €352.01 and €424
        eligible_for_credit = logical_and(
            weekly_earnings > min_threshold,
            weekly_earnings <= weekly_credit_threshold
        )
        
        # Calculate tapered credit
        credit_reduction = max_(0, (weekly_earnings - min_threshold) / 6)
        weekly_credit = max_(0, max_weekly_credit - credit_reduction)
        annual_credit = where(eligible_for_credit, weekly_credit * 52, 0)
        
        # Apply credit
        prsi_after_credit = max_(0, base_prsi - annual_credit)
        
        # Apply exemptions
        final_prsi = where(
            logical_or(exempt_age, below_threshold),
            0,
            prsi_after_credit
        )
        
        return final_prsi