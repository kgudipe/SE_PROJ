# <i>Movie Recommendation 🎥 </i>
    A collaborative filtering based recommendation engine!




[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://gitHub.com/kgudipe/SE_PROJ/graphs/commit-activity) [![Contributors Activity](https://img.shields.io/github/commit-activity/m/kgudipe/SE_PROJ)](https://github.com/kgudipe/SE_PROJ/pulse) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com) [![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10023338.svg)](https://doi.org/10.5281/zenodo.10023338) [![GitHub issues](https://img.shields.io/github/issues/kgudipe/SE_PROJ.svg)](https://github.com/kgudipe/SE_PROJ/issues/) [![GitHub issues-closed](https://img.shields.io/github/issues-closed/kgudipe/SE_PROJ.svg)](https://github.com/kgudipe/SE_PROJ/issues?q=is%3Aissue+is%3Aclosed)  [![black](https://img.shields.io/badge/StyleChecker-black-purple.svg)](https://pypi.org/project/black/) ![15465](https://img.shields.io/github/repo-size/kgudipe/SE_PROJ?label=Repo%20Size) ![33.5 kB](https://img.shields.io/github/languages/code-size/kgudipe/SE_PROJ) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Contributors](https://img.shields.io/github/contributors/kgudipe/SE_PROJ) [![Coverage](https://img.shields.io/badge/coverage-99%25-brightgreen)](file:///C:/Users/saisa/Documents/SE_PROJ/Project2/test/htmlcov/index.html)

### Project 3 Plan

(Please see [wiki](https://github.com/git-ankit/MovieRecommender/wiki/Project-3-Plan) for detailed information.)

Testing how good the Movie Recommender is :

1. Pick 10-15 very famous movies.
2. Make sure the movies have diversity based on genre, cast and production style.
3. Show users a set of 10 randomly generated movies vs top 10 movies recommended by the Movie Recommender.
4. Also ask the user how satisfied is he/she with the recommended movies.
4. Collect your results and quantify them.

Note: Our system can be virtually uploaded to sites like [Code SandBox](https://codesandbox.io/), for easier testing.

Make sure you taste your own medicine first and take into account other peoples familiarity with the system before you design your tests.


### Video ▶️ 

<a  href="https://youtu.be/OSjpryqI1RQ"><img height=150 width=500 alt="logo here" src="https://raw.githubusercontent.com/git-ankit/MovieRecommender/master/asset/group12.png"/></a>



### Working 📱
<a  href="https://www.youtube.com/watch?v=MwQxNfARMio&ab_channel=KoushikGudipelly"><img height=150 width=500 alt="logo here" src="https://github.com/kgudipe/SE_PROJ/blob/main/Project2/asset/Working.png"/></a>



### Tech stack 👨‍💻
- Python, Flask, HTML, CSS and JavaScript

### Requirements and Setup ⚙️


- python 3.5 +
- pip
- Style check  - black
    `pip install black`
- Static code analyser - Pylance
    `Install it in VS Code`

- Install all required python packages
    `pip install -r requirements.txt `

### Usage
1. `cd Code/recommenderapp`
2. `python3 app.py`

![Execution](https://raw.githubusercontent.com/git-ankit/MovieRecommender/master/asset/execution.gif)


### What's New
Navigation Bar Improvements:

Customizable UI introduced for a better user experience.
Seamless navigation between the home page and genre selections.
Genre dropdown includes: Action, Comedy, Thriller, Adventure, Romance, Science Fiction, Fantasy, and Crime.


Year-wise Movie Sorting and Listing:

Users can sort movies based on their release years.
Updated dataset comprises 9,000 movies up to 2018.
Genre-based movie listings enhanced with a pagination feature.


Advanced Recommendation System:

Integration of item-item based collaborative filtering with employed cosine similarity to refine recommendations.
The system is now more optimized to showcase only the top 10 movie recommendations.


Improved Search Capabilities:

AJAX requests have been minimized by:
Introducing a slight delay before search activation.
Implementing a minimum character length of 1 for search triggers.
Search results enhanced with a "remove" functionality for user flexibility.


Optimized Genre Processing:

Transitioned from sequential genre processing to vectorized operations using pandas.
Achieved a significant 50% speedup in genre processing times.

### Rubric
Refer to Rubric.md file [here](https://github.com/kgudipe/SE_PROJ/blob/main/Project2/Rubrics.md)

### Documentation 📚
Refer to Wiki page [here](https://github.com/git-ankit/MovieRecommender/wiki/Documentation)


### Bug? 🐛
Raise a issue on this repository, we would love to look at it ❤️
