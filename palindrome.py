#palindrome

s=input()
l=len(s)
flag =True

for i in range(l//2):
    if s[i]!=s[l-i-1]:
        flag =False
print(flag)