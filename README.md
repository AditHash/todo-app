# ToDo App

This is a simple ToDo application built using Flask and Bootstrap. It allows users to manage their tasks by adding, editing, and deleting them. The frontend is styled using Bootstrap for a clean and responsive design.

This project includes a working implementation of Docker Compose using Python and MongoDB.

## Features

1. **Authentication**:
   - Users can register, log in, and log out.
   - Each user's ToDo items are private and tied to their account.

2. **ToDo Management**:
   - Add, edit, delete, and mark tasks as completed.
   - Tasks include the following fields:
     - `Topic`: A short title for the task.
     - `Description`: A detailed description of the task.
     - `Due Date`: A deadline for the task.
     - `Priority`: Priority levels (`Low`, `Medium`, `High`).
     - `Status`: Mark tasks as `Completed` or `Pending`.

3. **REST API**:
   - Exposes a `/api/todos` endpoint for managing ToDo items programmatically.
   - Supports `GET` and `POST` methods.

4. **Health Check**:
   - A `/health` endpoint to verify the application's status.

## Environment Variables

The application uses a `.env` file to store sensitive information. Below are the required variables:

- `MONGO_URI`: MongoDB connection string (default: `mongodb://localhost:27017/`).
- `SECRET_KEY`: A secret key for Flask session management.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AditHash/todo-app.git
   cd todo-app
   ```

2. **Run the Application with Docker Compose**  
   Build and start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**  
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

4. Run the application:
   ```bash
   docker-compose down
   ```

## Project Structure

- `templates/`: Contains the HTML templates for the application.
- `app.py`: The main Flask application file.
- `static/`: Contains static files like CSS and JavaScript (if any).
- `docker-compose.yml`: Configuration file for Docker Compose.
- `Dockerfile`: Dockerfile for building the Flask application container.

## Requirements

- Docker
- Docker Compose

## License

This project is licensed under the MIT License.
