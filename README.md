# API testing for simple book

The scope of this project is to use all API knowledge gained throught the Software Testing course and apply them in practice, using a live application.

Application under test:This application provides functionalities for managing books, making reservations, and handling orders through a RESTful API. Authentication is required for operations that involve modifying data,for more details click on this [link](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md).

Tools used:Python,pytest

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
