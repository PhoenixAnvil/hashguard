"""
HashGuard CLI

A secure local file copy tool that verifies file integrity using hash functions.
Supports custom hashing algorithms, verbose output, and listing available algorithms.
"""

import argparse
import hashlib
from pathlib import Path

from hashguard.copy import copy_file


def setup_cli():
    """
    Set up and parse command-line arguments for the HashGuard CLI tool.

    Returns:
        argparse.Namespace: Parsed CLI arguments.
    """
    parser = argparse.ArgumentParser(
        prog="HashGuard", description="Secure Local File Copy CLI Tool"
    )

    parser.add_argument("sourcefile", help="Source file path to copy")
    parser.add_argument(
        "destfile", help="Destination file path to copy"
    )
    parser.add_argument("hashalg", help="Hash algorithm to use")
    parser.add_argument(
        "-l",
        "--list-algorithms",
        action="store_true",
        help="List available hashing algorithms",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show result of copy operation",
    )
    return parser.parse_args()


def file_exists(filepath):
    """
    Check whether the specified file exists.

    Args:
        filepath (str): Path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    file_path = Path(filepath)
    return file_path.exists()


def list_algorithms():
    """
    Print a sorted list of available hashing algorithms.
    """
    for alg in sorted(
        hashlib.algorithms_available, key=lambda a: a.lower()
    ):
        print(f"- {alg.lower()}")


def algorithm_exists(hashalg):
    """
    Check whether the given hashing algorithm is supported.

    Args:
        hashalg (str): Name of the hashing algorithm.

    Returns:
        bool: True if the algorithm exists, False otherwise.
    """
    return hashalg.lower() in {
        alg.lower() for alg in hashlib.algorithms_available
    }


def main():
    """
    Entry point for the HashGuard CLI.

    Parses command-line arguments, validates inputs, performs the secure
    file copy, and optionally prints results.
    """
    args = setup_cli()

    if args.list_algorithms:
        return list_algorithms()

    src, dest, alg = (
        args.sourcefile,
        args.destfile,
        args.hashalg.lower(),
    )

    if not file_exists(src):
        raise FileNotFoundError(f"Source file not found: {src}")

    if not algorithm_exists(alg):
        raise ValueError(f"Unsupported hashing algorithm: {alg}")

    result = copy_file(src, dest, alg)
    if args.verbose:
        print(f"Source Hash: {result['source_hash']}")
        print(f"Dest Hash: {result['dest_hash']}")
        print(f"Algorithm: {result['algorithm']}")
        print("✅ Match" if result["match"] else "❌ Mismatch")


if __name__ == "__main__":
    main()
