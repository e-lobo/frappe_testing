from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_testing/__init__.py
from frappe_testing import __version__ as version

setup(
	name="frappe_testing",
	version=version,
	description="A simpler frappe-test-fixture provider",
	author="Leam Technology Systems",
	author_email="info@leam.ae",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
