from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in micro/__init__.py
from micro import __version__ as version

setup(
	name="micro",
	version=version,
	description="Micro Crispr Biometric Integration",
	author="IBSL",
	author_email="-",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
