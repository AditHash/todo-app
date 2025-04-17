# ToDo App

This is a simple ToDo application built using Flask and Bootstrap. It allows users to manage their tasks by adding, editing, and deleting them. The frontend is styled using Bootstrap for a clean and responsive design.

## Features

- View a list of tasks.
- Add new tasks with a topic and description.
- Edit existing tasks.
- Delete tasks.

## Installation Instructions

Follow these steps to set up and run the project locally:

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd uv-test
   ```

2. **Set Up a Virtual Environment**  
   Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   Start the Flask development server:
   ```bash
   flask run
   ```

5. **Access the Application**  
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Project Structure

- `templates/`: Contains the HTML templates for the application.
- `app.py`: The main Flask application file.
- `static/`: Contains static files like CSS and JavaScript (if any).

## Requirements

- Python 3.7 or higher
- Flask

## License

This project is licensed under the MIT License.
