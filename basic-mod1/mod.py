msg = "54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288 "

print("picoCTF{", end="")
for val in msg.split():
    val = int(val) % 37
    if val < 26:
        print(chr(val + ord('A')), end="")
    elif val < 36:
        print(chr(val - 26 + ord('0')), end="")
    else:
        print("_", end="")
print("}")
