from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(path: str) -> List[str]:
    """
    This function allows us to return all, the packages which
    are mentioned in requirements.txt file.
    """
    
    requirements = []
    
    with open(path, 'r') as file:
        requirements = file.readlines()
        
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='open-problems-single-cell-perturbations-kaggle-competition',
    version='1.0.0',
    author="Abdullah Khan",
    author_email='abdullahkhan9003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
    # Remove any empty strings from list of lines and remove comments starting with '#' symbol