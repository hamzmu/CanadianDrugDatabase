import requests


def url_builder(code: str, id: str) -> str:
    code_dict = {
        "DIF": "drugproduct",
        "CIF": "company",
        "AIN": "activeingredient",
        "DFM": "form",
        "PTY": "packaging",
        "PST": "pharmaceuticalstd",
        "ROA": "route",
        "DSC": "schedule",
        "DST": "status",
        "TCL": "therapeuticclass"
    }

    base = 'https://health-products.canada.ca'
    url = base + '/api/drug/' + code_dict[code] + '/?lang=en&id=' + id
    return url

def stats(url: str) -> bool:
    if requests.get(url).status_code == 200:
        return True
    return False

def json_response(url: str) -> str:
    json_raw_data = requests.get(url).json()
    if isinstance(json_raw_data, list):
        return json_raw_data[0]
    return json_raw_data




