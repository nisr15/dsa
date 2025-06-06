from math import log10

#TC O(log10N) - because divion of number N
def countDigitsBf(n):
    c=0
    while n:
        c+=1
        n=n//10
    print(c)
    return c


#TC O(1) - because direct one step answer
def countDigitsOptimal(n):
    c=int(log10(n)+1)
    print(c)
    return c

def reverseNumber(n):
    ans = 0
    while n:
        ans=ans*10+(n%10)
        n = n // 10
    print(ans)
    return ans

def checkPalindrom(n):
    if (n==reverseNumber(n)):
        print(n)
        print(True)
        return True
    print(False)
    return False

#GCD is at end

#TC o(log10N)
def armstrongNum(n):
    ans = 0
    p=n
    while n:
        k=n%10
        ans = ans+(k*k*k)
        n = n // 10
    if(p==ans):
        print(True)
        return True
    print(False)
    return False


#TC : O(n)
def divisorBf(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    print(l)
    return l

# observation
# 1 36
# 2 18
# 3 12
# 4 9
# 6 6 -- after squrt the same numbers are repating as factors
# 9 4
# 12 3
# 18 2
# 36 1

# So if we capture the mutiplicant for n when a factor is found we get two factors for n
# And till squrt we will be covering all factors


#TC : O(squrt(n) + klogk )  = squrt(n) - for loop running squrt(n) time + klogk - sorting k number of factors of n
def divisorOptimal(n):
    l=[]
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            l.append(i)
            if n!=i*i:
                l.append(n//i)
    l.sort()
    print(l)
    return l

#TC : O(n)
def primnumberBf(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print("Prime")
        return True
    else:
        print("Comp")
        return False

#TC : O(squrt(n))
def primnumberOptimal(n):
    c=0
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            c+=1
            if n!=i*i:
                c+=1
    if c==2:
        print("Prime")
        return True
    else:
        print("Comp")
        return False


#TC : O(min(n1,n2))
def gcdBf(n1,n2):
    m=min(n1,n2)
    ans=1
    for i in range(1,m+1):
        if n1%i==0 and n2%i==0:
            ans=i
    print(ans)
    return ans

#TC : O(squrt(min(n1,n2)))
def gcdBetter(n1,n2):
    m=min(n1,n2)
    ans=1
    for i in range(1,int(m**(1/2))+1):
        k=m//i
        # print(i,k)
        if n1%i==0 and n2%i==0:
            ans=max(ans,i)
        if n1%k==0 and n2%k==0:
            ans=max(ans,k)
    print(ans)
    return ans


#Euclidian algorithm
# gcd(n1,n2) = gcd(n1-n2,n1) -- where n1>n2
# And if n1==0 then n2 is gcd else if n2==0 then n1 is gcd
# gcd(13,71)
# 13 71
# 13 58
# 13 45
# 13 32
# 13 19
# 13 6
# 7 6
# 1 6
# 1 5
# 1 4
# 1 3
# 1 2
# 1 1
# 1 0
# 1- is gcd of 13 and 71

# on observation
# gcd(13,71)
# 13 71
# 13 58
# 13 45
# 13 32
# 13 19
# 13 6     -- it is 71%13=6
# 7 6
# 1 6      -- it is 7%6=1
# 1 5
# 1 4
# 1 3
# 1 2
# 1 1
# 1 0     -- it is 6%1=0
# 1    -- it is the answer

#based on this chaninging logic gives
# 13 71
# 13 6
# 1 6
# 1 0
# 1

# TC O(
def gcdOptimal(n1,n2):
    while n1>0 and n2>0:
        if n1>n2:
            n1=n1%n2
        else:
            n2=n2%n1
    if n1==0:
        print(n2)
        return n2
    else:
        print(n1)
        return n1

def gcdOptimalRec(n1,n2):
    # print(n1, n2)
    if n1==0:
        print(n2)
        return n2
    elif n2==0:
        print(n1)
        return n1
    elif n1>n2:
        gcdOptimalRec(n1%n2,n2)

    else:
        gcdOptimalRec(n1,n2%n1)



