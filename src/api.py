import requests
import json
from configparser import ConfigParser
from requests.adapters import HTTPAdapter, Retry

class API:

    """

    API Class to manage configurations and requests

    """

    def __init__(self, api_id: str) -> None:
        """ Creates API Session

        Creates API connection through a Session objects

        Args:
            api_id (str): id used to get the API configurations in config file
        """
        config = ConfigParser()
        config.read("./assets/config/api.cfg")

        self.host = config.get(api_id, "host")

        self.api_session = requests.Session()
        self.api_session.headers = {
            "api-key": config.get(api_id, "api_key"),
            "Content-Type": "application/json"
        }
        
        # Retry mechanism
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[500])
        self.api_session.mount('http://', HTTPAdapter(max_retries=retries))
        self.api_session.mount('https://', HTTPAdapter(max_retries=retries))

    def __enter__(self) -> requests.Session:
        """ Manages API connection

        Manages the API connection Session object

        """
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        """ Closes API connection

        Closes Session objection when API connection is finished
        
        Args:
            exception_type: indicates class of exception.
            exception_value: ndicates type of exception. like divide_by_zero 
            error, floating_point_error, which are types of arithmetic exception.
            exception_tracebacka: traceback is a report which has all of the
            information needed to solve the exception.

        """
        self.api_session.close()

    def put(self, endpoint:str, payload: dict) -> dict:
        """ Makes put request to API

        Args:
            endpoint (str): Desired API endpoint
            payload (dict): Payload of the request
        Returns:
            A dict containing the response contents of the request

        """
        
        response = self.api_session.put(self.host+endpoint,
                json.dumps(payload))
        
        return json.loads(response.content)

