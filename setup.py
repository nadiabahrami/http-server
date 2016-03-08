# coding=utf-8
from setuptools import setup

setup(
    name="http-server",
    description="Python 401 http echo http-server",
    version=0.1,
    author=["Nadia Bahrami", "Daniel Zwelling"],
    author_email=["nadia.bahrami@gmail.com", "dzwellingmusic@gmail.com"],
    license="MIT",
    py_modules=["client", "server"],
    package_dir={"": "src"},
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
