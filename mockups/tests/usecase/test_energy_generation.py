import unittest
from unittest.mock import Mock
from src.entity.energy_generation_enti import EnergyGeneration

from src.usecase.energy_generation_usec import EnergyGenerationUseCase


class TestEnergyGenerationUseCase(unittest.TestCase):
    def test_energy_generation(self):
        #Mocking part:
        request = {"site_id":1,"kvp":3.3}
        repo = Mock()
        repo.energy_generation.return_value="Here is energy_generation_repository for EnergyGenerationUseCase"
        expected_response = "Here is energy_generation_repository for EnergyGenerationUseCase"

        #Test usecase:
        use_case = EnergyGenerationUseCase(repo)
        actual_response = use_case.execute(request)
        self.assertEqual(actual_response, expected_response)

        #Test data passed to the repository:
        repo.energy_generation.assert_called()
        repo.energy_generation.assert_called_with({"site_id":1,"kvp":3.3})
