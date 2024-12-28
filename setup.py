import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "leap_year_checker",
    packages = ["leap_year_checker"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = "1.0.1",
    description = "This package was created to check if a year is a leap year and to separate leap years from non-leap years in a set of years.",
    author = "ElenaReach",
    classifiers=(
        "Programming Language :: Python",
        "Natural Language :: English",
        "Environment :: Plugins",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ),
    project_urls={
        'Source': '',
    },
)
