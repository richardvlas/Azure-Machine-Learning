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



