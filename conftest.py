import pytest

@pytest.fixture(autouse=True)
def run_http_server(simplehttpserver):
    pass