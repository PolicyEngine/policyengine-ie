"""Universal Social Charge (USC) calculation."""

from policyengine_ie.model_api import *


class usc(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Universal Social Charge (USC)"
    documentation = """
    USC is charged on gross income at progressive rates.
    No USC is payable if gross income is €13,000 or less.
    Reduced rates apply for those aged 70+ or with full medical cards (if income ≤ €60,000).
    """
    unit = EUR
    reference = "https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx"

    def formula(person, period, parameters):
        gross_income = person("gross_income_for_usc", period)
        age = person("age", period)
        has_medical_card = person("has_medical_card", period, options=[False])

        p = parameters(period).gov.revenue.usc

        # Check if exempt from USC
        exempt = gross_income <= p.thresholds.exemption_threshold

        # Check if eligible for reduced rates
        eligible_for_reduced_rates = logical_or(
            age >= 70, has_medical_card
        ) * (gross_income <= p.thresholds.reduced_rate_income_threshold)

        # Calculate USC using progressive rates
        band_1_threshold = p.thresholds.band_1_upper
        band_2_threshold = p.thresholds.band_2_upper
        band_3_threshold = p.thresholds.band_3_upper

        # Band 1: First €12,012
        band_1_income = min_(gross_income, band_1_threshold)
        band_1_rate = where(
            eligible_for_reduced_rates, p.rates.reduced_band_1, p.rates.band_1
        )
        band_1_usc = band_1_income * band_1_rate

        # Band 2: €12,012.01 to €25,760
        band_2_income = max_(
            0,
            min_(
                gross_income - band_1_threshold,
                band_2_threshold - band_1_threshold,
            ),
        )
        band_2_rate = where(
            eligible_for_reduced_rates, p.rates.reduced_band_2, p.rates.band_2
        )
        band_2_usc = band_2_income * band_2_rate

        # Band 3: €25,760.01 to €70,044
        band_3_income = max_(
            0,
            min_(
                gross_income - band_2_threshold,
                band_3_threshold - band_2_threshold,
            ),
        )
        band_3_rate = where(
            eligible_for_reduced_rates, p.rates.reduced_band_3, p.rates.band_3
        )
        band_3_usc = band_3_income * band_3_rate

        # Band 4: Above €70,044
        band_4_income = max_(0, gross_income - band_3_threshold)
        band_4_rate = p.rates.band_4  # No reduced rate for highest band
        band_4_usc = band_4_income * band_4_rate

        total_usc = band_1_usc + band_2_usc + band_3_usc + band_4_usc

        # Apply exemption
        return where(exempt, 0, total_usc)
