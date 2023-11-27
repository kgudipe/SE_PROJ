# Movie Recommendation API Documentation

## Introduction

The Movie Recommendation API provides endpoints for retrieving movie recommendations based on user input. It utilizes a machine learning model to generate recommendations and includes features such as autocomplete suggestions and detailed movie information.

## Base URL

The base URL for the API is: `http://localhost:5000/`

## Endpoints

### 1. Get Autocomplete Suggestions

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
      ...
    ]
  }
