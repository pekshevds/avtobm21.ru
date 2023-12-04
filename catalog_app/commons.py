import hashlib


def secret_from_string(string: str) -> str:
    hash = hashlib.blake2s(digest_size=4)
    hash.update(string.encode('utf-8'))
    return hash.hexdigest()
