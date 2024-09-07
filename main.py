import os
import sys
import pymongo
import logging
import traceback


def configure_logger() -> None:
    log_level = logging.DEBUG if os.environ.get("DEBUG_MODE", "") else logging.INFO
    logging.basicConfig(
        format=r'%(levelname)s [%(asctime)s]: "%(message)s"',
        datefmt=r'%Y-%m-%d %H:%M:%S', level=log_level
    )


def get_mongo_client(host: str = "127.0.0.1", port: str = "27017", username: str = "root", password: str = "testing") -> pymongo.MongoClient:
    return pymongo.MongoClient(
        host=os.environ.get("MONGO_HOST", host),
        port=int(os.environ.get("MONGO_PORT", port)),
        username=os.environ.get("MONGO_USER", username),
        password=os.environ.get("MONGO_PASS", password)
    )


try:
    configure_logger()
    client = get_mongo_client()

except Exception:
    logging.debug("try/except block of the main")
    logging.error(traceback.format_exc())
    sys.exit(1)
