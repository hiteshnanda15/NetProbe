import time
import requests


def check_http(url):

    try:

        start_time = time.perf_counter()

        response = requests.get(
            url,
            timeout=5
        )

        end_time = time.perf_counter()

        response_time = (end_time - start_time) * 1000

        return {
            "status": "UP",
            "http_status": response.status_code,
            "response_time": round(response_time, 2),
            "error": None
        }

    except requests.exceptions.Timeout:

        return {
            "status": "DOWN",
            "http_status": None,
            "response_time": None,
            "error": "Request timed out"
        }

    except requests.exceptions.ConnectionError:

        return {
            "status": "DOWN",
            "http_status": None,
            "response_time": None,
            "error": "Connection failed"
        }

    except requests.exceptions.RequestException as error:

        return {
            "status": "DOWN",
            "http_status": None,
            "response_time": None,
            "error": str(error)
        }