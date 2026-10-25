import pytest

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

import requests


@pytest.fixture
def courier():
    """Создаёт уникального курьера, отдаёт dict с login/password/id, удаляет после теста."""
    payload = build_courier_payload()
    response = create_courier(payload)
    assert response.status_code == 201, f"Не удалось создать курьера: {response.text}"

    courier_id = get_courier_id(payload["login"], payload["password"])
    yield {"login": payload["login"], "password": payload["password"], "id": courier_id}

    delete_courier(courier_id)


@pytest.fixture
def order():
    """Создаёт заказ, отдаёт track и id, после теста отменяет его."""
    payload = build_order_payload()
    response = create_order(payload)
    assert response.status_code == 201, f"Не удалось создать заказ: {response.text}"
    track = response.json()["track"]

    order_id = get_order_by_track(track).json()["order"]["id"]

    yield {"track": track, "id": order_id}

    
    requests.put(f"{BASE_URL}{ORDERS_CANCEL}", json={"track": track})