import allure
import pytest

from helpers import build_order_payload, create_order


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с цветом {colors} возвращает 201 и track")
    @pytest.mark.parametrize(
        "colors",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            [],
        ],
        ids=["black", "grey", "both", "no_color"],
    )
    def test_create_order_with_colors_returns_201_and_track(self, colors):
        payload = build_order_payload(color=colors)
        response = create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()