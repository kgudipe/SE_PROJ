import unittest
from datetime import datetime
from search import Search

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.search = Search()

    def test_startsWith(self):
        result = self.search.startsWith("Star")
        expected = ['Star Wars: Episode IV - A New Hope (1977)', 'Star Wars: Episode V - The Empire Strikes Back (1980)', 'Star Wars: Episode VI - Return of the Jedi (1983)']
        self.assertEqual(result, expected)

    def test_anywhere(self):
        visited_words = set()
        result = self.search.anywhere("Star", visited_words)
        expected = ['Star Wars: Episode IV - A New Hope (1977)', 'Star Wars: Episode V - The Empire Strikes Back (1980)', 'Star Wars: Episode VI - Return of the Jedi (1983)', 'Star Trek (2009)']
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
