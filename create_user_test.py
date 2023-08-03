# Микулов Никита, 7-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import sender_stand_request
import data

def get_order_by_track(track):
    url = configuration.URL_SERVICE + configuration.TRACK_PATH + "?t=" + str(track)
    response = requests.get(url)
    assert response.status_code == 200
    return response.json()
def test_get_order_by_track():
    response = sender_stand_request.create_order(data.order)
    if response.status_code == 201:
        print("Ваш заказ:", data.order)
    else:
        print("Недостаточно данных для поиска. Код ошибки:", response.status_code)
test_get_order_by_track()