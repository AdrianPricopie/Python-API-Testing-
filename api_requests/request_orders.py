import requests
from api_requests import request_api_clients

token = request_api_clients.get_token()
headers = {
    "Authorization": f"Bearer {token}"
}



def submit_order(book_id, customer_name):
    body = {
        "bookId": book_id,
        "customerName": customer_name
    }

    return requests.post("https://simple-books-api.glitch.me/orders", json=body, headers=headers)

def submit_oder_without_customername(book_id):
    body = {
        "bookId": book_id
    }
    return requests.post("https://simple-books-api.glitch.me/orders", json=body, headers=headers)

def submit_order_without_bookId(customer_name):
    body = {
        "customerName": customer_name
    }

    return requests.post("https://simple-books-api.glitch.me/orders", json=body, headers=headers)

def get_all_orders():
    return  requests.get('https://simple-books-api.glitch.me/orders',headers=headers)

def get_order(order_id):
    return requests.get(f'https://simple-books-api.glitch.me/orders/{order_id}',headers=headers)


def submit_order_without_token():
    return requests.post("https://simple-books-api.glitch.me/orders")


def update_order(order_id,new_customer_name):
    body={
        "customerName":new_customer_name
    }
    return  requests.patch(f"https://simple-books-api.glitch.me/orders/{order_id}",headers=headers,json=body)

def update_order_without_body(order_id):
    return requests.patch(f"https://simple-books-api.glitch.me/orders/{order_id}",headers=headers)

def delete_order(order_id):
    return requests.delete(f"https://simple-books-api.glitch.me/orders/{order_id}", headers=headers)
