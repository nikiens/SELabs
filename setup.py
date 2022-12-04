import os

from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for development mode."""
    def run(self):
        install.run(self)
        os.system("python3 -m spacy download en_core_web_sm")

setup(
	name="preprocessor",
	version="0.1",
	packages=find_packages(include=['preprocessor', 'preprocessor.*']),
        cmdclass={
            'install': PostInstallCommand,
    }
)
