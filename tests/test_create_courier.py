import allure

from helpers import build_courier_payload, create_courier


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Создание курьера со всеми полями возвращает 201 и ok=true")
    def test_create_courier_all_fields_returns_201_and_ok_true(self):
        payload = build_courier_payload()
        response = create_courier(payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров — возвращается 409")
    def test_create_courier_duplicate_login_returns_409(self, courier):
        duplicate_payload = build_courier_payload(login=courier["login"])
        response = create_courier(duplicate_payload)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Создание курьера без логина возвращает 400")
    def test_create_courier_without_login_returns_400(self):
        payload = build_courier_payload()
        payload.pop("login")
        response = create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Создание курьера без пароля возвращает 400")
    def test_create_courier_without_password_returns_400(self):
        payload = build_courier_payload()
        payload.pop("password")
        response = create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"