from pydoc import describe
import unittest
from unittest.mock import Mock

from src.entity.example_sqlite_enti import ExampleSqlite
from src.usecase.example_sqlite_usec import ExampleSqliteUseCase


class TestExampleSqliteUseCase(unittest.TestCase):
    def test_example(self):
        #Mocking part:
        request = {'id':1}
        repo = Mock()
        repo.example_sqlite.return_value=ExampleSqlite(id=1,description="example_sqlite_test")
        expected_response = ExampleSqlite(id=1,description="example_sqlite_test")

        #Test usecase:
        use_case = ExampleSqliteUseCase(repo)
        actual_response = use_case.execute(request)
        self.assertEqual(actual_response, expected_response)

        #Test data passed to the repository:
        repo.example_sqlite.assert_called()
        repo.example_sqlite.assert_called_with({'id':1})
