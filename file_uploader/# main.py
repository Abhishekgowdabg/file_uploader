# main.py

import sys
from .uploader import upload_files

def main():
    if len(sys.argv) != 2:
        print("Usage: file-uploader <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    upload_files(directory)
