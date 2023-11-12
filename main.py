from datetime import time
from DataAccess import url_builder, json_response, stats
from UserInterface import get_code, exit_program



# Test ID, 48905
id = input("Enter Drug Identification Number (DIN): ")

print("What information do you want to receive on the Drug?")

code = get_code()
while code == "error":
    print ("Please re-enter a valid code, or press q to quit")
    code = get_code()


    codes = ["DIF", "CIF", "AI", "DFM", "PTY", "PST", "ROA", "DSC", "DST", "TCL"]


print("")
url = url_builder(code, id)

if stats(url):
    json_data = json_response(url)
    dict = json_data.items()
    for key, value in json_data.items():
        if value == "":
            value = "no information found"
        print(f"{key}: {value}")
else:
    print("Error: Code Not found")













