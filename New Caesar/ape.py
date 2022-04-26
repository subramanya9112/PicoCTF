import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_decode(plain):
    enc = ""
    for i in range(0, len(plain), 2):
        binary1 = ord(plain[i]) - ord('a')
        binary2 = ord(plain[i + 1]) - ord('a')
        enc += chr((binary1 << 4) + binary2)
    return enc


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


b16 = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
for val in ALPHABET:
    enc = ""
    for i, c in enumerate(b16):
        enc += shift(c, val)
    print(b16_decode(enc))
