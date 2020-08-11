import logging
import os
import boto3

# logging
LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)
root_logger = logging.getLogger()
root_logger.setLevel(LOG_LEVEL)
log = logging.getLogger(__name__)


def handler(event, context):
    log.debug("Received event {}".format(event))
    log.info("Lambda executed")
    return {"Response": f"Sucessfully executed Scenario 2 Lambda task 1!"}
