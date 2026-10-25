import allure

from helpers import build_courier_payload, login_courier


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешный логин возвращает 200 и id")
    def test_login_courier_valid_credentials_returns_200_and_id(self, courier):
        response = login_courier(courier["login"], courier["password"])

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин без пароля возвращает 400")
    def test_login_courier_without_password_returns_400(self, courier):
        response = login_courier(courier["login"], "")

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Логин без логина возвращает 400")
    def test_login_courier_without_login_returns_400(self, courier):
        response = login_courier("", courier["password"])

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Логин с неверным паролем возвращает 404")
    def test_login_courier_wrong_password_returns_404(self, courier):
        response = login_courier(courier["login"], "wrong_password")

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Логин под несуществующим пользователем возвращает 404")
    def test_login_courier_nonexistent_user_returns_404(self):
        payload = build_courier_payload()
        response = login_courier(payload["login"], payload["password"])

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"