import codecs
import os
import re
import sys

from setuptools import setup, find_packages

# Acknowledgement: This setup.py was adapted from Hynek Schlawack's Python
#                  Packaging Guide
# https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty

###################################################################

NAME = "habitat-predict"
PACKAGES = find_packages()
META_PATH = os.path.join("habitat", "__init__.py")
README_PATH = "README.md"
PYTHON_REQUIRES = ">=3.6"

PACKAGE_DATA = {
    "habitat": [
        "data/hints.yml",
        "data/bmm/model.pth",
        "data/conv2d/model.pth",
        "data/kernels.sqlite",
        "data/linear/model.pth",
        "data/lstm/model.pth",
        # "habitat_cuda.cpython-36m-x86_64-linux-gnu.so",
        "habitat_cuda.cpython-39-x86_64-linux-gnu.so",
    ],
}

INSTALL_REQUIRES = [
    "pyyaml",
    "torch>=1.4.0",
    "pandas>=1.1.2",
    "tqdm>=4.49.0"
]

KEYWORDS = [
    "neural networks",
    "pytorch",
    "performance",
    "profiler",
    "predictions",
]

CLASSIFIERS = [
    "Do Not Upload",
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3 :: Only",
]

###################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and return the contents of the
    resulting file. Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


if __name__ == "__main__":
    setup(
        name=NAME,
        description=find_meta("description"),
        license=find_meta("license"),
        version=find_meta("version"),
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        long_description=read(README_PATH),
        long_description_content_type="text/markdown",
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS,
    )
