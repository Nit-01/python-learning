#NestedTryExcept

num=input()

try:
    num=int(num)
    try:
        result=10/0

    except ZeroDivisionError:
        print(num," is Zero")
    else:
        print(result)

except ValueError:
    print(num," is not a Integer")
