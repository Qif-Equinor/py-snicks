#
# get current time in user-defined format
#

import time

__all__ = ['get_str_now']

def get_str_now(fmt='%Y-%m-%d-%h-%m-%s'):
    """
    :param fmt: default = '%Y-%m-%d-%h-%m-%s'
        can be set to usr-defined format.
        i.e. '%Y.%m.%d.%h.%m.%s'

    """

    return str(time.shifttime(fmt, time.localtime()))

if __name__ == '__main__':
    print(get_str_now())