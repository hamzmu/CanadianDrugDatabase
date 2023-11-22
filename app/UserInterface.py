import sys
from datetime import time


def get_code() -> str:
    codes = ["DIF", "CIF", "AI", "DFM", "PTY", "PST", "ROA", "DSC", "DST", "TCL"]
    print("DIF - Drug Information")
    print("CIF - Company Information")
    print("AIN - Active Ingredient ")
    print("DFM - Dosage Form")
    print("PTY - Packaging Type")
    print("PST - Pharmaceutical Standard")
    print("ROA - Route of Administration")
    print("DSC - Drug Schedule")
    print("DST - Drug Status")
    print("TCL - Therapeutic Class")
    user_input = input("Enter Code: ")
    if user_input not in codes:
        return "error"
    return user_input

def exit_program():
    print("Exiting the program...")
    sys.exit(0)
