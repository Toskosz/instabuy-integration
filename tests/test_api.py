import unittest
from src.api import API

class TestAPI(unittest.TestCase):
    maxDiff = None

    def test_setup(self):
        desired_headers = {
                "api-key": "123",
                "Content-Type": "application/json"
        }

        with API("test") as api_conn:
            self.assertEqual(api_conn.host, "https://httpbin.org/")
            self.assertEqual(api_conn.api_session.headers["api-key"], desired_headers["api-key"])
            self.assertEqual(api_conn.api_session.headers["Content-Type"], desired_headers["Content-Type"])

    def test_put(self):
        data = {
            "key": "value",
        }

        with API("test") as api_conn:
            response = api_conn.put("put", data)
            self.assertEqual(response["url"], "https://httpbin.org/put")

if __name__ == '__main__':
    unittest.main()

