from src.integration import Integration

class ProductIntegration(Integration):

    def __init__(self):
        self.endpoint = "products"

    def load(self, file_path: str) -> None:
        pass
