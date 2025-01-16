from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'  # Corrected value for editable install

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies,
    excluding '-e .' if present.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newline characters
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Remove '-e .' if it exists
    
    return requirements

setup(
    name='ML_project',
    version='0.0.1',
    author='Benet',
    author_email='beneta0603@gmail.com',  # Corrected spelling
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)