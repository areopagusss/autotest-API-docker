import pytest
import requests
import logging

BASE_URL = "https://reqres.in/api/users"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def setup_module():
    logging.info("Setting up the test module")


@pytest.fixture
def teardown_module():
    logging.info("Tearing down the test module")


@pytest.mark.parametrize("user_id, expected_status", [(2, 200), (23, 404)])
def test_get_user(base_url, user_id, expected_status):
    response = requests.get(f"{base_url}/{user_id}")
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json()["data"]["id"] == user_id
    else:
        assert response.json() == {}
    log_request_response(response)


def test_create_user(base_url):
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(base_url, json=payload)
    assert_request_success(response, 201, payload)


def test_update_user(base_url):
    user_id = 2
    payload = {"name": "morpheus", "job": "zion resident"}
    response = requests.put(f"{base_url}/{user_id}", json=payload)
    assert_request_success(response, 200, payload)


def assert_request_success(response, expected_status, payload=None):
    assert response.status_code == expected_status
    if payload:
        for key, value in payload.items():
            assert response.json()[key] == value
    log_request_response(response)


def log_request_response(response):
    logging.debug("Request URL: %s", response.request.url)
    logging.debug("Request Method: %s", response.request.method)
    logging.debug("Request Headers: %s", response.request.headers)
    logging.debug("Request Body: %s", response.request.body)
    logging.debug("Response Status Code: %s", response.status_code)
    logging.debug("Response Headers: %s", response.headers)
    logging.debug("Response Body: %s", response.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    pytest.main()