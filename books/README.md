# Books Collection API 📚

This is a **Django-based RESTful API** for managing a collection of books. It provides endpoints for CRUD operations, ensures data validation, and includes a feature to recommend a random book.

---

## Features 🚀

### API Endpoints

1. **GET /**  
   - **Description**: Displays a welcome message with basic information.  
   - **Response**:  
     ```json
     {
       "home": "you can select the book by id"
     }
     ```

2. **GET /books**  
   - **Description**: Fetch all books in the database.  
   - **Response**:  
     Returns a list of all books with their details.

3. **GET /books/:id**  
   - **Description**: Retrieve details of a specific book by its ID.  
   - **Response**:  
     Returns details of the requested book.

4. **POST /books**  
   - **Description**: Add a new book to the collection.  
   - **Request Body**:  
     ```json
     {
       "title": "Book Title",
       "author": "Author Name",
       "isbn": "1234567890",
       "published_year": 2021
     }
     ```
   - **Response**:  
     Returns the newly created book's details on success.

5. **POST /books/:id**  
   - **Description**: Update an existing book's details by ID.  
   - **Request Body**: Same as `POST /books`.  
   - **Response**:  
     Returns the updated book's details.

6. **DELETE /books/:id**  
   - **Description**: Remove a book from the collection using its ID.  
   - **Response**:  
     Returns a success message and `204 No Content` status.

7. **GET /books/recommendations**  
   - **Description**: Suggests a random book from the collection.  
   - **Response**:  
     Returns the details of the recommended book. If the collection is empty, it returns:  
     ```json
     {
       "message": "No books available for recommendations."
     }
     ```

---

## Technologies Used 🛠️

- **Django**: Framework for building the backend.  
- **Django REST Framework (DRF)**: For creating RESTful APIs.  
- **SQLite**: Database for storing book records.  

---

## Installation and Setup ⚙️

Follow the steps below to run this project locally:

### Prerequisites

Ensure you have the following installed:  
- Python 3.10+  
- `pip` (Python package manager)

### Steps

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/books-collection-api.git
   cd books-collection-api
   ```

Install Dependencies
Install the required dependencies by running:

bash
Copy code
pip install -r requirements.txt
Apply Migrations
Set up the database with the following command:

bash
Copy code
python manage.py migrate
Run the Server
Start the development server:

bash
Copy code
python manage.py runserver
Testing the API
Use tools like Postman or curl to interact with the API endpoints.

Example Usage 📖
Add a New Book
Endpoint: POST /books
Request Body:

json
Copy code
{
  "title": "Learn Python the Hard Way",
  "author": "Zed A. Shaw",
  "isbn": "9780134692883",
  "published_year": 2017
}
Get All Books
Endpoint: GET /books
Response:

json
Copy code
[
  {
    "id": 1,
    "title": "Learn Python the Hard Way",
    "author": "Zed A. Shaw",
    "isbn": "9780134692883",
    "published_year": 2017
  }
]
Custom Features ✨
Book Recommendations: The /books/recommendations endpoint suggests a random book from the collection.
Validation: Ensures valid data for title, author, isbn, and published_year before creating or updating a book.
Deployment 🌐
The API can be deployed to any public hosting platform (e.g., Render, Vercel, or Fly.io). Once deployed, share the live link here:
Deployed API URL

Folder Structure 🗂️
views.py: Contains all the API endpoints logic.
models.py: Defines the Book model for the database.
serializers.py: Converts database objects to JSON and validates input data.
urls.py: Maps URLs to the view functions.