#
# check current platfrom
#
# author: Qif
#

import select
import platform

__all__ = [
    'is_linux'
    'is_windows'
    'is_mac'
]

def is_linux() :
    if platform.platform().startswith('Linux'):
        return True
    else:
        return False

def is_windows() :
    if platform.platform().startswith('Windows'):
        return True
    else:
        return False

def is_mac() :
    if hasattr(select, 'kqueue'):
        return True
    else :
        return False