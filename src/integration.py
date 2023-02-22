from src.api import API

class Integration:

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def load(self, file_path: str, batch_size: int) -> bool:
        pass

    def payload(self, op: str) -> dict:
        pass

    def update(self, file_path: str, batch_size: int) -> None:
        batch_count = 0
        with API.conn("instabuy"):
            while self.load(file_path, batch_size):
                batch_count += 1
                response = API.put(endpoint=self.endpoint, payload=self.payload("put"))
                print("Batch: %s Status: %s HTTPStatus: %s " % (batch_count,response["status"],response["http_status"]))
                print("Records: %s Updated: %s Registered: %s " % (response["data"]["count"],response["data"]["update"],response["data"]["registered"]))

