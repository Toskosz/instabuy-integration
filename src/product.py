

class ProductIntegration():
    
    def __init__(self, file_path: str, batch_size: int) -> None:
        self.file_path = file_path
        self.batch_size = batch_size
        self.file = open(file_path, 'r', newline='')
        self.reader = csv.reader(self.file, delimiter=';')

    def finish(self) -> None:
        if self.file:
            self.file.close()
            self.file = None

    def load(self):
        pass
