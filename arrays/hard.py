##Write a program to generate Pascal's triangle. Give the nth line of Pascal’s triangle
# TC : O(N*N)
# SC : O(N*N)
def nthLineOfPascalTriangleBruteForce(n):
    if n==1:
        return [[1]]
    elif n==2:
        return [[1,1]]
    else:
        l=[[1],[1,1]]
        for j in range(n-2):
            k=l[-1]
            t=len(k)
            p=[1]
            for i in range(t-1):
                p.append(k[i]+k[i+1])
            p.append(1)
            l.append(p)
        return l[-1]

# TC : O(N-1)
# SC : O(n)
def nthLineOfPascalTriangleOptimal(n):
    r=n-1
    c=0
    res=1
    l=[res]
    for i in range(r):
        res=res*(r-i)
        res=res//(i+1)
        l.append(res)
    return l