"""Python setup.py for project_health package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("project_health", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="project_health",
    version=read("project_health", "VERSION"),
    description="Awesome project_health created by fidias-i",
    url="https://github.com/fidias-i/Project-Health/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="fidias-i",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["project_health = project_health.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
