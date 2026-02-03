import requests
from config import HEADERS


def test_honeypot_endpoint(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        return {
            "status_code": response.status_code,
            "response_body": response.text
        }

    except requests.exceptions.ConnectionError:
        return {"error": "Endpoint not reachable"}
    except requests.exceptions.Timeout:
        return {"error": "Request timeout"}
