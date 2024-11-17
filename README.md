```markdown
# Basic Web Server with Django

This is a simple Django project that implements a basic web server with three routes. The server responds with static messages based on the route requested. This is the first step in backend development.

## Routes and Expected Responses

1. **Route**: `/name`
   - **Response**: Returns your full name as a plain text message.
   
2. **Route**: `/hobby`
   - **Response**: Returns your favorite hobby or a fun activity you enjoy as a JSON object.
   
3. **Route**: `/dream`
   - **Response**: Returns a motivational message about your dream or goal in life.

## Features

- **GET** method is used for all routes.
- Returns the appropriate data with HTTP status code **200 OK**.

## Project Setup

Follow the instructions below to set up and run the project locally.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.10
- Django 5.1 or higher
- pip (Python package installer)

### Setting Up the Project Locally

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/Ibnumer4/Basic-web-server.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd Basic-web-server
   ```

3. **Install Dependencies**

   Install the required dependencies using pip. It is recommended to create a virtual environment before installing the dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   Run the following command to apply the migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   By default, the server will run at `http://127.0.0.1:8000/`.

### Testing the Routes

Once the server is running, you can test the following routes in your browser or using an HTTP client (e.g., Postman, cURL):

1. **/name**: returns `Nazir Umer` as a plain text message.
2. **/hobby**: returns a JSON object with ```{"favoriteHobby": "My hobby is reading books and learning new things, as it fuels my curiosity and broadens my knowledge."}```.
3. **/dream**: returns `My dream is to empower learning and innovation through technology and to be valued internationally and achieve success through meaningful contributions to the world.`.


## Deployment

This Django web server is hosted on https://pythonanywhere.com/. You can access the live version of the server via the following link:

[Live Server](https://ibnumertechub.pythonanywhere.com/)

## Repository Structure

- **`manage.py`**: Command-line utility for administrative tasks.
- **`project_name/`**: The project directory containing the settings and configurations.
- **`app_name/`**: The Django app with the views and routes.
- **`requirements.txt`**: Lists the dependencies for the project.