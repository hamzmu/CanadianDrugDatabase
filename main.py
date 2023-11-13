from DataAccess import url_builder, json_response, stats



# Test ID, 48905
id = input("Enter Drug Identification Number (DIN): ")

codes = ["DIF", "AIN", "DFM", "PTY", "PST", "ROA", "DSC", "DST", "TCL"]

code_dict_title = {
    "DIF": "Drug Product Information",
    "AIN": "Active Ingredients",
    "DFM": "Dosage Form",
    "PTY": "Packaging Information",
    "PST": "Pharmaceutical Standard",
    "ROA": "Route of Administration",
    "DSC": "Schedule Information",
    "DST": "Status of Drug",
    "TCL": "Therapeutic Class"
}

for element in codes:
    print(code_dict_title[element] + "\n")
    url = url_builder(element, id)
    if stats(url):
        json_data = json_response(url)
        dict = json_data.items()
        for key, value in json_data.items():
            if value == "":
                value = "no information found"
            print(f"{key}: {value}")
        print("\n")
    else:
        print("*** Error: Code Not Found/Applicable ***" + "\n" + "\n")













