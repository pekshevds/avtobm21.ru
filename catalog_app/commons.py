import hashlib
from string import punctuation, whitespace


def clean_string(dirty_string: str) -> str:
    bad_chars = punctuation + whitespace
    return "".join([_ for _ in dirty_string if _ not in bad_chars])


def secret_from_string(string: str) -> str:
    hash = hashlib.blake2s(digest_size=4)
    hash.update(string.encode('utf-8'))
    return hash.hexdigest()
