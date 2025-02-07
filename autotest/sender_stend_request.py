# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import envirement
# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

def create_order(order_body):
    # Создание заказа
    response_create = requests.post(envirement.URL_ORDERS,
                                    json=order_body)
    return response_create


def get_order(track):
    # Получение информации о заказе по номеру трека
    url = envirement.URL_TRACK + str(track)
    response_get = requests.get(url)
    return response_get