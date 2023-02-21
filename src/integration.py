from src.api import

class Integration:

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def load(self, file_path: str, batch_size: int) -> bool:
        pass

    def payload(self, op: str) -> dict:
        pass

    def update(self, file_path="", batch_size=None) -> None:
        while self.load(file_path, batch_size):
            response = API.put(endpoint=self.endpoint, payload=self.payload("put"))
            # TODO: Fazer alguma coisa com resposta, print talvez
