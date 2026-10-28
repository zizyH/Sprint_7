import allure

from helpers import build_courier_payload, build_order_payload, create_courier, create_order
from urls import BASE_URL, ORDERS_LIST
import requests


@allure.feature("Список заказов")
class TestOrderList:

    @allure.title("Получение списка заказов возвращает 200 и список orders")
    def test_get_orders_list_returns_200_and_orders(self):
        response = requests.get(f"{BASE_URL}{ORDERS_LIST}")

        assert response.status_code == 200
        body = response.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)

    @allure.title("Список заказов по несуществующему courierId возвращает 404")
    def test_get_orders_list_nonexistent_courier_returns_404(self):
        response = requests.get(f"{BASE_URL}{ORDERS_LIST}", params={"courierId": 999999999})

        assert response.status_code == 404
        assert "не найден" in response.json()["message"]