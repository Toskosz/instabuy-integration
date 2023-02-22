import unittest
from src.api import API

class TestAPI(unittest.TestCase):
    maxDiff = None

    def test_setup(self):
        desired_headers = {
                "api-key": "kUs5p-K-sIOMT_hfg2FOYFie7iqRD2pn47jfvPQElLQ",
                "Content-Type": "application/json"
        }
        with API.conn("instabuy"):
            self.assertEqual(API.host, "https://api.instabuy.com.br/store/")
            self.assertEqual(API.api_session.headers["api-key"], desired_headers["api-key"])
            self.assertEqual(API.api_session.headers["Content-Type"], desired_headers["Content-Type"])

    def test_put(self):
        data = {
            "key": "value",
        }

        with API.conn("test"):
            response = API.put("put", data)
            self.assertEqual(response["url"], "https://httpbin.org/put")

if __name__ == '__main__':
    unittest.main()

