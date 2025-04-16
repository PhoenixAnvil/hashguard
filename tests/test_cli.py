# tests/test_cli.py

from hashguard import cli


def test_file_exists_true(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("test content")
    assert cli.file_exists(str(file)) is True


def test_file_exists_false():
    assert cli.file_exists("nonexistent.file") is False


def test_algorithm_exists_valid():
    assert cli.algorithm_exists("sha256") is True


def test_algorithm_exists_invalid():
    assert cli.algorithm_exists("fakealgoxyz") is False
