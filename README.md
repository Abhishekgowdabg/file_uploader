This Python module scans a directory and uploads files to AWS S3 and Google Cloud Storage primarily based on their kinds. It supports photo and media documents for S3 and file documents for Google Cloud Storage. The forms of documents to be uploaded to each provider are configurable.

Table of Contents
Assignment Overview
Installation
Configuration
Usage
Testing
Contributing
License
Assignment Overview
The module presents the following functionalities:

Directory Scanning: Recursively reads all files from a distinct listing and its subdirectories.
File Uploading:
AWS S3: Uploads pics and media files.
Google Cloud Storage: Uploads file documents.
Configurability: File sorts to add to every garage service are configurable.
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.Com/Abhishekgowdabg/file_uploader.Git
cd file_uploader
2. Create and Activate a Virtual Environment
For Windows:
bash
Copy code
python -m venv venv
.VenvScriptsactivate
For macOS/Linux:
bash
Copy code
python3 -m venv venv
supply venv/bin/spark off
3. Install the Dependencies
bash
Copy code
pip set up -e .
Configuration
The configuration for record types and bucket names is placed in file_uploader/config.Py. Modify this record to specify which report kinds are uploaded to AWS S3 and Google Cloud Storage.

Configuration Details
AWS S3 Bucket: Update the AWS_S3_BUCKET variable together with your S3 bucket call.
Google Cloud Storage Bucket: Update the GCS_BUCKET variable with your GCS bucket call.
File Types for S3: Modify the s3 listing in the CONFIG dictionary to include document extensions for photographs and media documents.
File Types for GCS: Modify the gcs listing within the CONFIG dictionary to include file extensions for files.
Usage
To use the module, run the subsequent command:

bash
Copy code
report-uploader <directory>
Replace <directory> with the course to the folder you need to scan and add files from (e.G., C:UsersYourNameDocuments).

Example
bash
Copy code
document-uploader C:UsersChethanDocuments
Testing
To ensure the module works successfully, run the supplied test instances:

Run Tests:

bash
Copy code
python -m unittest find out -s checks
Add Test Cases: Add or adjust assessments within the assessments listing to cover extra scenarios.

Test Example
The test_uploader.Py file consists of a simple test for the get_files_by_extension characteristic:

python
Copy code
import unittest
from file_uploader.Uploader import get_files_by_extension

class TestUploader(unittest.TestCase):
    def test_get_files_by_extension(self):
        test_dir = "test_directory"
        extensions = ["jpg", "png"]
        files = get_files_by_extension(test_dir, extensions)
        # Mock test here: Normally you would installation a ridicule listing shape
        self.AssertTrue(isinstance(files, list))

if __name__ == "__main__":
    unittest.Foremost()
