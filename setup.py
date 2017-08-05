"""Setup module for project."""

from setuptools import setup

setup(
    name="barca-football-cli",
    version="0.1.0",
    description="Displays results and fixtures for the"
                "FC Barcelona matches",
    scripts=["fcb.py"],
    entry_points={
        "console_scripts": [
            "fcb=fcb:main",
        ],
    }
)
