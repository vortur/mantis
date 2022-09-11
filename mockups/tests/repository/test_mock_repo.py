import unittest
import random
from datetime import datetime
import time

from src.entity.energy_generation_enti import EnergyGeneration

from src.repository.mock_repo import MockRepository

def isTimeFormat(input):
    try:
        time.strptime(input, f"%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False
class TestExampleRepo(unittest.TestCase):
    def test_example(self):
        #Mocking part:
        repo = MockRepository("Example connection string...")

        data = {}
        actual_response = repo.example(data)
        expected_response = "Here is example_repository for ExampleUseCase"
        self.assertEqual(actual_response, expected_response)

class TestEnergyGenerationUseCaseRepo(unittest.TestCase):
    def test_energy_generation(self):
        #Mocking part:
        repo = MockRepository("energy_generation connection string...")

        rand_site_id = random.randint(0, 999)
        data = {"site_id":rand_site_id,"kvp":3.3}
        actual_responses = repo.energy_generation(data)

        for response in actual_responses:
            self.assertEqual(response.site_id, rand_site_id)
            self.assertTrue(isTimeFormat(response.from_time))
            self.assertTrue(isTimeFormat(response.to_time))
            self.assertTrue(type(response.energy) == int)

class TestEnergyUsageUseCaseRepo(unittest.TestCase):
    def test_energy_usage(self):
        #Mocking part:
        repo = MockRepository("energy_usage connection string...")

        rand_site_id = random.randint(0, 999)
        data = {"site_id":rand_site_id,"kw_max":3.3}
        actual_responses = repo.energy_usage(data)

        for response in actual_responses:
            self.assertEqual(response.site_id, rand_site_id)
            self.assertTrue(isTimeFormat(response.from_time))
            self.assertTrue(isTimeFormat(response.to_time))
            self.assertTrue(type(response.energy) == int)

class TestCurrentUsageUseCaseRepo(unittest.TestCase):
    def test_current_usage(self):
        #Mocking part:
        repo = MockRepository("current_usage connection string...")

        data = {'site_id':1,'power':300}
        actual_response = repo.current_usage(data)
        expected_response = "current_usage - not used with repository"
        self.assertEqual(actual_response, expected_response)

class TestCurrentGenerationUseCaseRepo(unittest.TestCase):
    def test_current_generation(self):
        #Mocking part:
        repo = MockRepository("current_generation connection string...")

        data = {'site_id':1,'power':300}
        actual_response = repo.current_generation(data)
        expected_response = "current_generation - not used with repository"
        self.assertEqual(actual_response, expected_response)

