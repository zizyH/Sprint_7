import allure
import requests

from helpers import get_order_by_track
from urls import BASE_URL, ORDERS_TRACK


@allure.feature("Получение заказа по номеру")
class TestGetOrderByTrack:

    @allure.title("Получение заказа по track возвращает 200 и объект order")
    def test_get_order_by_track_valid_track_returns_200_and_order(self, order):
        response = get_order_by_track(order["track"])

        assert response.status_code == 200
        body = response.json()
        assert "order" in body
        assert body["order"]["track"] == order["track"]

    @allure.title("Получение заказа без параметра t возвращает 400")
    def test_get_order_by_track_without_t_returns_400(self):
        response = requests.get(f"{BASE_URL}{ORDERS_TRACK}")

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Получение заказа с несуществующим track возвращает 404")
    def test_get_order_by_track_nonexistent_track_returns_404(self):
        response = get_order_by_track(999999999)

        assert response.status_code == 404
        assert response.json()["message"] == "Заказ не найден"