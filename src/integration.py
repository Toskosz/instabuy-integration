from src.api import API

class Integration:

    """
    General representation of a Integration
    """

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def load(self, file_path: str, batch_size: int) -> bool:
        """
        
        Batches data loading function. Defined by the Integration of what
        its loading
        
        Args:
            file_path (str): relative path to file/data source
            batch_size (int): Number os products to load
        Returns:
            bool signaling that data was loaded
        """
        pass

    def payload(self, op: str) -> dict:
        """
        Payload formatting function

        Args:
            op (str): Desired operation/way of formatting
        Returns:
            A dict representing the payload for that operation

        """
        pass

    def update(self, api: str, source: str, batch_size: int) -> None:
        """ Updates data in batches.

        Args:
            api (str): Desired api to update. API ID in config file.
            source (str): Data source
            batch_size (int): Size of batches
        Raises:
            KeyError if response doesn't contain some key used in printing

        """
        batch_count = 0
        with API.conn(api):
            while self.load(source, batch_size):
                batch_count += 1

                response = API.put(endpoint=self.endpoint,
                        payload=self.payload("put"))
                
                print("Batch: %s Status: %s HTTPStatus: %s " % (
                    batch_count,
                    response["status"],
                    response["http_status"]))
                if response["http_status"] >= 200 and response["http_status"] < 300:
                    print("Records: %s Updated: %s Registered: %s " % (
                        response["data"]["count"],
                        response["data"]["updated"],
                        response["data"]["registered"]))
                else:
                    return

