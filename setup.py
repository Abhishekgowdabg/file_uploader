# setup.py
from setuptools import setup, find_packages

setup(
    name="file_uploader",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "google-cloud-storage"
    ],
    entry_points={
        "console_scripts": [
            "file-uploader=file_uploader.main:main",  # Make sure this points to the main function in main.py
        ],
    },
)
