# API testing for simple book with pytest

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
 ![Screenhot code python ](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Screenshots/request%20books.png)
 
get_all_books(book_type="", limit=""): This function makes a GET request to a books API at a specific endpoint (https://simple-books-api.glitch.me/books). It accepts two optional parameters: book_type and limit. These parameters are used to filter the results based on the book type and limit the results to a certain number. The function returns the HTTP response received from the API.

get_book(book_id): This function makes a GET request to the same API but to a specific endpoint to retrieve details about a particular book. The parameter book_id is used to specify which book to request. The function also returns the HTTP response received from the API.

 ![Screenhot code python ](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Screenshots/request%20order%20%234.png)

 def submit_order_without_bookId(customer_name):

This function submits an order without specifying a bookId.
Constructs the request body with the provided customer_name.
Uses requests.post() to make a POST request to the "https://simple-books-api.glitch.me/orders" endpoint, including the JSON body and the authorization headers.

def get_all_orders():

This function retrieves all orders from the API.
Uses requests.get() to make a GET request to the "https://simple-books-api.glitch.me/orders" endpoint, including the authorization headers.

def get_order(order_id):

This function retrieves the details of a specific order identified by order_id from the API.
Uses requests.get() to make a GET request to the "https://simple-books-api.glitch.me/orders/{order_id}" endpoint, including the authorization headers.



  
- `https://simple-books-api.glitch.me/books/{book_id}` (returns one book by id)
- `https://simple-books-api.glitch.me/api-clients` (Get token)
- `https://simple-books-api.glitch.me/orders` (submit an order/get all orders/delete orders with correct body)
- `https://simple-books-api.glitch.me/orders/{order_id}` (get an order by id)

 ![Screenhot code python ](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Screenshots/request%20order%20%231.png)

'update_order(order_id, new_customer_name):

This function is designed to update the details of an existing order.
It takes two parameters: order_id identifies the order to be updated, and new_customer_name represents the new customer name.
Constructs the request body with the new customer name.
Uses the requests.patch() method to make a PATCH request to the specific endpoint of the order with order_id, including the authorization header and the updated request body.

update_order_without_body(order_id):

This function is intended for an update but does not include a request body.
Takes a single parameter, order_id, to identify the order to be updated.
Uses the requests.patch() method to make a PATCH request to the specific endpoint of the order with order_id, including the authorization header. It does not include a request body.

delete_order(order_id):

This function is designed to delete an existing order.
Takes a single parameter, order_id, to identify the order to be deleted.
Uses the requests.delete() method to make a DELETE request to the specific endpoint of the order with order_id, including the authorization header.

  

 ![Screenhot code python ](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Screenshots/request%20order%20%232.png)

The code begins with necessary imports, including the requests library for managing HTTP requests and the request_api_clients module, which houses functions designed for handling requests to APIs. The process of obtaining an authentication token involves the use of a function from request_api_clients.
Following this, the headers are configured by defining an authorization header using the acquired authentication token. This header is crucial for ensuring secure and authorized communication with the API.
The core functionality is encapsulated in the submit_order function, which initiates the process of sending a book order to the API. The function meticulously constructs the request body by incorporating the book_id and customer_name parameters. Finally, the requests.post() method is employed to execute a POST request to the specified endpoint, "https://simple-books-api.glitch.me/orders," and includes the authorization header for authentication. This comprehensive process ensures the submission of book orders to the designated API endpoint, facilitating seamless interaction with the underlying system

- `https://simple-books-api.glitch.me/api-clients` (Get token)
- Using all available HTTP methods.
- The expected HTTP responses are received together with the HTTP messages following the requests (200, 201, 204,404 and 401).
  Here you can find the list of [Test conditions](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Test%20conditions.xlsx).

# Test performed 

The 'utils' folder contains a subfolder with [global constants](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Test%20conditions.xlsx), which I have used as parameters for tests in the [test folder](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Test%20conditions.xlsx).

1.Verifiy that i can log in successful with valid credentials and  generates acces token

- HTTPS method for request:POST
- Test types / techniques used:Positive testing,blackbox testing;
- How I checked:response status is 201 and "accessToken" is present in the set of keys (keys()) of the JSON response received from the server.
- [Link to test_api_clients](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_api_clients.py).

2.Verify API Status Endpoint Returns 'OK' Status

- HTTPS method for request:GET
- Test types / techniques used:Positive testing,blackbox testing;
- How I checked:response status is 200 OK.
- [Link to test_status](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_status.py).

3.Verify Successful Retrieval of All Books

- HTTPS method for request:GET
- Test types / techniques used:Positive testing,blackbox testing;
- How I checked:response status is 200 OK,the length of the JSON response array is 6,For each book, it checks if certain keys ("id", "name", "type", "available") are present in the keys of the book's dictionary. If any of these keys is missing, the test will fail.
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

4.Verify Retrieval of All Fiction Books

- HTTPS method for request:GET
- Test types / techniques used:Positive testing,blackbox testing;
- How I checked:response status is 200 OK,Iterate through each book in the response and check if its type is "fiction"
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

5.Verify Retrieval of All Non-Fiction Books

- HTTPS method for request:GET
- Test types / techniques used:Positive testing,blackbox testing;
- How I checked:response status is 200 OK,Iterate through each book in the response and check if its type is "non-fiction"
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

6.Verify Limiting Number of Books in the Response

- HTTPS method for request:GET
- Test types / techniques used:Positive testing,blackbox testing;
- How I checked:response status is 200 OK, Send a request to get books with a limit of 3 using the get_all_books function and the number of books in the response is less than or equal to 3.
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

7.Verify Retrieval of a Specific Book

- HTTPS method for request:GET
- Test types / techniques used:Positive testing,blackbox testing;
- How I checked:response status is 200 OK,ID of the book in the response is 1.
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

8.Verify Handling of Invalid Book Type in Query

- HTTPS method for request:GET
- Test types / techniques used:Negative testing,blackbox testing;
- How I checked:response status is 400 bad request,Check if the error message in the response matches the expected error message.
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

9.Verify Handling of Excessive Limit in Query

- HTTPS method for request:GET
- Test types / techniques used:Negative testing,blackbox testing,boundary value 
- How I checked:response status is 400 bad request,Check if the error message in the response matches the expected error message.
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

10.Verify Handling of Non-Existent Book

- HTTPS method for request:GET
- Test types / techniques used:Negative testing,blackbox testing
- How I checked:response status is 400 bad request,It checks if the JSON response contains an 'error' key with a corresponding message. The error message should indicate that there is no book with the specified ID
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

11.Verify Handling of Negative Limit in Query

- HTTPS method for request:GET
- Test types / techniques used:Negative testing,blackbox testing,boundary value
- How I checked:response status is 400 bad request,It checks if the JSON response contains an 'error' key with a corresponding message. The error message should indicate that the provided limit value is invalid and must be greater than 0.
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

12.Verify Retrieval of Books with Valid Limit and Type

- HTTPS method for request:GET
- Test types / techniques used:Negative testing,blackbox testing
- How I checked:response status is 200 OK,It checks if the number of books in the response is less than or equal to 2. This ensures that the system respects the specified limit,It iterates through each book in the response and checks if the book type is "fiction". This ensures that all books in the response have the correct book type.
- [Link to test_books](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_books.py).

13.Verification of order submission

- HTTPS method for request:POST
- Test types / techniques used:Postive testing,blackbox testing
- How I checked:response status is 200 OK,Verify if the 'created' key in the JSON response is True,Verify if the 'orderId' key exists in the set of keys of the JSON response.
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

14.Verify Handling of Incorrect Order Submission

- HTTPS method for request:POST
- Test types / techniques used:Positive testing,blackbox testing
- How I checked:Make a request to submit an order with an incorrect book ID and a customer name
,Verify if the 'error' key in the JSON response contains the expected error message.
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

 15.Verify Order Submission Without Authorization Token

- HTTPS method for request:POST
- Test types / techniques used:Negative testing,blackbox testing
- How I checked:Make a request to submit an order without providing any authorization token,Verify if the response status code is 401 (Unauthorized),Verify if the 'error' key in the JSON response contains the expected error message.
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

16.Verify Retrieval of an Order by Valid ID

- HTTPS method for request:GET
- Test types / techniques used:Positive testing,blackbox testing
- How I checked:Submit an order to obtain a valid order ID,Make a request to get the order using the obtained order ID,Verify if the response status code is 200 (OK), Verify if the 'customerName' in the JSON response matches the expected customer name,Verify if the 'bookId' in the JSON response matches the expected book ID,Verify if the 'customerName' in the JSON response matches the expected customer name
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

17.Verify Retrieval of All Orders

- HTTPS method for request:GET
- Test types / techniques used:Positive testing,blackbox testing
- How I checked:Submit two orders to create some data,Make a request to get all orders,Verify if the number of orders in the response is 2,Verify if the order IDs of the submitted orders are present in the response
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

18.Verify Updating an Order

- HTTPS method for request:PATCH
- Test types / techniques used:Positive testing,blackbox testing
- How I checked: Submit an order to create some data and retrieve the order ID,Make . request to update the order with a new customer name,Verify if the response status code is 204 (No Content), indicating a successful update,Make a request to get the updated order,Verify if the customer name in the updated order matches the new customer name.
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

19.Verify Deletion of an Order

- HTTPS method for request:DELETE
- Test types / techniques used:Positive testing,blackbox testing
- How I checked:Submit an order to create some data and retrieve the order ID,Make a request to delete the order,Verify if the response status code is 204 (No Content), indicating a successful deletion,Make a request to get the deleted order,Verify if the response status code is 404 (Not Found),Verify if the 'error' key in the JSON response contains the expected error message
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

20.Verify Submission of an Order for an Out-of-Stock Book

- HTTPS method for request:POST
- Test types / techniques used:Negative testing,unit testing,blackbox testing
- How I checked:Submit an order for a specific book ID with a given customer name, Verify if the response status code is 404 ,Verify if the 'error' key in the JSON response contains the expected error message
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

21.Verify Updating an Order Without a Complete Body

- HTTPS method for request:PATCH
- Test types / techniques used:Positive testing,unit testing,blackbox testing
- How I checked:Submit an order to create some data and retrieve the order ID,Make a request to update the order without providing a complete request body,Verify if the response status code is 204 (No Content), indicating a successful update,Make a request to get the updated order,Verify if the customer name in the updated order remains unchanged
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

22.Verify Retrieval of an Order by Invalid ID

- HTTPS method for request:GET
- Test types / techniques used:Negative testing,unit testing,blackbox testing
- How I checked:Submit an order to create some data and retrieve the order ID,Make a request to get an order using an invalid ID,Verify if the response status code is 404 (Not Found),Verify if the 'error' key in the JSON response contains the expected error message.
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

23.Verify Submission of an Order Without Customer Name

- HTTPS method for request:POST
- Test types / techniques used:Negative testing,unit testing,blackbox testing
- How I checked:Make a request to submit an order without providing a customer name,Verify if the response status code is 400 (Bad Request), indicating an error due to missing customer name
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

24.Verify Submission of an Order Without Book ID

- HTTPS method for request:POST
- Test types / techniques used:Negative testing,unit testing,blackbox testing
- How I checked:Make a request to submit an order without providing a book ID,Verify if the response status code is 400 (Bad Request), indicating an error due to missing book ID,Verify if the 'error' key in the JSON response contains the expected error message.
- [Link to test_order](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/tests/test_order.py).

# Execution report 

Below you can find the execution report generated on the 23/02/2024:

![Execution report](https://github.com/AdrianPricopie/Python-API-Testing-/blob/main/Screenshots/raport_pytest.png)

Out of 24 test cases, 22 have passed successfully, while 2 have failed. Two bugs have been identified during the testing process. 

# Bug found:
I.Inconsistent Status Code on Order Submission

Description:
During testing, an inconsistency was observed between the expected and observed behavior regarding the response status codes when attempting to submit an order without providing a required field.

Steps to Reproduce:
1.Send a POST request to /orders/ without providing the required customerName field in the request body.

Actual Results:
The received status code is 201 Created.

Expected Results:
The expected status code is 400 Bad Request since providing customerName is mandatory.

II. Missing 'customerName' Key in GET Order by ID Response After Incomplete PATCH Request

Description:
An issue has been identified where the 'customerName' key is missing from the response of a GET request for a specific order ID after an incomplete PATCH request.

Steps to Reproduce:
1.Submit a POST request to create a new order and retrieve the order ID.
2.Attempt to update the order by sending a PATCH request without providing a complete request body.
3.Retrieve the order details using a GET request for the specific order ID.

Actual results:

KeyError:"CustomerName"

Expected Result:The 'customerName' key should still be present in the response of the GET request for the specific order ID.

# Conclusion

This comprehensive testing project has effectively utilized various test cases to validate the functionality of the Simple Books API. The combination of positive and negative testing, along with the consideration of different scenarios, has provided valuable insights into the reliability and correctness of the API.

The test cases cover a wide range of functionalities, including authentication, retrieving book details, submitting orders, updating orders, deleting orders, and handling different error scenarios. The use of clear test conditions, well-defined test types, and thorough execution has contributed to the identification of two critical bugs.

The first bug highlights an inconsistency in the status code returned during order submission without providing a required field (customerName). The observed behavior (201 Created) deviates from the expected result (400 Bad Request), leading to a potential issue in handling missing information.

The second bug addresses a missing 'customerName' key in the response of a GET request for a specific order ID after an incomplete PATCH request. The absence of the 'customerName' key, leading to a KeyError, signifies a discrepancy in maintaining the order details after an incomplete update.
Overall, the successful execution of 22 out of 24 test cases demonstrates the robustness of the API in various scenarios. The identified bugs offer opportunities for refinement and improvement in the API's error handling and response consistency. The execution report, including the test outcomes and bugs, provides a comprehensive overview of the testing process and outcomes.

The project's documentation is well-structured, providing clarity on the tested functionalities, tools used, and the test environment. The inclusion of execution reports and bug reports enhances the transparency and effectiveness of the testing effort.

In conclusion, this API testing project has effectively applied testing principles and methodologies to ensure the reliability and correctness of the Simple Books API. The identified bugs contribute to the continuous improvement of the API, fostering a robust and dependable application






















  



 
 
  



  





















