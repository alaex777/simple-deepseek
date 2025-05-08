from typing import Optional, Dict, Any


class DeepSeekClient:
    """A client for interacting with the DeepSeek API."""
    
    BASE_URL = "https://api.deepseek.com/v1"
    
    def __init__(self, api_key: str, base_url: Optional[str] = None):
        """
        Initialize the DeepSeek client.
        
        Args:
            api_key (str): Your DeepSeek API key
            base_url (str, optional): Custom base URL for the API. Defaults to the official DeepSeek API URL.
        """
        self.api_key = api_key
        self.base_url = base_url or self.BASE_URL
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def send_request(self, message: str, **kwargs) -> Dict[str, Any]:
        """
        Send a synchronous request to the DeepSeek API.
        
        Args:
            message (str): The message to send to the API
            **kwargs: Additional parameters to pass to the API
            
        Returns:
            Dict[str, Any]: The API response
        """

        import requests

        url = f"{self.base_url}/chat/completions"

        payload = {
            "messages": [{"role": "user", "content": message}],
            **kwargs
        }

        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    async def send_request_async(self, message: str, **kwargs) -> Dict[str, Any]:
        """
        Send an asynchronous request to the DeepSeek API.
        
        Args:
            message (str): The message to send to the API
            **kwargs: Additional parameters to pass to the API
            
        Returns:
            Dict[str, Any]: The API response
        """

        import aiohttp

        url = f"{self.base_url}/chat/completions"

        payload = {
            "messages": [{"role": "user", "content": message}],
            **kwargs
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=payload) as response:
                response.raise_for_status()
                return await response.json()
