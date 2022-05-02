word = 'python'
word [4]
word [-3]

word[:-1]

'i' in word
'o' in word

str = ' hello '
print(str.strip())
print(str.rstrip())
print(str.lstrip())
' '.join(str)
'12'.zfill(5)

import random

pick = set()

while len(pick) < 6:
    n = random.randint(0,45)
    if n not in pick:
        pick.add(n)
print(pick)
print(sorted(pick))