from src.repository.sqlite_repo import SqliteRepository
from src.usecase.example_sqlite_usec import ExampleSqliteUseCase



def example_sqlite_rest(request):
    repo = SqliteRepository("sqlite.db")
    use_case = ExampleSqliteUseCase(repo)
    result = use_case.execute(request)

    return result
