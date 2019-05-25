import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "frontman",
    version = "1.0.0",
    packages = find_packages(),
    author = "Felipe Faria",
    author_email = "thefelipefaria@gmail.com",
    description="Proxybroker with configurable settings.",
    license = "closed",
    keywords = "twitter extractor microservice",
    url = "https://github.com/synchronizing/chirp",
    long_description=read('README.md'),
    project_urls={
        "Home": "https://github.com/synchronizing/frontman",
    }
)
