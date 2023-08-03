import configuration
import requests
import data

def create_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.ORDER_PATH,
                             json=body,
                             headers=data.headers)
    return response

response = create_order(data.order)

if response.status_code == 201:
    order_track = response.json()
    track = order_track.get('track')
    print("Заказ успешно создан. Трек номер:", track)
else:
    print("Не удалось создать заказ. Код ошибки:", response.status_code)