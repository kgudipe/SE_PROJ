# Movie Recommendation API Documentation

## Introduction

The Movie Recommendation API provides endpoints for retrieving movie recommendations based on user input. It utilizes a machine learning model to generate recommendations and includes features such as autocomplete suggestions and detailed movie information.

## Base URL

The base URL for the API is: `http://localhost:5000/`

## Endpoints

### 1. Home Page - Get Autocomplete Suggestions

- **Endpoint:** `GET /home`
- **Description:** Returns a list of movie title suggestions for autocomplete.
- **Request:** `GET /home`
- **Response:**
  ```json
  {
    "suggestions": ["Movie 1", "Movie 2", "Movie 3"]
  }

### 2. Populate Movie Matches

- **Endpoint:** `POST /populate-matches`
- **Description:** Populates movie matches based on user-provided movie details.
- **Request:** `POST /populate-matches`
- **Body Example:**
  ```json
  {
    "movies_list": [
      {
        "poster_path": "/path/to/poster",
        "title": "Movie Title",
        "original_title": "Original Title",
        "vote_average": 8.5,
        "release_date": "2022-01-01",
        "id": 123
      },
    ]
  }
- **Response:**
  - **Status Code:** 200 OK
  - **Content Type:** text/html

### 3. Get Movie Recommendations

- **Endpoint:** `POST /recommend`
- **Description:** Generates movie recommendations based on user input and provides detailed movie information.
- **Request:** `POST /recommend`
- **Form Data:**
  - title: Movie title
  - cast_ids: Comma-separated list of cast IDs
  - cast_names: Comma-separated list of cast names
  - cast_chars: Comma-separated list of cast characters
  - ... (other form data fields)
- **Response:** 
  - **Status Code:** 200 OK
  - **Content Type:** text/html

# search.py Code Documentation

This documentation provides details about the `Search` class in the `search.py` file.

## Class: Search

The `Search` class in `search.py` contains the following methods:

### 1. startsWith(self, word)

**Input:**
- `word`: It is a string where users can write the name of the movie.

**Output:**
- Returns a list of movies that start with the given word.

### 2. anywhere(self, word, visitedWords)

**Input:**
- `word`: It is a string where users can write the name of the movie.
- `visitedWords`: A set (unordered hash-map) of movies that should not be part of the output.

**Output:**
- Returns a list of movies that have the input word anywhere in its title.

### 3. results(self, word)

**Input:**
- `word`: It is a string where users can write the name of the movie.

**Output:**
- Returns a list of movies where the first few movies will be the ones that start with the input word, followed by the movies that have the input word anywhere in its title.

### 4. resultsTop10(self, word)

**Input:**
- `word`: It is a string where users can write the name of the movie.

**Output:**
- Returns the first 10 results from the method `results`.
