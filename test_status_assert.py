#Елена Губарева 23 когорта диплом инженер по тестированию +
import sender_stand_request
import data


def test_status_200():
    track_number = sender_stand_request.get_track_number(sender_stand_request.post_new_orders(data.orders_body))
    response = sender_stand_request.get_order_by_track_number(track_number)
    assert response.status_code == 200