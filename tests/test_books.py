from api_requests import request_books
from utils.constants import *


class TestBooks:

    def test_get_all_books(self):
        response = request_books.get_all_books()
        assert response.status_code == OK_RESPONSE, f"Actual: {response.status_code}, Expected: 200"
        assert len(response.json()) == 6
        for book in response.json():
            assert "id" in book.keys()
            assert "name" in book.keys()
            assert "type" in book.keys()
            assert "available" in book.keys()

    def test_get_all_fiction_books(self):
        response = request_books.get_all_books(FICTION_QUERY_PARAMETER)
        assert response.status_code == 200, f"Actual: {response.status_code}, Expected: 200"
        for book in response.json():
            assert book["type"] == "fiction", f"Actual: {book['type']}, Expected: fiction"

    def test_get_all_non_fiction_books(self):
        response = request_books.get_all_books("non-fiction")
        assert response.status_code == 200, f"Actual: {response.status_code}, Expected: 200"
        for book in response.json():
            assert book["type"] == "non-fiction", f"Actual: {book['type']}, Expected: non-fiction"

    def test_limit_books_query(self):
        response = request_books.get_all_books(limit=3)
        assert response.status_code == 200, f"Actual: {response.status_code}, Expected: 200"
        assert len(response.json()) <= 3, f"Actual: number of objects: {response.json()}, Expected: number of objects: <=3"

    def test_get_book(self):
        response = request_books.get_book(1)
        assert response.status_code == 200, f"Actual: {response.status_code}, Expected: 200"
        assert response.json()["id"] == 1

    #
    def test_get_all_book_with_wrong_type_books(self):
        response = request_books.get_all_books(WRONG_BOOK_TYPE_PARAMETER)
        assert response.status_code == 400, f"Actual: {response.status_code}, Expected: 400"
        assert response.json()['error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", f"Actual:{response.status_code},Expected:Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."


    def test_get_all_book_with_hight_limit_books(self):
        response = request_books.get_all_books(limit=21)
        assert response.status_code == 400, f"Actual: {response.status_code}, Expected: 400"
        assert response.json()['error'] == "Invalid value for query parameter 'limit'. Cannot be greater than 20.", f"Actual:{response.status_code},Expected:Invalid value for query parameter 'limit'. Cannot be greater than 20."


    def test_get_book_that_is_not_exist(self):

        response = request_books.get_book(BOOK_ID_THAT_IS_NOT_EXIST_QUERY_PARAMETER)
        assert response.status_code == 404, f"Actual: {response.status_code}, Expected: 404"
        assert response.json()['error'] == f"No book with id {BOOK_ID_THAT_IS_NOT_EXIST_QUERY_PARAMETER}", (f"Actual: {response.json()}, Expected: "
                                                                          f"error: No book with id {BOOK_ID_THAT_IS_NOT_EXIST_QUERY_PARAMETER} ")


    def test_get_book_with_negativ_limit(self):

        response = request_books.get_all_books(limit=-1)
        assert response.status_code == 400,  f"Actual: {response.status_code}, Expected: 400"
        assert response.json()['error'] == "Invalid value for query parameter 'limit'. Must be greater than 0.", (f"Actual: {response.json()}, Expected:"
                                                                          f"error: Invalid value for query parameter 'limit'. Must be greater than 0.")


    def test_get_book_with_valid_limit_and_type(self):

        response = request_books.get_all_books(limit=2,book_type="fiction")
        assert response.status_code == 200 ,  f"Actual: {response.status_code}, Expected: 200"
        assert len(response.json()) <= 2
        for book in response.json():
            assert book["type"] == "fiction", f"Actual: {book['type']}, Expected:fiction"











