# TC : O(N*N) - two for loops n+(n-1)+(n-2)+.....+1 = worst,avg,best
# SC : O(1)
def selectionSort(l):
    n=len(l)
    for i in range(n):
        minNumIndx=i
        for j in range(i+1,n):
            if l[j]<l[minNumIndx]:
                minNumIndx=j
        l[i],l[minNumIndx]=l[minNumIndx],l[i]
        # print(l)
    print(l)

# TC : O(N*N) - two for loops n+(n-1)+(n-2)+.....+1 = worst,avg,best
# SC : O(1)
def bubbleSortBF(l):
    n=len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
        # print(l)
    print(l)

# TC : O(N*N) - two for loops n+(n-1)+(n-2)+.....+1 = worst,avg
# TC : O(N) - when we check and if there is swap it means all are in correct order = best
# SC : O(1)
def bubbleSortOptimal(l):
    n=len(l)
    for i in range(n):
        didSwap=0
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                didSwap = 1
                l[j],l[j+1]=l[j+1],l[j]
        if didSwap==0:
            break
        # print(l)
    print(l)

# TC : O(N*N) - n+(n-1)+(n-2)+.....+1 = worst,avg
# TC : O(N) - no insertion and changing when array is sorted = best
# SC : O(1)
def insertionSort(l):
    n=len(l)
    for i in range(1,n):
        k=l[i]
        j=i-1
        while j>=0 and l[j]>k:
            l[j+1]=l[j]
            j-=1
            # print(l, k)
        l[j+1]=k
        # print(l,k)
    print(l)

# TC : O(NlogN)
# recursion
# N                    1
# N/2 N/2              2
# N/4 N/4 N/4 N/4      4
# .
# .
# N/(2 pow n).........   (2 pow n)
# So TC = Log N    --- it is for recussion Mergesort function

#For Merge
# worst we need to iterate N size array , so it will be for log N times as for recurssion
# NlogN

# SC : O(N)
def mergeSort(low,high,arr):
    if low>=high:
        return
    mid=(low+high)//2
    mergeSort(low,mid,arr)
    mergeSort(mid+1,high,arr)
    Merge(low,mid,high,arr)
    # print(arr)
    if(low==0 and high==len(arr)-1):
        print(arr)

def Merge(low,mid,high,arr):
    i=low
    j=mid+1
    temp=[]
    while i<=mid and j<=high:
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        elif arr[i]>=arr[j]:
            temp.append(arr[j])
            j+=1
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<=high:
        temp.append(arr[j])
        j += 1
    # print("temp",temp,low,high,i,j)
    for i in range(low,high+1):
        arr[i]=temp[i-low]

# TC : O(N*N) - N - recurssion n-1 to 0 , N for swapping check = worst,Avg
# SC : O(1)
def recurssiveBubbleSort(l,n):
    if n==0:
        print(l)
        return
    for k in range(n):
        if l[k]>l[k+1]:
            l[k],l[k+1]=l[k+1],l[k]
    # print(l)
    recurssiveBubbleSort(l,n-1)

# TC : O(N*N) - N - recurssion n-1 to 0 , N for swapping check = worst,Avg
# O(N) - N for checking swapping = best
# SC : O(1)
def recurssiveBubbleSortOptimal(l,n):
    if n==0:
        print(l)
        return
    didSwap=0
    for k in range(n):
        if l[k]>l[k+1]:
            didSwap = 1
            l[k],l[k+1]=l[k+1],l[k]
    # print(l)
    if didSwap==0:
        print(l)
        return
    recurssiveBubbleSortOptimal(l,n-1)

# TC : O(N*N) - N - recurssion 1 to n , N for swapping while loop = worst,Avg
# O(N) - N only recurssive calls no while loop will run = best
# SC : O(1)
def recurssiveInsertionSort(l,k,n):
    if k==n:
        print(l)
        return
    i=k-1
    ele=l[k]
    while i>=0 and l[i+1]<l[i]:
        l[i+1],l[i]=l[i],l[i+1]
        i-=1
    l[i+1]=ele
    recurssiveInsertionSort(l,k+1,n)


# steps
# 1 . Pick a pivot
# 2 . place smaller in left and greater on left
# 3 . Place pivot in correct place

#TC : O(NlogN) LogN - func recurssion , N - for arranging smaller in left and greater on left
#SC : O(1)
def quickSort(l,low,high):
    if low>high:
        # print(l)
        return
    p=quickSortPartition(l,low,high)
    quickSort(l,low,p-1)
    quickSort(l,p+1,high)
    if low==0 and high==len(l)-1:
        print(l)

def quickSortPartition(l,low,high):
    pivot=low
    i=low
    j=high
    while i<j:
        while i<=j and l[i]<=l[pivot]:
            i+=1
        while i<=j and l[j]>l[pivot]:
            j-=1
        if i<j and l[i]>l[j] :
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
    l[j],l[pivot]=l[pivot],l[j]
    return j










