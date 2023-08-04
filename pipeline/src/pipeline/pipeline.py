import datetime
import requests
import pandas as pd
import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
import click
import logging
logging.root.handlers = []
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG, filename='ex.log')
# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)
load_dotenv(dotenv_path="../credentials/.env")


def get_blob_service_client(blob_path, container):
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv("CONNECTION"))
    return blob_service_client.get_blob_client(container=container, blob=blob_path)


def upload_file(container, file_path='messages.csv', blob_path='messages.csv'):
    # upload file to azure blob storage
    blob_client = get_blob_service_client(blob_path, container)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)


def download_file(container, file_path='messages.csv', blob_path='messages.csv'):
    # download file from azure blob storage
    blob_client = get_blob_service_client(blob_path, container)
    with open(file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())


def list_files(container, blob_service_client: BlobServiceClient, container_name):
    # list files in azure blob storage container
    container_client = blob_service_client.get_container_client(container)
    blob_list = container_client.list_blobs()
    return [f"{blob.name}" for blob in blob_list]


@click.command()
def main():
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    container = os.getenv('CONTAINER')

    download_file(container, 'local_directory/local_file.csv', 'blob_directory/blob_file.csv')
    # do stuff
    # ...
    #
    upload_file(container, 'local_directory/local_file.csv', 'blob_directory/blob_file.csv')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)


if __name__ == "__main__":
    main()

