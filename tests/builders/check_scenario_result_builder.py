from tests.testdata import MESSAGE


class CheckScenarioBuilder:
    def __init__(self) -> None:
        ...

    def send_request(self, response: str) -> None:
        assert response == MESSAGE

    async def send_async_request(self, response: str) -> None:
        assert response == MESSAGE
