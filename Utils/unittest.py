#
# unit test functionalities
#

__all__ = [
    'assert_true',
    'assert_false'
]

def _assert_bool(val, exp, errmsg=''):
    if (val is not exp):
        msg = 'got %s, expect %s\n User ErrMsg: %s' % (val, exp, errmsg)
        assert False, msg

def assert_true(val, errmsg=''):
    """
    if val is NOT true, assert and print to stdout
    errmsg: error message for stderr
    """
    if type(val) != bool:
        raise ValueError('The type of val is not bool.')

    _assert_bool(val, True, errmsg)


def assert_false(val, errmsg=''):
    """
    if val is NOT false, assert and print to stdout
    errmsg: error message for stderr
    """
    if type(val) != bool:
        raise ValueError('The type of val is not bool.')

    _assert_bool(val, False, errmsg)