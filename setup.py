# Remember to change versions in the following files:
# README.md
# remember to change the last updated date on release [14] (in README.md)
# conf.py (in docs)
# index.rst [16] (in docs)

import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = "1.2.1.1"
PACKAGE_NAME = "Epytoml"
AUTHOR = "Zhean Robby Ganituen"
AUTHOR_EMAIL = "zheanrobbyganituen@gmail.com"
URL = "https://github.com/Z1aaan/Epytoml"

LICENSE = "MIT License"
DESCRIPTION = "A python library that converts plain text into a specified markup language using python."
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ["pdfkit", "tkDocViewer", "tkPDFViewer", "PyPDF2", "lorem"]


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
)
