import unittest
from unittest.mock import Mock

from src.usecase.example_usec import ExampleUseCase


class TestExampleUseCase(unittest.TestCase):
    def test_example(self):
        #Mocking part:
        request = {'id':1}
        repo = Mock()
        repo.example.return_value="Here is example_repository for ExampleUseCase"
        expected_response = "Here is example_repository for ExampleUseCase"

        #Test usecase:
        use_case = ExampleUseCase(repo)
        actual_response = use_case.execute(request)
        self.assertEqual(actual_response, expected_response)

        #Test data passed to the repository:
        repo.example.assert_called()
        repo.example.assert_called_with({'id':1})
