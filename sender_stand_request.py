import configuration
import requests
import data

def create_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.ORDER_PATH,
                             json=body,
                             headers=data.headers)
    return response
def get_order_by_track(track):
    url = configuration.URL_SERVICE + configuration.TRACK_PATH + "?t=" + str(track)
    response = requests.get(url)
    return response