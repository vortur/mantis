class Test$classUseCaseRepo(unittest.TestCase):
    def test_$methodUseCase(self):
        #Mocking part:
        request = {'id':1}
        repo = MockRepository("$methodUseCase connection string...")

        data = {}
        actual_response = repo.$methodUseCase(data)
        expected_response = "Here is empty $methodUseCase_repository for $classUseCase"
        self.assertEqual(actual_response, expected_response)

