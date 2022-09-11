from src.repository.mock_repo import MockRepository
from src.usecase.$methodUseCase_usec import $classUseCase


def $methodUseCase_rest(request):
    repo = MockRepository("example connection string...")
    use_case = $classUseCase(repo)
    result = use_case.execute(request)

    return str(result)
