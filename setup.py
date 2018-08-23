import os
import sys
import re
import traceback

from setuptools import setup

try:
    __name__    = 'Utils'
    __author__  = __import__(__name__).version.AUTHOR
    __version__ = __import__(__name__).version.VERSION
except Exception:
    print(traceback.print_exc())
    exit(-1)

def _find_packages(prefix=''):
    packages = []
    path = '.'
    for root, _, files in os.walk(path):
        if '__init__.py' in files:
            if sys.platform.startswith('win'):
                packages.append(re.sub('^[^A-z0-9_]', '', root.replace('\\', '.')))

    print(packages)
    return packages

setup(
    name='py-snicks',
    version= __version__,
    packages=[''],
    url='',
    license='',
    author=__author__,
    author_email='Qif@equinor.com',
    description='Some small utilities'
)
