import random
import string

import requests

from urls import (
    BASE_URL,
    COURIER_CREATE,
    COURIER_LOGIN,
    COURIER_DELETE,
    ORDERS_CREATE,
    ORDERS_TRACK,
)


def generate_random_string(length: int = 10) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def build_courier_payload(login=None, password=None, first_name=None) -> dict:
    return {
        "login": login or generate_random_string(),
        "password": password or generate_random_string(),
        "firstName": first_name or generate_random_string(),
    }


def build_order_payload(**overrides) -> dict:
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-01-01",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"],
    }
    payload.update(overrides)
    return payload


def register_new_courier_and_return_login_password():
    """Возвращает [login, password, firstName] или [] при ошибке (как в задании)."""
    payload = build_courier_payload()
    response = requests.post(f"{BASE_URL}{COURIER_CREATE}", data=payload)
    if response.status_code == 201:
        return [payload["login"], payload["password"], payload["firstName"]]
    return []


def create_courier(payload: dict) -> requests.Response:
    return requests.post(f"{BASE_URL}{COURIER_CREATE}", data=payload)


def login_courier(login: str, password: str) -> requests.Response:
    return requests.post(
        f"{BASE_URL}{COURIER_LOGIN}",
        data={"login": login, "password": password},
    )


def get_courier_id(login: str, password: str):
    response = login_courier(login, password)
    if response.status_code == 200:
        return response.json().get("id")
    return None


def delete_courier(courier_id) -> requests.Response:
    return requests.delete(f"{BASE_URL}{COURIER_DELETE.format(courier_id=courier_id)}")


def create_order(payload: dict) -> requests.Response:
    return requests.post(f"{BASE_URL}{ORDERS_CREATE}", json=payload)


def get_order_by_track(track) -> requests.Response:
    return requests.get(f"{BASE_URL}{ORDERS_TRACK}", params={"t": track})