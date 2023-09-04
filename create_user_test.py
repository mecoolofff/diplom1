# Микулов Никита Финальный проект
import sender_stand_request
import data
def test_get_order_by_track():
    response = sender_stand_request.create_order(data.order)
    assert response.status_code == 201, f"Не удалось создать заказ. Код ошибки: {response.status_code}"
    order_track = response.json()
    track = order_track.get('track')
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200, f"Ошибка при получении заказа по трек-номеру. Код ошибки: {get_response.status_code}"
