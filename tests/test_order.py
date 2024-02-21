import requests

from api_requests import request_orders
from utils.constants import *


class TestOrder:

    def test_submit_order(self):
        response = request_orders.submit_order(BOOK_ID_1_QUERY_PARAMETER,CUSTOMER_NAME_QUERY_PARAMETER)
        assert response.json()['created'] == True
        assert 'orderId' in response.json().keys()

        # clean up
        request_orders.delete_order(response.json()['orderId'])

    def test_submit_incorrect_order(self):
        response = request_orders.submit_order(30, "Jhon")
        assert response.json()['error'] == 'Invalid or missing bookId.', (f"Actual: {response.json()}, Expected: "
                                                                          f"error: Invalid or missing bookId.")

    def test_submit_order_when_we_are_not_using_any_token(self):
        response = request_orders.submit_order_without_token()
        assert response.status_code == 401, f'Actual:{response.status_code},Expected:401'
        assert response.json()['error'] == 'Missing Authorization header.', (f"Actual: {response.json()}, Expected: "
                                                                             f"error: Missing Authorization header.")

    def test_get_an_order_by_valid_id(self):
        response_submit = request_orders.submit_order(BOOK_ID_5_QUERY_PARAMETER, CUSTOMER_NAME_QUERY_PARAMETER).json()['orderId']
        response_order_id = request_orders.get_order(response_submit)
        assert response_order_id.status_code == 200, f'Actual:{response_order_id.status_code},Expected:200'
        assert response_order_id.json()[
                   'customerName'] == CUSTOMER_NAME_QUERY_PARAMETER, f"Actual:{response_order_id.json()},Expected:customerName={CUSTOMER_NAME_QUERY_PARAMETER}"
        assert response_order_id.json()['bookId'] == BOOK_ID_5_QUERY_PARAMETER
        assert response_order_id.json()['customerName'] == CUSTOMER_NAME_QUERY_PARAMETER

        # clean up
        request_orders.delete_order(response_submit)

    def test_get_all_orders(self):
        order_1 = request_orders.submit_order(BOOK_ID_5_QUERY_PARAMETER,CUSTOMER_NAME_QUERY_PARAMETER)
        order_2 = request_orders.submit_order(BOOK_ID_6_QUERY_PARAMETER,CUSTOMER_NAME_2_QUERY_PARAMETER)
        response = request_orders.get_all_orders()
        assert len(response.json()) == 2
        assert order_1.json()['orderId'] in response.json()[0].values() or order_1.json()['orderId'] in response.json()[
            1].values()
        assert order_2.json()['orderId'] in response.json()[0].values() or order_2.json()['orderId'] in response.json()[
            1].values()

        # clean up
        request_orders.delete_order(order_1.json()['orderId'])
        request_orders.delete_order(order_2.json()['orderId'])

    def test_update_order(self):
        order_id = request_orders.submit_order(BOOK_ID_5_QUERY_PARAMETER, CUSTOMER_NAME_QUERY_PARAMETER).json()['orderId']
        response = request_orders.update_order(order_id, NEW_CUSTOMER_NAME_QUERT_PARAMETER)
        assert response.status_code == 204
        new_order_response = request_orders.get_order(order_id)
        assert new_order_response.json()['customerName'] == NEW_CUSTOMER_NAME_QUERT_PARAMETER

        # clean up
        request_orders.delete_order(order_id)

    def test_delete_order(self):
        order_id = request_orders.submit_order(BOOK_ID_5_QUERY_PARAMETER, CUSTOMER_NAME_2_QUERY_PARAMETER).json()['orderId']
        response = request_orders.delete_order(order_id)
        assert response.status_code == 204
        get_order_response = request_orders.get_order(order_id)
        assert get_order_response.status_code == 404
        assert get_order_response.json()[
                   'error'] == f'No order with id {order_id}.', f"Actual:{get_order_response.json()['error']}, expected:No order with id {order_id}"

    def test_submit_order_that_is_not_in_stock(self):
        order_1 = request_orders.submit_order(BOOK_ID_2_QUERY_PARAMETER, CUSTOMER_NAME_QUERY_PARAMETER)
        assert order_1.status_code == 404, f'Actual:{order_1.status_code},Expected:404'
        assert order_1.json()['error'] == 'This book is not in stock. Try again later.' ,f"Actual:{order_1.json()['error']}, expected:This book is not in stock. Try again later."


    def test_update_order_without_complete_body(self):
        order_id = request_orders.submit_order(BOOK_ID_5_QUERY_PARAMETER, CUSTOMER_NAME_QUERY_PARAMETER).json()['orderId']
        response = request_orders.update_order_without_body(order_id)
        assert response.status_code == 204, f'Actual:{response.status_code},Expected:204'
        new_order_response = request_orders.get_order(order_id)
        assert new_order_response.json()['customerName'] == CUSTOMER_NAME_QUERY_PARAMETER ,f'Actual:{new_order_response.json()['customerName']},expected:CustomerName:{CUSTOMER_NAME_QUERY_PARAMETER}'

        # clean up
        request_orders.delete_order(order_id)

    def test_get_an_order_by_invalid_id(self):
        order_id = request_orders.submit_order(BOOK_ID_5_QUERY_PARAMETER, CUSTOMER_NAME_QUERY_PARAMETER).json()['orderId']
        response_order_id = request_orders.get_order(order_id + 'BSF')
        assert response_order_id.status_code == 404, f'Actual:{response_order_id.status_code},Expected:404'
        assert response_order_id.json()['error'] == f'No order with id {order_id + 'BSF'}.'

        #clean up
        request_orders.delete_order(order_id)

    def test_submit_an_order_without_add_customername(self):
        response = request_orders.submit_oder_without_customername(BOOK_ID_1_QUERY_PARAMETER)
        assert response.status_code == 400 ,f'actual:{response.status_code}'
        #clean up
        request_orders.delete_order(response.json()['orderId'])

    def test_submit_an_order_without_add_bookId(self):
        response = request_orders.submit_order_without_bookId(CUSTOMER_NAME_2_QUERY_PARAMETER)
        assert response.status_code == 400, f'actual:{response.status_code}'
        assert response.json()['error'] == 'Invalid or missing bookId.' ,f'Actual:{response.json()['error']},expected:Invalid or missing bookId.'
       




