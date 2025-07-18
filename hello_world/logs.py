# see: https://docs.python.org/3/howto/logging.html

"""
Setup logging system for your script
"""
import logging


def log_setup(args):
    """Setup python logs"""
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
