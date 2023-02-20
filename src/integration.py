

class Integration():

    def load(self):
        pass

    def payload(self, op: str):
        pass

    def update(self, file_path="", batch_size=None) -> None:

        counter = 0
        for row in self.load(file_path):
            counter += 1

            if batch_size <= counter:
                counter = 0
                payload = self.payload("put")
                response = API.put(endpoint=self.endpoint, payload=self.payload)
                self.payload.clear()

        if len(self.payload) > 0:
            response = API.put(endpoint=self.endpoint, payload=self.payload)
            self.payload.clear()
        
        return

    def create():
        pass

    def delete():
        pass

    def read():
        pass

