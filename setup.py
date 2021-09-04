from setuptools import setup
from pathlib import Path

ROOT = Path(__file__).parent

LONG_DESCRIPTION = (ROOT / "README.md").read_text()


setup(
    name="pyromises",
    version="0.0.2",
    description="Promises for Python",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Eder Lima",
    author_email="lima.eder101@gmail.com",
    keywords=["python", "async", "promises"],
    license="MIT",
    packages=["pyromises", "pyromises/promise"],
)
