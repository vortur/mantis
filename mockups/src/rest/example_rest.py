from src.repository.mock_repo import MockRepository
from src.usecase.example_usec import ExampleUseCase


def example_rest(request):
    repo = MockRepository("example connection string...")
    use_case = ExampleUseCase(repo)
    result = use_case.execute(request)

    return str(result)
