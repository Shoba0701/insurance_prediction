from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function get all the packages from given path 
    '''
    hypen_e_dot = "-e ."
    requirements =[]
    with open("requirements.txt") as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements


setup(
    name = "insurance_charge_prediction",
    version = "0.0.1",
    author = "Shoba",
    author_email = "arun.shoba137@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")

)