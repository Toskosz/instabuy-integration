import requests
import json
from configparser import ConfigParser
from requests.adapters import HTTPAdapter, Retry
from contextlib import contextmanager

class API:

    """

    API Class to manage configurations and requests

    """

    host: str

    @contextmanager
    def conn(api_id: str) -> None:
        """ Manages API connection

        Creates and manages the API connection through a Session objects

        Args:
            api_id (str): id used to get the API configurations in config file
            
        """
        config = ConfigParser()
        config.read("./assets/config/api.cfg")

        API.host = config.get(api_id, "host")

        API.api_session = requests.Session()
        API.api_session.headers = {
            "api-key": config.get(api_id, "api_key"),
            "Content-Type": "application/json"
        }
        
        # Retry mechanism
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[500])
        API.api_session.mount('http://', HTTPAdapter(max_retries=retries))
        API.api_session.mount('https://', HTTPAdapter(max_retries=retries))

        try:
            yield
        finally:
            API.api_session.close()

    @staticmethod
    def put(endpoint:str, payload: dict) -> dict:
        """ Makes put request to API

        Args:
            endpoint (str): Desired API endpoint
            payload (dict): Payload of the request
        Returns:
            A dict containing the response contents of the request

        """
        
        try:
            response = API.api_session.put(API.host+endpoint,
                    json.dumps(payload))
        except Exception as e:
            print(e)

        
        return json.loads(response.content)

