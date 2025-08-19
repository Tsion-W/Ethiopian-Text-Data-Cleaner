from setuptools import setup, find_packages

setup(
    name="ethioclean",
    version="0.1.0",
    description="Ethiopian text data cleaning tool (Amharic, Geez, etc.)",
    author="Tsion Getachew",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ethioclean=cli:main",
        ],
    },
    install_requires=["pandas", "regex"],
)
