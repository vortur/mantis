import unittest
from unittest.mock import Mock

from src.usecase.current_generation_usec import CurrentGenerationUseCase


class TestCurrentGenerationUseCase(unittest.TestCase):
    def test_current_generation(self):
        #Mocking part:
        request = {'power':300,'site_id':1,}
        repo = Mock()
        repo.current_generation.return_value = request
        expected_response = {'site_id':1,'power':300}

        #Test usecase:
        use_case = CurrentGenerationUseCase(repo)

        #Test data passed to the repository:
        repo.current_generation.assert_not_called()
