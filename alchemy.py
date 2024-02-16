import json

import requests


class AlchemyAPI:
    def __init__(self, hf_api_key, endpoint_url):
        self.hf_api_key = hf_api_key
        self.endpoint_url = endpoint_url

    def invoke_model(self, inputs, parameters=None):
        headers = {
            "Authorization": f"Bearer {self.hf_api_key}",
            "Content-Type": "application/json"
        }
        data = {"inputs": inputs}
        if parameters is not None:
            data.update({"parameters": parameters})
        response = requests.post(
            self.endpoint_url,
            headers=headers,
            data=json.dumps(data)
        )
        try:
            response_data = json.loads(response.content.decode("utf-8", errors="ignore"))
            return response_data
        except json.JSONDecodeError:
            return response.content