import Utils

from Utils import platforms
from Utils import  unittest

def test_platforms():
    unittest.assert_true(platforms.is_windows())