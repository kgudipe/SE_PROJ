# <i>Movie Recommendation System🎥 </i>
![Python](https://img.shields.io/badge/Python-3.6.13-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-green)
![API](https://img.shields.io/badge/API-TMDB-fcba03)

This Movie Recommender System is like having a movie buddy who knows your taste super well. It looks at movie info from TMDB and even checks out what people say on IMDB. Then, it uses something called cosine similarity along with the sentiment analysis to match you with movies you'll love.

Imagine each movie is a star, and cosine similarity is like a cool trick to see which stars go together in the movie universe. You just type in a movie you like, and boom! It suggests other movies you'll probably dig. Setting it up is a breeze—just follow the steps. It's like having your own movie sidekick, making sure every suggestion is spot-on for your movie mood!
    


### Architecture of the Recommendation System 🏗️

### What's New? 🤔
**🔄 Evolution Snapshot: Old vs. New**
- **Static to Dynamic Magic:** Old system had static movie details - a fixed menu with limited movie details. But now, with dynamic web scraping, we're serving real-time details like titles, cast details, genres, and eye-catching posters. So even the latest movies released are incorporated into the recommendation model. It's not just a movie; it's a dynamic experience! 🍿✨

- **Predictable to Feel-Good Feels:** Before, we just knew your movie likes. Now, with sentiment analysis, we feel them too! Reviews are no longer just words; they're a mix of positive and negative vibes. So now instead of taking a list of movies from the user and suggesting another list of similar movies, we now present to you the most similar movies that you would like based on your movie selection and how other people feel about it (using sentiment analysis). Your movie night just got a mood boost! 🎭👍

- **Interface Glow-Up:** Say goodbye to the old look; we've given it a complete makeover! The user interface is now a captivating wonderland of movie details, cast revelations, and user reviews. One can even get details of the cast like when their birthday and place of birth is, if you are curious, and also a biography explaining their jouney in the movie industry. It's not just watching; it's a visual feast! 🎨👀

- **Poster Pretty to Interactive Play:** Posters were just pretty faces. Now, click on them, and it's a gateway to excitement! Experience the thrill with interactive movie trailers. It's not just lights, camera, action; it's lights, camera, interaction! 🎬🔗



### Video ▶️ 





### How to run the project? ⚙️

1. Create an account on [TMDB](https://www.themoviedb.org/).

2. Obtain your API key by clicking on the API link in your account settings.

3. Copy or download this repository to your local machine.

4. Create a new conda environment using the command:

    ```bash
    conda create --name YOUR_ENV_NAME python=3.6.13
    ```

5. Activate the conda environment:

    ```bash
    conda activate YOUR_ENV_NAME
    ```

6. Install all required Python packages using:

    ```bash
    pip install -r requirements.txt
    ```

7. Replace `YOUR_API_KEY` in both instances (line no. 15 and 29) within the `static/recommend.js` file and save the changes.

8. Launch your terminal or command prompt from the project directory and execute `main.py` using the command `python main.py`.

9. Access [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.






### Rubric 📝
Refer to Rubric.md file [here](https://github.com/kgudipe/SE_PROJ/blob/main/Project2/Rubrics.md)

### Documentation 📚
Refer to Wiki page [here](https://github.com/git-ankit/MovieRecommender/wiki/Documentation)



### Similarity Score 📏
The recommender system employs a similarity score to quantify the likeness between two items, providing a numerical measure on a scale from zero to one. This score is derived through the application of cosine similarity, a method that assesses the resemblance between the textual details of the two items. The resulting numerical value encapsulates the degree of similarity, with zero indicating dissimilarity and one signifying identical text details. In essence, the similarity score serves as a crucial metric for the system to gauge and rank the similarity between items based on their textual characteristics.

### How Cosine Similarity Works 🔍

Cosine similarity is a measure used to evaluate the similarity between two vectors by calculating the cosine of the angle between them in a multi-dimensional space. In the context of the recommender system, these vectors represent the textual details of different movies. The method is particularly useful when dealing with high-dimensional data, as it captures the similarity between items irrespective of their overall size. A smaller angle between vectors indicates higher similarity, making cosine similarity a valuable tool for comparing and ranking items based on their textual characteristics.

For a deeper dive into the mathematical aspects of cosine similarity, refer to the [Cosine Similarity Wikipedia page](https://en.wikipedia.org/wiki/Cosine_similarity).

## Datasets 📊

The project utilizes data from the following sources:

1. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
2. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
3. [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)
4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
5. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)


## Funding 💰
The project is not currently funded

## Future Roadmap 🌠

See RoadMap here:

### Bug? 🐛
Raise a issue on this repository, we would love to look at it ❤️

# Contributors 👥
  <table>
  <tr>
    <td align="center"><a href="https://github.com/prathyu99"><img src="https://avatars.githubusercontent.com/u/33190791?v=4" width="100px;" alt=""/><br /><sub><b>Prathyusha Kodali</b></sub></a></td>
    <td align="center"><a href="https://github.com/aravinda-1402"><img src="https://avatars.githubusercontent.com/u/71303848?v=4" width="100px;" alt=""/><br /><sub><b>Aravinda Raman Jatavallabha</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/SurajRKU"><img src="https://avatars.githubusercontent.com/u/53537228?v=4" width="100px;" alt=""/><br /><sub><b>Suraj Raghu Kumar</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/yuktasree"><img src="https://avatars.githubusercontent.com/u/64723066?v=4" width="100px;" alt=""/><br /><sub><b>Yuktasree Muppala</b></sub></a><br /></td>
  </tr>
</table>

**For any further support please email us:** segrp12fall2023@gmail.com 




