print("========= HOSPITAL BILLING SYSTEM =========")


concession_rates = {
    "general": 0,
    "senior": 10,
    "insurance": 15,
    "bpl": 25
}


MAX_CONCESSION = 5000


patient_id = input("Enter Patient ID: ")
patient_name = input("Enter Patient Name: ")
patient_type = input(
    "Enter Patient Type (general/senior/insurance/bpl): "
).lower()


if patient_type not in concession_rates:
    print("Invalid patient category!")
else:

    
    consultation = float(input("Enter Consultation Charges: Rs. "))
    diagnostic = float(input("Enter Diagnostic Charges: Rs. "))
    treatment = float(input("Enter Treatment Charges: Rs. "))

    
    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Invalid billing! Charges cannot be negative.")

    else:
       
        total_bill = consultation + diagnostic + treatment

        
        concession_rate = concession_rates[patient_type]

        
        calculated_concession = (
            total_bill * concession_rate / 100
        )

        
        concession = min(
            calculated_concession,
            MAX_CONCESSION
        )

        
        final_amount = total_bill - concession

        
        if final_amount > 20000:
            classification = "High Payment Category"
        elif final_amount > 5000:
            classification = "Medium Payment Category"
        else:
            classification = "Low Payment Category"

        
        print("\n========== HOSPITAL INVOICE ==========")

        print("Patient ID          :", patient_id)
        print("Patient Name        :", patient_name)
        print("Patient Type        :", patient_type.upper())

        print("--------------------------------------")

        print("Consultation Charges: Rs.",
              round(consultation, 2))

        print("Diagnostic Charges  : Rs.",
              round(diagnostic, 2))

        print("Treatment Charges   : Rs.",
              round(treatment, 2))

        print("--------------------------------------")

        print("Total Bill          : Rs.",
              round(total_bill, 2))

        print("Concession Rate     :",
              concession_rate, "%")

        print("Calculated Concession: Rs.",
              round(calculated_concession, 2))

        print("Maximum Concession  : Rs.",
              MAX_CONCESSION)

        print("Final Concession    : Rs.",
              round(concession, 2))

        print("--------------------------------------")

        print("Final Payable Amount: Rs.",
              round(final_amount, 2))

        print("Patient Classification:",
              classification)

        print("======================================")
