n1=int(input("Enter a two number\n"))
n2=int(input())

try:

    div=n1/n2
    print("Division",div)

except ZeroDivisionError:
    print("zero can div number")    