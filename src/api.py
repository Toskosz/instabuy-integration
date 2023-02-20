import requests
import json

class API:

    host: str
    api_key: str
    api_session: requests.Session

    @staticmethod
    def setup(self):
        self.api_session = requests.Session()
        # Retry mechanism
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[500])
        self.api_session.mount('http://', HTTPAdapter(max_retries=retries))

    @staticmethod
    def put(endpoint:str, payload: dict) -> dict:
        
        response = requests.put(self.host+endpoint,
                json.dumps(payload), headers=self.headers)

        return json.loads(response.content)['data']
