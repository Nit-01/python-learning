#replaceOldStringPart.py
def find_main(text,old,new):
    result=text.replace(old,new)
    return result
text=input()
old=input()
new=input()

output=find_main(text,old,new)
print(output)
