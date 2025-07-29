import pytest
import sys

from hello_world.arguments import parser, parse


def helper_test_no_argv(argv_0: str):
    sys.argv = [argv_0]
    args = parse(parser())
    assert not args.is_verbose, "expected 'args.is_verbose' to be False"
    # TODO Check additional default values


def helper_test_verbose(argv_0: str):
    sys.argv = [argv_0, "--verbose"]
    args = parse(parser())
    assert args.is_verbose, "expected 'args.is_verbose' to be True"


def test_parse():
    e = None
    _sys_argv = sys.argv
    try:
        helper_test_no_argv(_sys_argv[0])
        helper_test_verbose(_sys_argv[0])
    except Exception as ex:
        e = ex
    finally:
        sys.argv = _sys_argv
        if e != None:
            raise e

    # No arguments
    sys.args = []
    args = parse(parser())
