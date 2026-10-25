BASE_URL = "https://qa-scooter.education-services.ru"

COURIER_CREATE = "/api/v1/courier"
COURIER_LOGIN = "/api/v1/courier/login"
COURIER_DELETE = "/api/v1/courier/{courier_id}"
COURIER_ORDERS_COUNT = "/api/v1/courier/{courier_id}/ordersCount"

ORDERS_CREATE = "/api/v1/orders"
ORDERS_LIST = "/api/v1/orders"
ORDERS_ACCEPT = "/api/v1/orders/accept/{order_id}"
ORDERS_TRACK = "/api/v1/orders/track"
ORDERS_FINISH = "/api/v1/orders/finish/{order_id}"
ORDERS_CANCEL = "/api/v1/orders/cancel"