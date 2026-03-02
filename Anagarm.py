#Anagarm
'''
a=input()
b=input()

if sorted(a)==sorted(b):
    print("Anagaram")
else:
    print("Not a Anagram")
'''

a=input()
b=input()

if len(a)!=len(b):
    print("Not a Anagram")
else:
    count={}

    for ch in a:
        count[ch]=count.get(ch,0)+1

    for ch in b:
        count[ch]=count.get(ch,0)-1
    
    if all(v==0 for v in count.values()):
        print("Anagram")
    else:
        print("Not a Anagarm")