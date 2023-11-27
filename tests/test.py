import unittest
import warnings
import sys
from datetime import datetime

sys.path.append("../")
from main import get_suggestions, convert_to_list, convert_to_list_num, app

warnings.filterwarnings("ignore")


class TestMain(unittest.TestCase):

    def test_get_suggestions(self):
        suggestions = get_suggestions()
        self.assertTrue(isinstance(suggestions, list))

    def test_convert_to_list(self):
        result = convert_to_list('["abc", "def"]')
        self.assertEqual(result, ["abc", "def"])
    
    def test_convert_to_list_num(self):
        result = convert_to_list_num("[1, 2, 3]")
        self.assertEqual(result, [1, 2, 3])

    def test_home_route(self):
        with app.test_client() as client:
            response = client.get("/home")
            self.assertEqual(response.status_code, 200)

    def test_recommend_route(self):
        with app.test_client() as client:
            response = client.post(
                "/recommend",
                data={
                    "title": "Test Movie",
                    "poster": "test_poster.jpg",
                    "overview": "Test overview",
                    "vote_average": "8.0",
                    "vote_count": "100",
                    "release_date": "2022-01-01",
                    "runtime": "120",
                    "status": "Released",
                    "genres": "Action, Adventure",
                    "rec_movies": '["Movie 1", "Movie 2"]',
                    "rec_posters": '["poster1.jpg", "poster2.jpg"]',
                    "rec_movies_org": '["Movie 1", "Movie 2"]',
                    "rec_year": "[2020, 2021]",
                    "rec_vote": "[8.5, 9.0]",
                    "rec_ids": "[1, 2]",
                },
            )
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
