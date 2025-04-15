"""
File copy and Verification Logic for HashGuard

This module provides functions for performing secure file copies
with cryptographic hash verification to ensure integrity.
"""

import hashlib
import shutil


def calc_file_hash(filepath, alg, chunk_size=4096):
    """
    Calculate the cryptographic hash of a file.

    Args:
        filepath (str): Path to the file to hash.
        alg (str): Hash algorithm to use (e.g., 'sha256', 'md5').
        chunk_size (int, optional): Number of bytes to read at a time. Defaults to 4096.

    Returns:
        str: Hexadecimal digest of the file's hash.
    """
    hasher = hashlib.new(alg)
    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()


def copy_file(src, dest, alg):
    """
    Perform a secure local file copy with hash verification.

    Args:
        src (str): Path to the source file.
        dest (str): Path to the destination file.
        alg (str): Hash algorithm to use for integrity check.

    Returns:
        dict: A dictionary with the following keys:
            - 'match' (bool): True if source and destination hashes match.
            - 'source_hash' (str): Hash of the source file.
            - 'dest_hash' (str): Hash of the destination file.
            - 'algorithm' (str): The algorithm used for hashing.
    """
    hash_start = calc_file_hash(src, alg)
    shutil.copy2(src, dest)
    hash_end = calc_file_hash(dest, alg)
    return {
        "match": hash_start == hash_end,
        "source_hash": hash_start,
        "dest_hash": hash_end,
        "algorithm": alg,
    }
