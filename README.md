# School Review Web App (Edusaint Task)

This is a Flask-based web application that allows users to submit and view school reviews. Reviews are stored in a MySQL database and displayed with a Bootstrap-styled UI.

## Features

- Submit reviews with school name, reviewer, rating, and comments
- View all submitted reviews in a table
- MySQL database integration
- Bootstrap responsive layout
- Basic form validation and flash messages

## Tech Stack

- Flask
- MySQL
- Bootstrap 5
- Jinja2 Templates

## Project Structure

school_review_app/
├── app.py # Main Flask application
├── config.py # DB configuration using dotenv
├── .env # Environment variables (NOT committed to Git)
├── reviews.sql # SQL file to create database and table
├── requirements.txt # Python dependencies
├── static/ # Optional custom CSS/JS
├── templates/ # Jinja2 HTML templates
│ ├── base.html # Base layout with navbar and styling
│ ├── home.html # Landing page with buttons
│ ├── add_review.html # Form to submit a new review
│ └── reviews.html # Page displaying all reviews
└── README.md # Project documentation (this file)


---

## Setup Instructions

Follow these steps to get the app running locally:

### 1. Install Python Requirements

Make sure you have Python 3.9+ and MySQL installed. Then run:

```bash
pip install -r requirements.txt

### 2. Set Up .env File

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=school_reviews

### 3. Create Database & Table

Use the reviews.sql file to create the required database and table.

Option A: Terminal
```bash
mysql -u root -p < reviews.sql

Option B: MySQL Workbench
Open reviews.sql, run it manually.

### 4. Start your Flask app:

```bash
python app.py

Then visit: http://127.0.0.1:5000