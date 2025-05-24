from aioresponses import aioresponses
from requests_mock import Mocker
from simple_mistral.client import MistralClient
from tests.testdata import API_KEY, MESSAGE


class PrepareScenarioBuilder:
    def __init__(self) -> None:
        ...

    def send_request(self, mock: Mocker) -> MistralClient:
        mock.post(
            url=f'https://api.mistral.ai/v1/chat/completions',
            json={'choices': [{'message': {'content': MESSAGE}}]},
        )
        return MistralClient(api_key=API_KEY)

    async def send_async_request(self, mock: aioresponses) -> MistralClient:
        mock.post(
            url=f'https://api.mistral.ai/v1/chat/completions',
            status=200,
            payload={'choices': [{'message': {'content': MESSAGE}}]},
        )
        return MistralClient(api_key=API_KEY)
