from unittest import TestCase
from unittest.mock import patch, Mock

from goodreads_api import GoodreadsQueryAPI

ACCESS_KEY = "test"
USER_ID = "another-test"

class GoodreadsQueryAPITest(TestCase):
    def setUp(self):
        self.gdr = GoodreadsQueryAPI(USER_ID, ACCESS_KEY)

        self.gdr_fixture = ""
        with open('goodreads_api/tests/gdr_fixture.xml', 'r') as f:
            self.gdr_fixture = f.read()

    @patch('requests.get')
    def test_get_books(self, mock_get):
        mock_response = Mock()
        mock_get.return_value = mock_response
        mock_response.content = self.gdr_fixture

        books = self.gdr.get_books()
        self.assertEqual(2, len(books))
        self.assertEqual("9780399590566", books[0]['isbn'])
        self.assertEqual("9780684833392", books[1]['isbn'])
