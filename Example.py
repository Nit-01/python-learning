#let=[x*y for x in range(3,6,2) for y in range(7,4,-1)]
#print(let)


#import sys
#a=10
#b=20
#c=a+b
#sys.stdout.write(c)

'''
def add():
    a=10
    b=20
    print(f"sum is {a+b}")

def main():
    print("Program started")
    add()

if __name__=="__main__":
    main()
'''
'''
nums=[10,20,3,6,23]
print(max(nums, key=lambda x:x))
'''

'''
def add():
    print("Def add funvtion")
def main():
    print("My name is niteesh")
    add()
if __name__ == "__main__":
    main()
'''


'''
text=input()

result=""

for c in text:
    if c not in result:
        result+=c

print("".join(sorted(set(result))))


a=1050
b=1050
print(a is b)

for i in range(5):
    pass
    print(i)


    
s=input()
rev="" 
for ch in s:
    rev=ch+rev
print(rev)


import sys
ss=input()
s=0
l=len(ss)-1
while s<l:
    if ss[s]!=ss[l]:
        sys.stdout.write("Not a Palindrome")
        break
    s+=1
    l-=1
else:
    print("Palindrome") 



square=lambda x:x*x
print(square(5))

nums=[2,3,4,5]
result=list(map(lambda x:x*x,nums))
print(result)
'''

nums=[2,3,4,5]
result=list(filter(lambda x:x%2==0,nums))
print(result)