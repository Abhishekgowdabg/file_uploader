# config.py

# Configuration for file types
CONFIG = {
    "s3": ["jpg", "png", "svg", "webp", "mp3", "mp4", "mpeg4", "wmv", "3gp", "webm"],
    "gcs": ["doc", "docx", "csv", "pdf"]
}

# Mock configurations for AWS and GCP (for real usage, replace with actual credentials and settings)
AWS_S3_BUCKET = "mock-s3-bucket"
GCS_BUCKET = "mock-gcs-bucket"
