# Flask Calculator

A phone-style web calculator built with Flask.

## Purpose

This project demonstrates how to build a server-rendered calculator app with Flask, while providing a modern calculator-like interface in the browser. Calculations are handled on the server, and the UI is designed to feel similar to a mobile calculator.

## Features

- Phone-style calculator UI with display and keypad
- Basic operations: addition, subtraction, multiplication, and division
- Clear (`AC`) and delete (`DEL`) controls
- Keyboard support
- Server-side calculation logic
- Error handling (including division by zero)

## Keyboard Controls

- `0-9`: Enter numbers
- `.` or `,`: Decimal input
- `+`, `-`, `*`, `/`: Choose operation
- `Enter` or `=`: Calculate
- `Backspace`: Delete last character
- `Escape`: Clear all

## Frameworks and Technologies Used

- Python 3
- Flask
- Jinja2
- HTML5
- CSS3
- Vanilla JavaScript

## Project Structure

- `app.py`: Flask app, routing, cache control, and template rendering
- `definition.py`: Arithmetic helper functions
- `templates/index.html`: Calculator markup and client-side keypad/keyboard logic
- `static/style.css`: Calculator styling
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
4. Open `http://127.0.0.1:5000` in your browser.

## Notes

- The app listens on `0.0.0.0`.
- It uses the `PORT` environment variable if available; otherwise it defaults to `5000`.
- Static/template caching is disabled for easier local development updates.
