import requests
import pytest

url = 'https://reqres.in/api/users'
data = {
    "name": "morpheus",
    "job": "leader"
}


def test_create_user_with_correct_data():
    response = requests.post(url, json=data)
    assert response.status_code == 201


def test_create_user_with_incomplete_data():
    incomplete_data = {"name": "morpheus"}
    response = requests.post(url, json=incomplete_data)
    assert response.status_code == 400


def test_create_user_with_invalid_data():
    invalid_data = {"name": "morpheus", "job": 123}
    response = requests.post(url, json=invalid_data)
    assert response.status_code == 400


def test_create_user_with_empty_request_body():
    response = requests.post(url, json={})
    assert response.status_code == 400


def test_create_user_with_invalid_endpoint():
    invalid_url = 'https://reqres.in/api/users/123'
    response = requests.post(invalid_url, json=data)
    assert response.status_code == 404