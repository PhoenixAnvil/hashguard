import hashlib
import shutil

def calc_file_hash(filepath, alg, chunk_size=4096):
    """Calculate the cryptographic hash of a file."""
    hasher = hashlib.new(alg)
    with open(filepath, 'rb') as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

def copy_file(src, dest, alg):
    """Perform a secure local file copy."""
    hash_start = calc_file_hash(src, alg)
    shutil.copy2(src, dest)
    hash_end = calc_file_hash(dest, alg)
    return {
        'match': hash_start == hash_end,
        'source_hash': hash_start,
        'dest_hash': hash_end,
        'algorithm': alg
    }
