from flask import Flask, render_template, request, redirect, flash
import mysql.connector
from config import Config

app = Flask(__name__)
app.secret_key = "supersecretkey"

db = mysql.connector.connect(
    host=Config.MYSQL_HOST,
    user=Config.MYSQL_USER,
    password=Config.MYSQL_PASSWORD,
    database=Config.MYSQL_DB
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add-review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        school_name = request.form['school_name']
        reviewer_name = request.form['reviewer_name']
        rating = request.form['rating']
        comment = request.form['comment']

        if not (school_name and reviewer_name and rating):
            flash("Please fill all required fields", "danger")
        else:
            cursor.execute("INSERT INTO reviews (school_name, reviewer_name, rating, comment) VALUES (%s, %s, %s, %s)",
                           (school_name, reviewer_name, rating, comment))
            db.commit()
            flash("Review added successfully!", "success")
            return redirect('/add-review')  # <- This is key

    return render_template('add_review.html')


@app.route('/reviews')
def reviews():
    cursor.execute("SELECT * FROM reviews ORDER BY id DESC")
    reviews_list = cursor.fetchall()
    return render_template('reviews.html', reviews=reviews_list)

if __name__ == '__main__':
    app.run(debug=True)
