from src.integration import Integration
from models.product import Product

import csv
import datetime
import locale

class ProductIntegration(Integration):

    def __init__(self) -> None:
        locale.setlocale(locale.LC_ALL, "pt_BR.utf8")
        super().__init__("products")
        self.data = []
        self.file = None
        self.reader = None

    def _file_init(self, file_path: str) -> None:
        self.file = open(file_path, 'r')
        self.reader = csv.reader(self.file, delimiter=';')
        next(self.reader, None)

    def _file_terminate(self) -> None:
        self.file.close()
        self.file = None
        self.reader = None

    def load(self, file_path: str, batch_size: int) -> bool:
        if not self.file:
            self._file_init(file_path)
        
        batch_count = 0
        while batch_count < batch_size:
        
            raw_data = next(self.reader, None)
            if not raw_data:
                break
 
            product = Product()
            product.internal_code = raw_data[0].strip()
            if len(product.internal_code) == 0:
                product.name = "unavailable"

            product.barcode = [raw_data[1].strip()]
            if (len(product.barcode[0]) not in [8,12,13]):
                product.barcode = []

            product.name = raw_data[2].strip()
            if len(product.name) == 0:
                product.name = "unavailable"
            
            try:
                product.price = float(raw_data[3].replace(",", "."))
                product.price = round(product.price, 2)
            except ValueError:
                product.price = 0.0

            try:
                product.stock = float(raw_data[6].replace(",", "."))
                product.stock = round(product.stock, 0)
            except ValueError:
                product.stock = 0.0

            product.visible = raw_data[7].strip().lower()
            if product.visible != "true" and product.visible != "false":
                product.visible = False
            else:
                product.visible = product.visible == "true"

            # Optional attributes
            try:
                product.promo_price = float(raw_data[4].replace(",", "."))
                product.promo_price = round(product.promo_price, 2)
            except ValueError:
                product.promo_price = 0.0

            try:
                product.promo_end_at = datetime.datetime.strptime(raw_data[5].title(), "%d-%b-%y").isoformat()
            except:
                product.promo_end_at = ""

            self.data.append(product)
            batch_count += 1

        # If at least one product was loaded, then it must be sent
        # hence the 'True'
        if batch_count > 0:
            return True
        else:
        # If not even one was loaded then the file is over and theres nothing
        # to send, hence the 'False'
            self._file_terminate()
            return False

    def payload(self, op: str) -> dict:

        if op == "put":
            payload = {
                'products': [product.__dict__ for product in self.data]
            }
            self.data.clear()
            return payload
        else:
            return {}

