import pytest
import requests

from helpers import (
    build_courier_payload,
    create_courier,
    delete_courier,
    get_courier_id,
    build_order_payload,
    create_order,
    get_order_by_track,
)
from urls import BASE_URL, ORDERS_CANCEL


@pytest.fixture
def cleanup_courier():
    
    couriers_to_delete = []

    def _add_to_cleanup(login, password):
        courier_id = get_courier_id(login, password)
        if courier_id:
            couriers_to_delete.append(courier_id)

    yield _add_to_cleanup

    # Выполняется после теста
    for courier_id in couriers_to_delete:
        delete_courier(courier_id)


@pytest.fixture
def courier():
    
    payload = build_courier_payload()
    response = create_courier(payload)
    
    if response.status_code != 201:
        raise Exception(f"Не удалось создать курьера для фикстуры: {response.text}")

    courier_id = get_courier_id(payload["login"], payload["password"])
    yield {"login": payload["login"], "password": payload["password"], "id": courier_id}

    delete_courier(courier_id)


@pytest.fixture
def order():
    
    payload = build_order_payload()
    response = create_order(payload)
    
    if response.status_code != 201:
        raise Exception(f"Не удалось создать заказ для фикстуры: {response.text}")
        
    track = response.json()["track"]

    order_id = get_order_by_track(track).json()["order"]["id"]

    yield {"track": track, "id": order_id}

    
    requests.put(f"{BASE_URL}{ORDERS_CANCEL}", json={"track": track})