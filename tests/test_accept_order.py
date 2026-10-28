import allure
import requests

from urls import BASE_URL, ORDERS_ACCEPT


@allure.feature("Принятие заказа")
class TestAcceptOrder:

    @allure.title("Успешное принятие заказа возвращает 200 и ok=true")
    def test_accept_order_valid_ids_returns_200_and_ok_true(self, courier, order):
        url = f"{BASE_URL}{ORDERS_ACCEPT.format(order_id=order['id'])}"
        response = requests.put(url, params={"courierId": courier["id"]})

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Принятие заказа без courierId возвращает 400")
    def test_accept_order_without_courier_id_returns_400(self, order):
        url = f"{BASE_URL}{ORDERS_ACCEPT.format(order_id=order['id'])}"
        response = requests.put(url)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Принятие заказа с неверным courierId возвращает 404")
    def test_accept_order_invalid_courier_id_returns_404(self, order):
        url = f"{BASE_URL}{ORDERS_ACCEPT.format(order_id=order['id'])}"
        response = requests.put(url, params={"courierId": 999999999})

        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id не существует"

    @allure.title("Принятие заказа без id заказа возвращает 404")
    def test_accept_order_without_order_id_returns_404(self, courier):
        response = requests.put(
            f"{BASE_URL}/api/v1/orders/accept/",
            params={"courierId": courier["id"]},
        )

        assert response.status_code == 404

    @allure.title("Принятие заказа с неверным id заказа возвращает 404")
    def test_accept_order_invalid_order_id_returns_404(self, courier):
        url = f"{BASE_URL}{ORDERS_ACCEPT.format(order_id=999999999)}"
        response = requests.put(url, params={"courierId": courier["id"]})

        assert response.status_code == 404
        assert response.json()["message"] == "Заказа с таким id не существует"