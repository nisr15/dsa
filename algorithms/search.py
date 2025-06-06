def linerSearch(l,k):
    for i in range(len(l)):
        if l[i]==k:
            return True
    return False


def binarySearch(l,k):
    high=len(l)-1
    low=0
    while(high>=low):
        mid = (high + low) // 2
        if l[mid]==k:
            return mid
            # return True
        elif l[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return None
    # return False

def binarySearchRecurrsion(l,k,low,high):
    mid=(low+high)//2
    if(high>=low):
        if l[mid]==k:
            return True
        elif l[mid]<k:
            return binarySearchRecurrsion(l,k,mid+1,high)
        elif l[mid]>k:
            return binarySearchRecurrsion(l,k,low,mid-1)
    else:
        return False

