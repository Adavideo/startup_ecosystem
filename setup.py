from setuptools import setup, find_packages

setup(
    name="startup_ecosystem",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
        "pytest",
        "pytest-asyncio",
        "httpx",
    ],
)
