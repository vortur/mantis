import dataclasses, json, requests, logging
from src.repository.mock_repo import MockRepository
from src.usecase.energy_usage_usec import EnergyUsageUseCase


def energy_usage_rest(request):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    repo = MockRepository("example connection string...")
    use_case = EnergyUsageUseCase(repo)
    results = use_case.execute(request)

    responses=[]

    for result in results:
        result_json = dataclasses.asdict(result)
        request_json = {"data": result_json}
        req = requests.post("http://localhost:1337/api/energy-usages", json = request_json, headers=headers)
        responses.append({"data": result_json, "resp":str(req)})

    return responses
