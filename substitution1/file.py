t = 'abcdefghijklmnopqrstuvwxyz'
v = 'xtikscaqdbporyfznujelghwmv'

msg = "CTFs (short for capture the flag) are a type of computer security competition. Contestants are presented with a set of challenges which test their creativity, technical (and googling) skills, and problem-solving ability. Challenges usually cover a number of categories, and when solved, each yields a string (called a flag) which is submitted to an online scoring service. CTFs are a great way to learn a wide array of computer security skills in a safe, legal environment, and are hosted and played by many security groups around the world for fun and practice. For this problem, the flag is: picoCTF{FR3QU3NCY"
msg = msg.lower()

print("Correct ----- ", end="")
for i in range(26):
    if t[i] in msg:
        print(v[i], end='')
    else:
        print("_", end='')

print()
print("Not Correct - ", end="")
for i in range(26):
    if t[i] in msg:
        print("_", end='')
    else:
        print(v[i], end='')


