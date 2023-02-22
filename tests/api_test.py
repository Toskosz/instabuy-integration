import unittest
from src.api import API

class TestAPI(unittest.TestCase):
    maxDiff = None

    def test_setup(self):
        API.setup("test")

        desired_headers = {
                "api-key": "123",
                "Content-Type": "application/json"
        }

        self.assertEqual(API.host, "https://httpbin.org/")
        self.assertEqual(API.api_session.headers["api-key"], desired_headers["api-key"])
        self.assertEqual(API.api_session.headers["Content-Type"], desired_headers["Content-Type"])

    def test_put(self):
        data = {
            "key": "value",
        }

        API.setup("test")
        response = API.put("put", data)
        response = API.put("put", data)
        self.assertEqual(response["url"], "https://httpbin.org/put")

if __name__ == '__main__':
    unittest.main()

