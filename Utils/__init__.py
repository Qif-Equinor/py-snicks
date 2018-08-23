import sys

# check env
if sys.version_info < (2, 6):
    raise ImportError(
        'Needs to be run on python 2.6 and above.'
    )
# end check env

from Utils import platforms
from Utils import unittest