# uploader.py

import os
from .config import CONFIG, AWS_S3_BUCKET, GCS_BUCKET

# Mock upload functions
def mock_upload_to_s3(file_path, bucket):
    print(f"Mock uploading {file_path} to S3 bucket {bucket}.")

def mock_upload_to_gcs(file_path, bucket):
    print(f"Mock uploading {file_path} to Google Cloud Storage bucket {bucket}.")

def get_files_by_extension(directory, extensions):
    matched_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.split(".")[-1].lower() in extensions:
                matched_files.append(os.path.join(root, file))
    return matched_files

def upload_files(directory):
    # Get files by type
    s3_files = get_files_by_extension(directory, CONFIG["s3"])
    gcs_files = get_files_by_extension(directory, CONFIG["gcs"])
    
    # Upload to S3
    for file_path in s3_files:
        mock_upload_to_s3(file_path, AWS_S3_BUCKET)
    
    # Upload to GCS
    for file_path in gcs_files:
        mock_upload_to_gcs(file_path, GCS_BUCKET)
