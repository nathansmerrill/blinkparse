import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cliparse2", # Replace with your own username
    version="0.0.1",
    author="Nathan Merrill",
    author_email="mathiscool3000@gmail.com",
    description="A python library for parsing command line arguments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nathansmerrill/cliparse2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)