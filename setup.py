from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.0.2",
    description="This contains the code in the ./src directory of the project",
    author="adamr",
    packages=find_packages(where="./src"),
    package_dir={"":"./src"},
    install_requires=["setuptools"]

)