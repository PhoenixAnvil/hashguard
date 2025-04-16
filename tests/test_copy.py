# tests/test_copy.py

import hashlib

import pytest

from hashguard import copy


def create_test_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def test_calc_file_hash_valid(tmp_path):
    file_path = tmp_path / "file.txt"
    create_test_file(file_path, "hello world")
    expected_hash = hashlib.sha256(b"hello world").hexdigest()
    result = copy.calc_file_hash(str(file_path), "sha256")
    assert result == expected_hash


def test_calc_file_hash_different_alg(tmp_path):
    file_path = tmp_path / "file.txt"
    create_test_file(file_path, "hello")
    expected_hash = hashlib.md5(b"hello").hexdigest()
    result = copy.calc_file_hash(str(file_path), "md5")
    assert result == expected_hash


def test_calc_file_hash_invalid_algorithm(tmp_path):
    file_path = tmp_path / "file.txt"
    create_test_file(file_path, "data")
    with pytest.raises(ValueError):
        copy.calc_file_hash(str(file_path), "fakealg")


def test_copy_file_hashes_match(tmp_path):
    src = tmp_path / "source.txt"
    dest = tmp_path / "dest.txt"
    create_test_file(src, "same content")
    result = copy.copy_file(str(src), str(dest), "sha256")
    assert result["match"] is True
    assert result["source_hash"] == result["dest_hash"]
    assert result["algorithm"] == "sha256"


def test_copy_file_hashes_do_not_match(tmp_path):
    src = tmp_path / "source.txt"
    dest = tmp_path / "dest.txt"
    copy.create_test_file = lambda p, c: p.write_text(c)

    # Create source file
    copy.create_test_file(src, "original content")

    # Perform a valid copy first
    result = copy.copy_file(str(src), str(dest), "sha256")
    assert result["match"] is True  # sanity check

    # Tamper with destination AFTER the copy
    with open(dest, "a", encoding="utf-8") as f:
        f.write(" -- tampered")

    # Recalculate dest hash only
    tampered_hash = copy.calc_file_hash(str(dest), "sha256")

    # Check that hashes no longer match
    assert tampered_hash != result["source_hash"]


def test_copy_file_invalid_algorithm(tmp_path):
    src = tmp_path / "source.txt"
    dest = tmp_path / "dest.txt"
    create_test_file(src, "test")
    with pytest.raises(ValueError):
        copy.copy_file(str(src), str(dest), "fakehash")


def test_calc_file_hash_file_not_found():
    with pytest.raises(FileNotFoundError):
        copy.calc_file_hash("nonexistent.file", "sha256")


def test_copy_file_source_not_found(tmp_path):
    dest = tmp_path / "dest.txt"
    with pytest.raises(FileNotFoundError):
        copy.copy_file("nonexistent.file", str(dest), "sha256")
