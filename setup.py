from setuptools import setup, find_packages

setup(
    name='my_yolov10_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'gdown',
        'ultralytics',
        'streamlit',
        'Pillow',
    ],
)
