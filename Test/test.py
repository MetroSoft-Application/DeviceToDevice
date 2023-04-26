import os
import unittest
from azure.functions import HttpRequest
from DeviceToDevice import main

os.environ["IOTHUB_DEVICE_CONNECTION_STRING"] = ""
os.environ["DEVICE_ID"] = ""


class TestFunction(unittest.TestCase):
    def test_main(self):
        req = HttpRequest(
            method="POST",
            url="http://localhost:7071/api/",
            headers={"Content-Type": "application/json"},
            body=b'{"message": "Test message"}'
        )

        response = main(req)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_body(),
                         b"Message sent to target device.")


if __name__ == "__main__":
    unittest.main()
