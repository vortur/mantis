import unittest
from unittest.mock import Mock

from src.usecase.$methodUseCase_usec import $classUseCase


class Test$classUseCase(unittest.TestCase):
    def test_$methodUseCase(self):
        #Mocking part:
        request = {'id':1}
        repo = Mock()
        repo.$methodUseCase.return_value="Here is $methodUseCase_repository for $classUseCase"
        expected_response = "Here is $methodUseCase_repository for $classUseCase"

        #Test usecase:
        use_case = $classUseCase(repo)
        actual_response = use_case.execute(request)
        self.assertEqual(actual_response, expected_response)

        #Test data passed to the repository:
        repo.$methodUseCase.assert_called()
        repo.$methodUseCase.assert_called_with({'id':1})
