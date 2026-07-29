'''
setup.py file is an essential part of packing and distributing python projects. It is used by setuptools to define the 
configuration of project, such as metadata, dependencies and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst:List[str] = []
    try :
        with open('requirements.txt', 'r') as file :
            # Read lines from files
            lines = file.readlines()

            # Process each line
            for line in lines :
                requirement = line.strip()

                #Ignore empty lines and -e.
                if requirement and requirement != '-e .' :
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name = "ML-NetworkSecurity",
    version = "0.0.1",
    author = "Sahil Patel",
    author_email = "sahilpatel16301@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)