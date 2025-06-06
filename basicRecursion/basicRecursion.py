# Recursion : function calls itself

# Whenever recursion calls are executed, they’re simultaneously stored in a recursion stack
# where they wait for the completion of the recursive function

# A recursive function can only be completed if a base condition is fulfilled and the control returns to the parent function.
# But, when there is no base condition given for a particular recursive function,
# it gets called indefinitely which results in a Stack Overflow i.e, exceeding the memory limit of the recursion stack




def fun(n=0):
    print(n)
    if n==3:
        return
    fun(n+1)

#TC : O(N)  -- N function calls
def funname(n):
    if n==0:
        return
    print("Nana")
    funname(n-1)


#TC : O(N)  -- N function calls
def fun1ton(n):
    if n==0:
        return
    print(n)
    fun1ton(n-1)

#TC : O(N)  -- N function calls
def funnto1(n):
    if n==0:
        return
    funnto1(n-1)
    print(n)

#TC : O(N)  -- N function calls
def sumRec(n):
    if n==0:
        return 0
    return sumRec(n-1)+n

#TC : O(N) -- N function calls
def factRec(n):
    if n==1:
        return 1
    return factRec(n-1)*n


#TC : O(N/2) -- n/2 as we are only iterating of half of array
def revArrayRec(l,start,end):
    if start>=end:
        return l
    l[start],l[end]=l[end],l[start]
    # print(l)
    return revArrayRec(l, start+1, end-1)

#TC : O(N/2) -- n/2 as we are only iterating of half of string
def checkPalendromRec(s,start,end):
    if start>=end:
        return True
    elif s[start]==s[end]:
        return checkPalendromRec(s,start+1,end-1)
    else:
        # print(s,start,end)
        return False

# TC: O(2 pow N) -- involves two function calls for each iteration which further expands to 4 function calls and so on which makes worst-case time complexity to be exponential in nature
def fibonaciRec(n):
    if n<=1:
        return n
    return fibonaciRec(n-1)+fibonaciRec(n-2)


