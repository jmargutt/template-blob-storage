# template-blob-storage
Template of Dockerized Python application to download/upload data from/to Azure blob storage.

## setup
1. Add the name of your container and the [connection string](https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account) as environment variables (credentials/.env).
2. Add what you need in [pipeline.py:main](https://github.com/jmargutt/template-blob-storage/blob/main/pipeline/src/pipeline/pipeline.py).
3. Install and run locally
```
cd pipeline
pip install .
run-pipeline
```
Or build docker container and push it to Azure Container Registry
```
az acr login -n myregistry
docker build -t myregistry.azurecr.io/template-blob-storage .
docker image push myregistry.azurecr.io/template-blob-storage
```
