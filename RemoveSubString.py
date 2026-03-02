#RemoveSubString

def remove(s,sub):
    if sub not in s:
        return s
    else:
        return remove(s.replace(sub,"",1),sub)
s=input()
sub=input()

result=remove(s,sub)
print(result)