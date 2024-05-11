import random
import string


ALPHABET = string.digits + string.ascii_letters
SHORT_URL_LENGTH = 7


cache = {}


def to_short(url):
    short_url = ''.join(random.choices(population=ALPHABET, k=SHORT_URL_LENGTH))
    cache[short_url] = url
    return short_url


def to_original(short_url):
    return cache[short_url]
