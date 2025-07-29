# see: https://docs.python.org/3/library/argparse.html

"""
Configure the arguments accepted by your script.
"""
import argparse


def parser():
    """parser Configure the argument parser and return it"""
    p = argparse.ArgumentParser()
    p.add_argument(
        "--verbose",
        action="store_true",
        dest="is_verbose",
        help="Verbose logs",
        default=False,
    )

    # TODO Left on purpose as part of the template to help to the developer
    #      to extend based on their requirements.

    # subparsers = p.add_subparsers(
    #     dest="subcommand", title="subcommand", description="The subcommand to run"
    # )

    # Install subcommand
    # install_parser = subparsers.add_parser("install", help="Install something")
    # install_parser.add_argument(
    #     "--force", action="store_true", help="Force installation"
    # )

    # Remove subcommand
    # remove_parser = subparsers.add_parser("remove", help="Remove something")
    # remove_parser.add_argument("--force", action="store_true", help="Force removal")

    # Run subcommand
    # run_parser = subparsers.add_parser("run", help="Run something")
    # run_parser.add_argument(
    #     "--verbose", action="store_true", dest="is_verbose", help="Verbose execution"
    # )

    return p


def parse(the_parser):
    """Retrieve a new argument parser and extract the arguments"""
    args = the_parser.parse_args()
    return args
