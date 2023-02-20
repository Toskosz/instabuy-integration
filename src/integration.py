from src.api import

class Integration:

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def load(self):
        pass

    def payload(self, op: str):
        pass

    def update(self, file_path="", batch_size=None) -> None:

        while (self.load(file_path)):
            payload = self.payload("put")
            response = API.put(endpoint=self.endpoint, payload=payload)
        
        return

   def _file_init(self, file_path: str) -> None:
        self.file = open(file_path, 'r')
        self.reader = csv.reader(self.file, delimiter=';')

    def _file_terminate(self) -> None:
        self.file.close()
        self.reader = None

