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

2. Switch to the newly created blob-quickstart-v12 directory.
    ```bash
    cd blob-quickstart-v12
    ```

3. In side the blob-quickstart-v12 directory, create another directory called data. This directory is where the blob data files will be created and stored.
    
    ```bash
    mkdir data
    ```


