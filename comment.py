#Была еще попытка сделать вот так, но программа в таком случае ругается на строку assert order_response.get('track') == str(track)
#Идеи как сделать рабочий код закончились( не понимаю в чем ошибка, уже запутался в присваиваниях, мб что-то не то присваиваю..
#Не понимаю вроде же правильно путь указываю: configuration.URL_SERVICE + configuration.TRACK_PATH + "?t=" + str(track) с методом get, но почему-то идет ошибка при вводе
#assert order_response.get('track') == configuration.URL_SERVICE + configuration.TRACK_PATH + "?t=" + str(track)

#import configuration
#import requests
#import sender_stand_request
#import data

#def get_order_by_track(track):
#url = configuration.URL_SERVICE + configuration.TRACK_PATH + "?t=" + str(track)
#response = requests.get(url)
#assert response.status_code == 200
#return response.json()

#def test_get_order_by_track():
#response = sender_stand_request.create_order(data.order)
#if response.status_code == 201:
#order_track = response.json()
#track = order_track.get('track')
#order_response = get_order_by_track(track)
#assert order_response.get('track') == str(track)
#print("Тест успешно пройден. Трек номер заказа:", track)
#else:
#print("Не удалось создать заказ. Код ошибки:", response.status_code)

#test_get_order_by_track()