from unittest import TestCase
from unittest.mock import patch, Mock

from goodreads_api import GoodreadsQueryAPI

ACCESS_KEY = "test"
USER_ID = "another-test"

GOODREADS_QUERY_URL = "https://www.goodreads.com/review/list?v=2&key={access_key}&id={user_id}&shelf=to-read&per_page=200&sort=position"

"""
    Tests for the GoodreadsQueryAPI class. This tests only the happy path
    for now, since we do not really do any error handling in there
"""
class GoodreadsQueryAPITest(TestCase):
    def setUp(self):
        self.gdr = GoodreadsQueryAPI(USER_ID, ACCESS_KEY)

        self.gdr_fixture = ""
        with open('goodreads_api/tests/gdr_fixture.xml', 'r') as f:
            self.gdr_fixture = f.read()

        get_patcher = patch('requests.get')
        self.addCleanup(get_patcher.stop)
        self.mock_get = get_patcher.start()

        mock_response = Mock()
        self.mock_get.return_value = mock_response
        mock_response.content = self.gdr_fixture


    def test_get_books(self):
        books = self.gdr.get_books()
        self.assertEqual(2, len(books))
        self.assertEqual("9780399590566", books[0]['isbn'])
        self.assertEqual("9780684833392", books[1]['isbn'])

        self.mock_get.assert_called_once_with(GOODREADS_QUERY_URL.format(
            access_key=ACCESS_KEY, user_id=USER_ID))
