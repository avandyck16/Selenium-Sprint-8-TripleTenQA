import requests
import data
import json
from selenium import webdriver

def get_phone_code() -> str:
    api_request = requests.get(
        f'{data.urban_routes_url}/api/v1/number?number={data.phone_number}'
    ).json()["code"]
    print("get_phone_number_code")
    return api_request


