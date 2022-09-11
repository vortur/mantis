import unittest
from unittest.mock import Mock

from src.usecase.energy_usage_usec import EnergyUsageUseCase


class TestEnergyUsageUseCase(unittest.TestCase):
    def test_energy_usage(self):
        #Mocking part:
        request = {"site_id":1,"kw_max":5.8}
        repo = Mock()
        repo.energy_usage.return_value="Here is energy_generation_repository for EnergyUsageUseCase"
        expected_response = "Here is energy_generation_repository for EnergyUsageUseCase"

        #Test usecase:
        use_case = EnergyUsageUseCase(repo)
        actual_response = use_case.execute(request)
        self.assertEqual(actual_response, expected_response)

        #Test data passed to the repository:
        repo.energy_usage.assert_called()
        repo.energy_usage.assert_called_with({"site_id":1,"kw_max":5.8})