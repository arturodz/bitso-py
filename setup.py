# chardet's setup.py
from distutils.core import setup
setup(
    name = "bitso-py",
    packages = ["bitso-py"],
    version = "0.0.1",
    description = "Bitso Exchange API Wrapper",
    author = "Arturo Diaz",
    author_email = "me@arturodz.com",
    url = "http://github.com/arturodz/bitso-py",
    download_url = "http://github.com/arturodz/bitso-py",
    keywords = ["bitcoin", "bitso", "api", "wrapper"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        ],
    long_description = """\
Bitso API Wrapper
-------------------------------------
"""
)
