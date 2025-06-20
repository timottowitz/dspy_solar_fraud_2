# client_data.py

def get_john_doe_data():
    """Returns a dictionary with all the variables for a new client case."""
    return {
        "client_name": "John Doe",
        "client_address": "123 Maple St, Houston, TX 77002",
        "financing_institution_name": "SolarFinance Corp",
        "installer_name": "BrightFuture Solar",
        "installation_date": "October 15, 2022",
        "loan_amount": "55,200.00",
        "monthly_payment": "210.00, increasing to 285.00 after 18 months",
        "system_output_status": "System has consistently underproduced, generating less than 40% of the promised electricity. It has never eliminated the client's utility bill.",
        "expert_findings_summary": "Expert report by 'Solar Forensics Inc.' found the system was oversized by 30% for the property's needs and used suboptimal, east-facing panel placement, reducing potential output. The price per watt was $5.10, significantly above the regional average.",
        "roof_report_summary": "Roof inspection revealed 12 improperly sealed mounting brackets, leading to a slow leak into the attic. Estimated repair cost is $7,500.",
        "medical_disability_summary": "Mr. Doe is a 68-year-old retiree on a fixed income.",
        "zoom_transcript_excerpt": "'They told me my electric bill would be gone. GONE. Now I have the loan and my electric bill is almost the same. I feel like a fool. I can't sleep thinking about this debt.'",
        "ucc_lien_filing_date": "November 1, 2022",
        "ucc_lien_entity_name": "SolarFinance Corp",
        "sales_rep_promises": [
            "Your electric bill will be replaced by the solar loan payment.",
            "You will receive a 30% tax credit from the government as a cash rebate.",
            "The system will add over $40,000 to your home's value.",
            "The loan payment will never increase."
        ],
        "financing_terms_summary": "25-year loan at 2.99% APR, with a 30% prepayment required at 18 months to maintain the initial monthly payment.",
        "income_level_description": "a retiree living on a fixed pension and social security.",
    }
