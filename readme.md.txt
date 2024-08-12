running modules
Follow these steps to run the File Uploader Module.

Prepare a directory with files:

Create a folder and upload some sample files. You can add images (such as .jpg or .png), media files (such as .mp4), and documents (such as .pdf or .docx).
Run the module:

Type the following command on the terminal or command prompt.
Bush
Copy the code
file-uploader access_to_your_test_folder
Replace path_to_your_test_folder with the actual path to the folder where your files are stored.
What happens next?
The module will search your folder and its subfolders for files.
It will "upload" images and media files to AWS S3 and "upload" documents to Google Cloud Storage (remember, this is just fake; there's no real upload).
You will see a message in the terminal indicating where each file has been "uploaded".
Settings for:
If you want to exchange files that go into AWS S3 or Google Cloud Storage, you can do so easily:

Open config.py file:

This file is located in the file_uploader/file_uploader folder.
Change the file extension:

The CONFIG dictionary in this file specifies which files will be uploaded to each service. You can add or remove extensions as needed.
For example:
Working with Python
Copy the code
CONFIG = { 1 .
    "s3": ["jpg", "png", "svg", "webp", "mp3", "mp4"],
    "gcs": ["doc", "docx", "csv", "pdf".
} . } . } . } .
This means that .jpg and .png files will be uploaded to S3, while .doc and .pdf files will be uploaded to Google Cloud Storage.
Examine
To test the module, create some dummy files in a folder and use the module as described in the Usage section. The module will show you fake upload messages for each file.