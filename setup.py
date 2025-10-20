"""Setup configuration for crisiscore-text-splitter package."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="crisiscore-text-splitter",
    version="0.1.0",
    author="CrisisCore-Systems",
    author_email="Crisiscore.systems@proton.me",
    description="Intelligent text file splitting utility with GUI and CLI interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CrisisCore-Systems/text_splitter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PySimpleGUI>=4.60.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "text-splitter=src.main:main",
        ],
    },
)
