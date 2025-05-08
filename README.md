# simple-deepseek
Simple deepseekAPI client

## Your simple async and sync DeepSeek client
![image info](./pictures/deepseek.png)

## Installation

You can install the package using pip:

```bash
pip install simple-deepseek
```

Or install directly from the source:

```bash
git clone https://github.com/yourusername/simple-deepseek.git
cd simple-deepseek
pip install -e .
```

## Requirements

- Python 3.7+
- requests
- aiohttp (for async support)

## Usage

```python
from simple_deepseek import DeepSeekClient

# Initialize the client
client = DeepSeekClient(api_key="your-api-key")

# Synchronous request
response = client.send_request(
    message="What is Python?"
)

# Asynchronous request
response = await client.send_request_async(
    message="What is Python?"
)
```
