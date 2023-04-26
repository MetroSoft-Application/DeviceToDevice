import os
import logging
import azure.functions as func
import json
from azure.iot.hub import IoTHubRegistryManager

CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
DEVICE_ID = os.getenv("DEVICE_ID")


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        message = req_body.get('message')

        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
        registry_manager.send_c2d_message(DEVICE_ID, message)

        return func.HttpResponse("Message sent to target device.", status_code=200)

    except Exception as e:
        logging.error("Error: %s", e)
        return func.HttpResponse("Error sending message to target device.", status_code=500)
