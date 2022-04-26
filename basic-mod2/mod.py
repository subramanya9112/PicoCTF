msg = "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186"

def modInverse(n):
    for i in range(1, 41):
        if i * n % 41 == 1:
            return i
    return 0

print("picoCTF{", end="")
for val in msg.split():
    val = int(val) % 41
    val = modInverse(val)
    if 1 <= val and val <= 26:
        print(chr(val - 1 + ord('A')), end="")
    elif val < 37:
        print(chr(val - 27 + ord('0')), end="")
    else:
        print("_", end="")
print("}")
