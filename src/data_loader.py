import os
import shutil


def download_and_extract_dataset(url, extract_to):
    """Download and extract dataset from the given URL."""
    os.system(f"gdown {url}")
    os.makedirs(extract_to, exist_ok=True)
    shutil.unpack_archive('Safety_Helmet_Dataset.zip', extract_to)
