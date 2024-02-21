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

