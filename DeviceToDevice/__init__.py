import logging
import azure.functions as func
import json
from azure.iot.hub import IoTHubRegistryManager

CONNECTION_STRING = ""
DEVICE_ID = ""


def main(req: func.HttpRequest) -> func.HttpResponse:
    print("test")
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Get message from request
        req_body = req.get_json()
        message = req_body.get('message')

        # Send message to target device
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
        registry_manager.send_c2d_message(DEVICE_ID, message)

        return func.HttpResponse("Message sent to target device.", status_code=200)

    except Exception as e:
        logging.error("Error: %s", e)
        return func.HttpResponse("Error sending message to target device.", status_code=500)
