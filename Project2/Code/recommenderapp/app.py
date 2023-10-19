from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import json
import sys
import csv
import time
import pandas as pd

sys.path.append("../../")
from Code.prediction_scripts.item_based import recommendForNewUser
from search import Search

app = Flask(__name__)
app.secret_key = "secret key"

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def landing_page():
    return render_template("landing_page.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.data)  # contains movies
    data1 = data["movie_list"]
    training_data = []
    for movie in data1:
        movie_with_rating = {"title": movie, "rating": 5.0}
        training_data.append(movie_with_rating)
    recommendations = recommendForNewUser(training_data)
    recommendations = recommendations[:10]
    resp = {"recommendations": recommendations}
    return resp


@app.route("/search", methods=["POST"])
def search():
    term = request.form["q"]
    print("term: ", term)

    search = Search()
    filtered_dict = search.resultsTop10(term)

    resp = jsonify(filtered_dict)
    resp.status_code = 200
    return resp


@app.route("/feedback", methods=["POST"])
def feedback():
    data = json.loads(request.data)
    with open("experiment_results/feedback_{}.csv".format(int(time.time())), "w") as f:
        for key in data.keys():
            f.write("%s - %s\n" % (key, data[key]))
    print(data)
    return data


@app.route("/success")
def success():
    return render_template("success.html")

@app.route('/genrePage.html')
def genre_page():
    genre = request.args.get('Genre', default="Action", type=str)

     # Pagination
    page = request.args.get('page', default=1, type=int)
    per_page = 30
    start_from = (page - 1) * per_page
    end_on = start_from + per_page
    
    # Load the dataset
    df = pd.read_csv('../../data/MovieGenre.csv', encoding='ISO-8859-1')

    df['Year'] = df['Title'].str.extract(r'\((\d{4})\)').astype(float)

    # Filter the movies based on the genre
    filtered_movies = df[df['Genre'].str.contains(genre, case=False, na=False)]

    sorted_movies = filtered_movies.sort_values(by="Year", ascending=False)

    paginated_movies = sorted_movies.iloc[start_from:end_on]
    
    return render_template('genrePage.html', movies=paginated_movies.to_dict(orient='records'), genre=genre, current_page=page, total_pages=(len(filtered_movies) // per_page) + 1)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
