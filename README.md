# Books Collection API

This is a Django-based RESTful API for managing a collection of books. It allows users to perform CRUD operations on books, validate the data, and get recommendations. The API supports adding, updating, deleting, and fetching books from a database.

## Routes and Expected Responses

1. **Route**: `/books`  
   - **Method**: `GET`  
   - **Response**: Returns a list of all books in the collection.
   
2. **Route**: `/books/:id`  
   - **Method**: `GET`  
   - **Response**: Returns details of the book with the specified ID.
   
3. **Route**: `/books`  
   - **Method**: `POST`  
   - **Request Body**:  
     ```json
     {
       "title": "Book Title",
       "author": "Book Author",
       "isbn": "Book ISBN",
       "published_year": 2024
     }
     ```
   - **Response**: Adds a new book to the collection and returns the book details.

4. **Route**: `/books/:id`  
   - **Method**: `POST`  
   - **Request Body**:  
     ```json
     {
       "title": "Updated Title",
       "author": "Updated Author",
       "isbn": "Updated ISBN",
       "published_year": 2024
     }
     ```
   - **Response**: Updates the book with the specified ID.

5. **Route**: `/books/:id`  
   - **Method**: `DELETE`  
   - **Response**: Deletes the book with the specified ID.

6. **Route**: `/books/recommendations`  
   - **Method**: `GET`  
   - **Response**: Returns a random book from the collection as a suggestion.

## Features

- **CRUD Operations**: Supports create, read, update, and delete operations for managing books.
- **Data Validation**: Ensures valid data (title, author, isbn, and published year) when adding or updating books.
- **Recommendations**: Suggests a random book from the collection via the `/books/recommendations` endpoint.

## Project Setup

Follow the instructions below to set up and run the project locally.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.10 or higher
- Django 5.1 or higher
- pip (Python package installer)

### Setting Up the Project Locally

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/books-collection-api.git
Navigate to the Project Directory

Change into the project directory:

bash
Copy code
cd books-collection-api
Install Dependencies

Install the required dependencies using pip. It is recommended to create a virtual environment before installing the dependencies.

bash
Copy code
pip install -r requirements.txt
Apply Migrations

Run the following command to apply the migrations to set up the database:

bash
Copy code
python manage.py migrate
Start the Development Server

Start the Django development server:

bash
Copy code
python manage.py runserver
By default, the server will run at http://127.0.0.1:8000/.

Testing the API
Once the server is running, you can test the following routes in your browser or using an HTTP client (e.g., Postman, cURL):

/books: returns a list of all books in the collection.
/books/:id: returns details of the book with the specified ID.
/books (POST): adds a new book to the collection.
/books/:id (POST): updates the book with the specified ID.
/books/:id (DELETE): deletes the book with the specified ID.
/books/recommendations: returns a random book as a recommendation.
Deployment
This API can be deployed to any public hosting platform (e.g., Render, Vercel, or Fly.io). Once deployed, share the live link here:
Deployed API URL: [Insert the live URL here]

Repository Structure
views.py: Contains all the API endpoint logic.
models.py: Defines the Book model for the database.
serializers.py: Converts database objects to JSON and validates input data.
urls.py: Maps URLs to the view functions.
requirements.txt: Lists the dependencies for the project.

