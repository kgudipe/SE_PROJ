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
    
    # Load the dataset
    df = pd.read_csv('../../data/MovieGenre.csv', encoding='ISO-8859-1')


    #df = df.rename(columns={'Movie Poster': 'movie_poster'})

    # Filter the movies based on the genre
    filtered_movies = df[df['Genre'].str.contains(genre, case=False, na=False)]

    
    return render_template('genrePage.html', movies=filtered_movies.to_dict(orient='records'), genre=genre)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
