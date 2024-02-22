# API testing for simple book

The scope of this project is to use all API knowledge gained throught the Software Testing course and apply them in practice, using a live application.

Application under test:This application provides functionalities for managing books, making reservations, and handling orders through a RESTful API. Authentication is required for operations that involve modifying data,for more details click on this [link](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md).

Tools used:Python,pytest

versions used:
- requests 2.31.0
- pytest 8.0.1
- pytest-html 4.1.1

## How the token was created
To submit or view an order, you need to register your API client.

POST `/api-clients/`

The request body needs to be in JSON format and include the following properties:

 - `clientName` - String
 - `clientEmail` - String

 Example

 ```
 {
    "clientName": "Postman",
    "clientEmail": "valentin@example.com"
}
 ```

The response body will contain the access token. The access token is valid for 7 days.

In python :
![Screenhot code python ](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Screenshots/Token.png)

I have written two Python functions that interact with an API called "Simple Books API," which manages clients and authentication. Here's an explanation of the code:

Function get_token:

This function is designed to obtain an access token from the API.
It constructs a dictionary body containing client information, such as the name and a randomly generated email address.
Then, it sends a POST request to the endpoint "https://simple-books-api.glitch.me/api-clients" with the client data in JSON format.
The response is then parsed, and the access token is extracted from it.

Function login:

This function is intended for authenticating a client within the API.
It receives the client's name and email address.
It constructs a dictionary body with the client's information.
It sends a POST request to the same endpoint "https://simple-books-api.glitch.me/api-clients" with the client's data in JSON format.


**Possible errors**

Status code 409 - "API client already registered." Try changing the values for `clientEmail` and `clientName` to something else.

## Types available for testing

HTTP methods supported by this API are GET, POST, PATCH, and DELETE. In this section, you can explore and perform tests on various types of operations supported by the  Simple Book. Some examples include:

- **GET Requests:**
   Retrieve a list of books;
   Get detailed information about a specific book (replace :bookId with the actual book ID);
   View all orders (requires authentication);
   View details of a specific order (replace :orderId with the actual order ID, requires authentication);
- **POST Requests:**
   Submit a new order (requires authentication);
   Register a new API client;
- **PATCH Requests:** Update an existing order (replace :orderId with the actual order ID, requires authentication);
- **DELETE Requests:** Delete an existing order (replace :orderId with the actual order ID, requires authentication);


#### I send responses to some endpoints:
- `https://simple-books-api.glitch.me/status` (for status)
- `https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}` (returns all books by limit and type)
- `https://simple-books-api.glitch.me/books/{book_id}` (returns one book by id)
- `https://simple-books-api.glitch.me/api-clients` (Get token)
- `https://simple-books-api.glitch.me/orders` (submit an order)
- `https://simple-books-api.glitch.me/orders/{order_id}` (get an order by id)
- Using all available HTTP methods.
- The expected HTTP responses are received together with the HTTP messages following the requests (200, 201, 204,404 and 401).
  Here you can find the list of [Test conditions](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Test%20conditions.xlsx).


