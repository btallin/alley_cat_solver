from setuptools import setup, find_packages


setup(
    name="travelling_salesperson",
    version="0.0.1",
    description="Library for solving travelling salesperson problem in "
    "real-world uses cases using google maps API for find distances "
    "between nodes.",
    author="Benjamin Tallin",
    author_email="btallin35@gmail.com",
    packages=find_packages(include=["travelling_salesperson"]),
    install_requires=[
        "python-dotenv",
        "numpy",
        "requests",
    ],
    include_package_data=True
)
