import requests
import json
from configparser import ConfigParser

class API:

    host: str
    api_key: str
    api_session: requests.Session

    @staticmethod
    def setup(self, api_id: str) -> None:
        config = ConfigParser()
        config.read("./assets/config/api.cfg")

        self.host = config.get(api_id, "host")

        self.api_session = requests.Session()
        self.api_session.headers.update({
            "api_key": config.get(api_id, "api_key"),
            "Content-Type": "application/json"
        })
        
        # Retry mechanism
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[500])
        self.api_session.mount('http://', HTTPAdapter(max_retries=retries))
        self.api_session.mount('https://', HTTPAdapter(max_retries=retries))

    @staticmethod
    def put(endpoint:str, payload: dict) -> dict:
        
        response = self.api_session.put(self.host+endpoint,
                json.dumps(payload))

        return json.loads(response.content)['data']
