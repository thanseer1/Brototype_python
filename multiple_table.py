print("----------- Multiplication Table.............")

print("---------------------------------------------")

N=int(input("How much long multplication table you want\n"))

M=int(input("which multiplication table you want\n"))

for i in range(1,N+1):
    mul=i*N
    print("  {}  X  {}  ={}".format(i,M,mul))