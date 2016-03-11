"""setup script.

Basic project setup script.
"""
from setuptools import setup, find_packages


setup(
    name='progen',
    version='0.0.1',
    description='Random Profile generator',
    license=None,
    author='Falade Mayowa',
    author_email='falademayowa240@gmail.com',
    install_requires=['markovify'],
    url='https://github.com/amandapickering/markovgenerator',
    keywords='Profile Random names address generator job job-title city description',
    packages=find_packages(),
)
