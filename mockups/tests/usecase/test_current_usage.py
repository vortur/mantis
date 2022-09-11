import unittest
from unittest.mock import Mock

from src.usecase.current_usage_usec import CurrentUsageUseCase


class TestCurrentUsageUseCase(unittest.TestCase):
    def test_current_usage(self):
        #Mocking part:
        request = {'power':300,'site_id':1,}
        repo = Mock()
        repo.current_usage.return_value = request
        expected_response = {'site_id':1,'power':300}

        #Test usecase:
        use_case = CurrentUsageUseCase(repo)
        
        #Test data passed to the repository:
        repo.current_usage.assert_not_called()
