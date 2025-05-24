from simple_mistral.client import MistralClient
from tests.testdata import MESSAGE


class CallScenarioBuilder:
    def __init__(self) -> None:
        ...

    def send_request(self, client: MistralClient) -> str:
        return client.send_request(message=MESSAGE)

    async def send_async_request(self, client: MistralClient) -> str:
        return await client.send_request_async(message=MESSAGE)

