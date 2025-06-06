def bubbleSort(l):
    n=len(l)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print(l)


def selectionSort(l):
    n=len(l)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if l[min]>l[j]:
                min=j
        l[i],l[min]=l[min],l[i]
    print(l)

def insertionSort(l):
    n=len(l)
    for i in range(1,n):
        k=i-1
        ele=l[i]
        while (k>=0 and ele<l[k]):
            l[k+1]=l[k]
            k-=1
        l[k+1]=ele
    print(l)

def mergeSort(l,low,high):
    if(low==high):
        return
    mid=(low+high)//2
    mergeSort(l,low,mid)
    mergeSort(l,mid+1,high)
    merge(l,low,mid,high)
    if(high==len(l)-1 and low==0):
        print(l)
        return l


def merge(l,low,mid,high):
    temp=[]
    i=low
    j=mid+1
    # print(low, mid,high, i, j)
    while(i<=mid and j<=high):
        if l[i]>l[j]:
            temp.append(l[j])
            j+=1
        else:
            temp.append(l[i])
            i+=1
    for k in range(i,mid+1):
        temp.append(l[k])
    for k in range(j,high+1):
        temp.append(l[k])
    for k in range(low,high+1):
        l[k]=temp[k-low]



def quickSortBasic(l):
    if (len(l)<=1):
        return l
    pivot=l[0]
    left=[]
    right=[]
    for k in l[1:]:
        if k<=pivot:
            left.append(k)
        elif k>=pivot:
            right.append(k)
    quickSort(left)
    quickSort(right)
    print(left + [pivot] + right)
    return left+[pivot]+right




def quickSort(l,low,high):
    if(low>=high):
        return
    pivot=l[low]
    mid=(low+high)//2
    i=low+1
    j=high
    print("1", l)
    while True:
        while(l[i]<=pivot):
            i+=1
        while(l[j]>=pivot):
            j-=1
        if(l[i]>l[j]):
            l[i], l[j] = l[j], l[i]
            i+=1
            j-=1
        print("2",l,i,j)
    l[j],l[low]=l[low],l[j]
    quickSort(l,low,mid)
    quickSort(l,mid+1,high)




