from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vignesh@139",
    database="cineverse"
)

cursor = db.cursor()

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Movies Page
@app.route('/movies')
def movies():
    cursor.execute("SELECT * FROM movies")
    data = cursor.fetchall()
    return render_template("movies.html", movies=data)

# Add Review Page
@app.route('/add_review', methods=['GET', 'POST'])
def add_review():

    if request.method == 'POST':

        movie_id = request.form['movie_id']
        user_id = request.form['user_id']
        rating = request.form['rating']
        comment = request.form['comment']

        sql = """
        INSERT INTO reviews(movie_id, user_id, rating, comment)
        VALUES (%s, %s, %s, %s)
        """

        values = (movie_id, user_id, rating, comment)

        cursor.execute(sql, values)
        db.commit()

        return "Review Added Successfully!"

    return render_template("add_review.html")

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)