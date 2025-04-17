# ToDo App

This is a simple ToDo application built using Flask and Bootstrap. It allows users to manage their tasks by adding, editing, and deleting them. The frontend is styled using Bootstrap for a clean and responsive design.

This project includes a working implementation of Docker Compose using Python and MongoDB.

## Features

- View a list of tasks.
- Add new tasks with a topic and description.
- Edit existing tasks.
- Delete tasks.

## Installation Instructions

Follow these steps to set up and run the project using Docker Compose:

1. **Clone the Repository**  
   Clone this repository to your local machine:
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

4. **Stop the Application**  
   To stop the application, press `Ctrl+C` in the terminal and run:
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
