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
The following code snippet:

1. Creates a local directory to hold data files.
2. Creates a text file in the local directory.
3. Gets a reference to a [BlobClient](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobclient) object by calling the [get_blob_client](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient#get-blob-client-blob--snapshot-none-) method on the [BlobServiceClient](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient) from the [Create a container](#create-a-container) section.
4. Uploads the local text file to the blob by calling the [upload_blob](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobclient#upload-blob-data--blob-type--blobtype-blockblob---blockblob----length-none--metadata-none----kwargs-) method.
Add this code to the end of the `try` block:

```bash
# Create a local directory to hold blob data
local_path = "./data"
os.mkdir(local_path)

# Create a file in the local data directory to upload and download
local_file_name = str(uuid.uuid4()) + ".txt"
upload_file_path = os.path.join(local_path, local_file_name)

# Write text to the file
file = open(upload_file_path, 'w')
file.write("Hello, World!")
file.close()

# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

# Upload the created file
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)
```

### List the blobs in a container
List the blobs in the container by calling the [list_blobs](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient#list-blobs-name-starts-with-none--include-none----kwargs-) method. In this case, only one blob has been added to the container, so the listing operation returns just that one blob.

Add this code to the end of the `try` block:

```bash
print("\nListing blobs...")

# List the blobs in the container
blob_list = container_client.list_blobs()
for blob in blob_list:
    print("\t" + blob.name)
```

### Download blobs
Download the previously created blob by calling the [download_blob](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobclient#download-blob-offset-none--length-none----kwargs-) method. The example code adds a suffix of "DOWNLOAD" to the file name so that you can see both files in local file system.

Add this code to the end of the `try` block:

```bash
# Download the blob to a local file
# Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
print("\nDownloading blob to \n\t" + download_file_path)

with open(download_file_path, "wb") as download_file:
    download_file.write(blob_client.download_blob().readall())
```

### Delete a container
The following code cleans up the resources the app created by removing the entire container using the [delete_container](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient#delete-container---kwargs-) method. You can also delete the local files, if you like.

The app pauses for user input by calling `input()` before it deletes the blob, container, and local files. Verify that the resources were created correctly, before they're deleted.

Add this code to the end of the `try` block:

```bash
# Clean up
print("\nPress the Enter key to begin clean up")
input()

print("Deleting blob container...")
container_client.delete_container()

print("Deleting the local source and downloaded files...")
os.remove(upload_file_path)
os.remove(download_file_path)
os.rmdir(local_path)

print("Done")
```

## Run the code
This app creates a test file in your local folder and uploads it to Azure Blob Storage. The example then lists the blobs in the container, and downloads the file with a new name. You can compare the old and new files.

Navigate to the directory containing the *blob-quickstart-v12.py* file, then execute the following `python` command to run the app.

```bash
python blob-quickstart-v12.py
```

The output of the app is similar to the following example:

```bash
Azure Blob Storage v12 - Python quickstart sample

Uploading to Azure Storage as blob:
        cf275796-2188-4057-b6fb-038352e35038.txt

Listing blobs...
        cf275796-2188-4057-b6fb-038352e35038.txt

Downloading blob to
        ./data/cf275796-2188-4057-b6fb-038352e35038DOWNLOAD.txt

Press the Enter key to begin clean up

Deleting blob container...
Deleting the local source and downloaded files...
Done
```

Before you begin the cleanup process, check your *data* folder for the two files. You can open them and observe that they're identical.

After you've verified the files, press the Enter key to delete the test files and finish the demo.
