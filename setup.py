"""Setup module for project."""

from setuptools import setup

setup(
    name="barca-football-cli",
    version="0.1.0",
    description="Displays results and fixtures for the"
                "FC Barcelona matches",
    scripts=["fcb.py"],
    install_requires=[
        "beautifulsoup4>=4.6.0",
        "click>=6.7",
        "requests>=2.18.1",
        "termcolor>=1.1.0"
    ],
    entry_points={
        "console_scripts": [
            "fcb=fcb:main",
        ],
    }
)
