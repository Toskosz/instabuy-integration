from src.integration import Integration
from models.product import Product
import csv

class ProductIntegration(Integration):

    def __init__(self):
        super().__init__("products")
        self.data = []

    def load(self, file_path: str) -> bool:
        if not self.file:
            self._file_init(file_path)

        raw_data = next(self.reader, None)
        if not raw_data:
            self._file_terminate()
            return false
         
        product = Product()
        product.internal_code = raw_data[0]
        if len(product.internal_code) == 0:
            product.name = "unavailable"

        product.barcode = [raw_data[1]]
        if (len(product.barcode[0]) not in [0,8,12,13]):
            product.barcode = []

        product.name = raw_data[2]
        if len(product.name) == 0:
            product.name = "unavailable"
            
        try:
            product.price = float(raw_data[3])
            product.price = round(product.price, 2)
        except ValueError:
            product.price = 0.0

        try:
            product.stock = float(raw_data[6])
            product.stock = round(product.stock, 0)
        except ValueError:
            product.stock = 0.0

        product.visible = raw_data[7]
        if product.visible != "True" and product.visible != "False":
            product.visible = False
        else:
            product.visible = product.visible == "True"

        # Optional attributes
        try:
            product.promo_price = float(raw_data[4])
            product.promo_price = round(product.promo_price, 2)
        except ValueError:
            product.promo_price = 0.0

        # tratar se houver
        product.promo_end_at = raw_data[5]
        
        self.data.append(product)

        return true

    def payload(self, op: str) -> dict:
        # criacao do payload
        self.data.clear()
        pass
