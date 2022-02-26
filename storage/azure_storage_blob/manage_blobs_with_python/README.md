# Manage blobs with Python v12 SDK
In this quickstart, you learn to manage blobs by using Python. Blobs are objects that can hold large amounts of text or binary data, including images, documents, streaming media, and archive data. You'll upload, download, and list blobs, and you'll create and delete containers.

## Setting up
This section walks you through preparing a project to work with the Azure Blob Storage client library v12 for Python.

### Create the project
Create a Python application named *blob-quickstart-v12*.

1. In a console window (such as cmd, PowerShell, or Bash), create a new directory for the project.

    ```bash
    mkdir blob-quickstart-v12
    ```

2. Switch to the newly *created blob-quickstart-v12* directory.
    ```bash
    cd blob-quickstart-v12
    ```

3. In side the *blob-quickstart-v12 directory*, create another directory called *data*. This directory is where the blob data files will be created and stored.
    
    ```bash
    mkdir data
    ```

### Install the package
While still in the application directory, install the Azure Blob Storage client library for Python package by using the `pip install` command.

```bash
pip install azure-storage-blob
```

This command installs the Azure Blob Storage client library for Python package and all the libraries on which it depends. In this case, that is just the Azure core library for Python.

### Set up the app framework
From the project directory:

1. Open a new text file in your code editor
2. Add `import` statements
3. Create the structure for the program, including basic exception handling
    Here's the code:
    
    ```python
    import os, uuid
    from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

        # Quick start code goes here

    except Exception as ex:
        print('Exception:')
        print(ex)
    ```
    
4. Save the new file as *blob-quickstart-v12.py* in the *blob-quickstart-v12* directory.

### Copy your credentials from the Azure portal
When the sample application makes a request to Azure Storage, it must be authorized. To authorize a request, add your storage account credentials to the application as a connection string. To view your storage account credentials, follow these steps:

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Locate your storage account.
3. In the storage account menu pane, under **Security + networking**, select **Access keys**. Here, you can view the account access keys and the complete connection string for each key.

4. In the **Access keys** pane, select **Show keys**.
5. In the **key1** section, locate the **Connection string** value. Select the **Copy to clipboard** icon to copy the connection string. You will add the connection string value to an environment variable in the next section.


    ![Access keys](assets/storage-account-access-key.png)

### Configure your storage connection string
After you copy the connection string, write it to a new environment variable on the local machine running the application. To set the environment variable, open a console window, and follow the instructions for your operating system. Replace `<yourconnectionstring>` with your actual connection string.

### Linux
```bash
export AZURE_STORAGE_CONNECTION_STRING="<yourconnectionstring>"
```

### Restart programs
After you add the environment variable, restart any running programs that will need to read the environment variable. For example, restart your development environment or editor before you continue.

## Object model
Azure Blob Storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that doesn't adhere to a particular data model or definition, such as text or binary data. Blob storage offers three types of resources:

- The storage account
- A container in the storage account
- A blob in the container

The following diagram shows the relationship between these resources.

![Blob storage](assets/blob-storage-structure.png)


Use the following Python classes to interact with these resources:

- [BlobServiceClient](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient): The `BlobServiceClient` class allows you to manipulate Azure Storage resources and blob containers.
- [ContainerClient](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient): The `ContainerClient` class allows you to manipulate Azure Storage containers and their blobs.
- [BlobClient](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobclient): The `BlobClient` class allows you to manipulate Azure Storage blobs.

## Code examples
These example code snippets show you how to do the following tasks with the Azure Blob Storage client library for Python:

- [Get the connection string](#get-the-connection-string)
- [Create a container](#create-a-container)
- [Upload blobs to a container](#upload-blobs-to-a-container)
- [List the blobs in a container](#list-the-blobs-in-a-container)
- [Download blobs](#download-blobs)
- [Delete a container](#delete-a-container)

### Get the connection string
The code below retrieves the storage account connection string from the environment variable created in the [Configure your storage connection string](#configure-your-storage-connection-string) section.

Add this code inside the `try` block:

```bash
# Retrieve the connection string for use with the application. The storage
# connection string is stored in an environment variable on the machine
# running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
# created after the application is launched in a console or with Visual Studio,
# the shell or application needs to be closed and reloaded to take the
# environment variable into account.
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
```

### Create a container
Decide on a name for the new container. The code below appends a UUID value to the container name to ensure that it's unique.

> **Important**: Container names must be lowercase.

Create an instance of the [BlobServiceClient](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient) class by calling the [from_connection_string](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient#from-connection-string-conn-str--credential-none----kwargs-) method. Then, call the [create_container](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient#create-container-name--metadata-none--public-access-none----kwargs-) method to actually create the container in your storage account.

Add this code to the end of the `try` block:

```bash
# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Create a unique name for the container
container_name = str(uuid.uuid4())

# Create the container
container_client = blob_service_client.create_container(container_name)
```




### Upload blobs to a container


### List the blobs in a container


### Download blobs


### Delete a container


