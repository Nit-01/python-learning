num=input()
try:
    num=int(num)
except ValueError:
    print(num,"Not Integer")
else:
    print(num," is a Integer")
finally:
    print("Always print if error or not error")
