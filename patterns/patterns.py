#patters
n=5
for i in range(n):
    for j in range(n):
        print("* ",end="")
    print("")


for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print("")

for i in range(n):
    for j in range(i+1):
        print(j+1," ",end="")
    print("")

for i in range(n):
    for j in range(i+1):
        print(i+1," ",end="")
    print("")

for i in range(n):
    for j in range(n-i):
        print("* ",end="")
    print("")

for i in range(n):
    for j in range(n-i):
        print(j+1," ",end="")
    print("")

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    for j in range(n-i-1):
        print(" ",end="")
    print("")

for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(n-i-1)+1):
        print("*",end="")
    for j in range(i):
        print(" ",end="")
    print("")

#diamond
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    for j in range(n-i-1):
        print(" ",end="")
    print("")
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(n-i-1)+1):
        print("*",end="")
    for j in range(i):
        print(" ",end="")
    print("")

#half daimond
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print("")
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end="")
    print("")

for i in range(n):
    for j in range(i+1):
        print((j+i+1)%2,end=" ")
    print(" ")

for i in range(n-1):
    for j in range(2*(n-1)):
        if j<=i:
            print(j+1, end="")
        elif j>=2*(n-1)-i-1:
            print(2*(n-1)-j,end="")
        else:
            print(" ",end="")
    print("")

k=0
for i in range(n):
    for j in range(i+1):
        k+=1
        print(k,end=" ")
    print(" ")


for i in range(n):
    for j in range(i+1):
        print(chr(j+65),end=" ")
    print(" ")
print("hello")
for i in range(n):
    for j in range(n-i):
        print(chr(j+65),end=" ")
    print(" ")

for i in range(n):
    for j in range(i+1):
        print(chr(i+65),end=" ")
    print(" ")

for i in range(n):
    for j in range(i+1):
        print(chr(i+65),end=" ")
    print(" ")

for i in range(n-1):
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(2*i+1):
        if j<=i:
            print(chr(j+ 65), end="")
        else:
            print(chr(2*i-j+ 65), end="")
    print("")

for i in range(n):
    for j in range(i+1):
        print(chr(n+j-1-i+65),end=" ")
    print("")

for i in range(n):
    for j in range(2*n):
        if j<(n-i) or j>(n-1+i):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print("")
for i in range(n):
    for j in range(2*n):
        if j<(i+1) or j>(2*(n-1)-i):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print("")


for i in range(n-1):
    for j in range(2*n):
        if j<(i+1) or j>(2*(n-1)-i):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print("")
for i in range(n):
    for j in range(2*n):
        if j<(n-i) or j>(n-1+i):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print("")


for i in range(n-1):
    for j in range(n-1):
        if i==0 or i==(n-2) or j==0 or j==(n-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

# p=4
# for i in range(2*p-1):
#     for