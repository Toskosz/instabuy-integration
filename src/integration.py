from src.api import

class Integration:

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
        self.file = None
        self.reader = None

    def load(self):
        pass

    def payload(self, op: str):
        pass

    def update(self, file_path="", batch_size=None) -> None:

        batch_count = 0
        while(self.load(file_path)):
            batch_count += 1
            if batch_count >= batch_size:
                payload = self.payload("put")
                response = API.put(endpoint=self.endpoint, payload=self.payload("put"))
                batch_count = 0
        
        # The last batch's size may be less then batch_size
        # TODO: If last one is empty
        response = API.put(endpoint=self.endpoint, payload=self.payload("put"))



   def _file_init(self, file_path: str) -> None:
        self.file = open(file_path, 'r')
        self.reader = csv.reader(self.file, delimiter=';')

    def _file_terminate(self) -> None:
        self.file.close()
        self.file = None
        self.reader = None

