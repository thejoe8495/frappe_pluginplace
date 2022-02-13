from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_pluginplace/__init__.py
from frappe_pluginplace import __version__ as version

setup(
	name="frappe_pluginplace",
	version=version,
	description="Get a overview over all plugins of frappe and erpnext",
	author="Jörg Stemmer",
	author_email="info@gluecks-it.de",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
