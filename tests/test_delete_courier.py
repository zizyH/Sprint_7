import allure
import requests

from helpers import delete_courier
from urls import BASE_URL


@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Успешное удаление курьера возвращает 200 и ok=true")
    def test_delete_courier_valid_id_returns_200_and_ok_true(self, courier):
        response = delete_courier(courier["id"])

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Удаление курьера без id возвращает 404")
    def test_delete_courier_without_id_returns_404(self):
        response = requests.delete(f"{BASE_URL}/api/v1/courier/")

        assert response.status_code == 404

    @allure.title("Удаление курьера с несуществующим id возвращает 404")
    def test_delete_courier_nonexistent_id_returns_404(self):
        response = delete_courier(999999999)

        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id нет."