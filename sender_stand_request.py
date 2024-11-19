import configuration
import requests
import data
from data import orders_body


def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_ORDER,
                         json=body,
                         headers=data.headers)
response = post_new_orders(data.orders_body)

def get_track_number(new_orders_response):
    track_number = new_orders_response.json()['track']
    return track_number

def get_order_by_track_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "?t=" + str(track_number),
                         headers=data.headers)


