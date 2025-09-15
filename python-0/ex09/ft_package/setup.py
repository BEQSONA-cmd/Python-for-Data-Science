from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    packages=find_packages(),
    author="Beqa Tvildiani",
    author_email="tvildiani2001@gmail.com",
    description="A small package from 42 school subject",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BEQSONA-cmd/ft_package",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
