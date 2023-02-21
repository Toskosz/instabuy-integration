import unittest
from src.integrations.product import ProductIntegration
from models.product import Product

class TestProductIntegration(unittest.TestCase):

    maxDiff = None

    def test_load(self):
        target_p = Product()
        target_p.internal_code = "11902"
        target_p.barcode = ["7898646710031"]
        target_p.name = "ACQUISSIMA Passion Natural 1,5L Com Gás"
        target_p.price = 85.72
        target_p.promo_price = 2.99
        target_p.promo_end_at = "2022-12-31T00:00:00" 
        target_p.stock = 148.00
        target_p.visible = False


        p = ProductIntegration()
        p.load("./assets/data/test.csv",1)
        p._file_terminate()

        test_p = p.data[0]

        # verificar tamanho de p.date = 1
        self.assertEqual(len(p.data), 1)
        self.assertEqual(target_p.internal_code, test_p.internal_code)
        self.assertEqual(target_p.barcode, test_p.barcode)
        self.assertEqual(target_p.name, test_p.name)
        self.assertEqual(target_p.price, test_p.price)
        self.assertEqual(target_p.promo_price, test_p.promo_price)
        self.assertEqual(target_p.promo_end_at, test_p.promo_end_at)
        self.assertEqual(target_p.stock, test_p.stock)
        self.assertEqual(target_p.visible, test_p.visible)


    def test_payload(self):
        correct_payload = {
                "products":[
                    {
                        "internal_code": "11902",
                        "barcode": ["7898646710031"],
                        "name": "ACQUISSIMA Passion Natural 1,5L Com Gás",
                        "price": 85.72,
                        "promo_price": 2.99,
                        "promo_end_at": "2022-12-31T00:00:00",
                        "stock": 148.00,
                        "visible": False
                    },
                    {
                        "internal_code": "12902",
                        "barcode": [],
                        "name": "ALIM PASSARO FORTE 500g PAPAGAIO",
                        "price": 14.96,
                        "promo_price": 8.90,
                        "promo_end_at": "2022-12-31T00:00:00",
                        "stock": 447.00,
                        "visible": False
                    }
                ]
        }

        p = ProductIntegration()
        while p.load("./assets/data/test.csv", 2):
            payload = p.payload("put")

        self.assertDictEqual(correct_payload, payload)

if __name__ == '__main__':
    unittest.main()
