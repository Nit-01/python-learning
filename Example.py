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

text=input()

result=""

for c in text:
    if c not in result:
        result+=c

print("".join(sorted(set(result))))
