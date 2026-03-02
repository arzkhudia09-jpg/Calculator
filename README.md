# Flask Calculator

A simple web-based calculator built with Flask.

## Purpose

This project demonstrates a basic server-rendered web application using Python and Flask. It takes two numeric inputs and an arithmetic operation, performs the calculation on the server, and displays the result in the browser.

## Features

- Addition, subtraction, multiplication, and division
- Server-side calculation logic
- Error handling for invalid input (including division by zero)
- Single-page UI built with HTML and CSS

## Frameworks and Technologies Used

- Python 3
- Flask (web framework)
- Jinja2 (template rendering via Flask)
- HTML5
- CSS3

## Project Structure

- `app.py`: Flask app entry point and route handling
- `definition.py`: Arithmetic operation functions
- `templates/index.html`: Main UI template
- `static/style.css`: Stylesheet
- `requirements.txt`: Python dependencies

## How to Run

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   python app.py
   ```

4. Open your browser at `http://127.0.0.1:5000`.

## Notes

- The application listens on `0.0.0.0`.
- It uses the `PORT` environment variable when provided; otherwise, it defaults to `5000`.
