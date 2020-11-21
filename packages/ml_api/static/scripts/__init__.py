
from static.scripts.config import PACKAGE_ROOT, PACKAGE_ROOT_MAIN

with open(PACKAGE_ROOT / 'VERSION_api') as version_file:
	_version = version_file.read().strip()



with open(PACKAGE_ROOT_MAIN / 'VERSION') as version_file:
	__version__ = version_file.read().strip()