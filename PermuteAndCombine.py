#PermuteAndCombine.py

from collections import Counter

words=input().split()
chars=input().split()

char_count=Counter(chars)

for w in words:
    word_count=Counter(w)

    flag=True
    for c in word_count:
        if word_count[c]>char_count[c]:
            flag=False
            break
    if flag:
        print(w)