import dataclasses, json, requests, logging
from src.repository.mock_repo import MockRepository
from src.usecase.current_generation_usec import CurrentGenerationUseCase


def current_generation_rest(request):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    repo = MockRepository("example connection string...")
    use_case = CurrentGenerationUseCase(repo)
    result = use_case.execute(request)

    request_json = {"data": result}
    req = requests.post("http://localhost:1337/api/current-generations", json = request_json, headers=headers)

    return {"data": request_json, "resp":str(req)}
