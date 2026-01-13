#given a sorted array of integers and a target, search for the target in the given array. Assume the given array does not contain any duplicate numbers.
import sys


# TC : O(logN)
# SC : O(1)
def binarySearchIterative(nums,target):
    n = len(nums)
    i = 0
    j = n - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] > target:
            j = mid - 1
        elif nums[mid] < target:
            i = mid + 1
        else:
            return mid
    return -1

# TC : O(logN)
# SC : O(1)
def binarySearchRecurssive(nums,target):
    n = len(nums)
    def bs(l, n, low, high):
        if low <= high:
            mid = (low + high) // 2
            if l[mid] == target:
                return mid
            elif l[mid] > target:
                return bs(l, n, low, mid - 1)
            else:
                return bs(l, n, mid + 1, high)
        return -1

    return bs(nums, n, 0, n - 1)

# Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
# TC : O(N)
# SC : O(1)
def lowerBoundBruteforce(l,r):
    n=len(l)
    for i in range(n):
        if l[i]>=r:
            return i
    return n

# TC : O(logN)
# SC : O(1)
def lowerBoundOptimal(l,r):
    n=len(l)
    i = 0
    j = n - 1
    ans=n
    while i <= j:
        mid = (i + j) // 2
        if l[mid]>=r:
            ans = mid
            j = mid - 1
        elif l[mid] < r:
            i = mid + 1
    return ans


#Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.
# TC : O(N)
# SC : O(1)
def upperBoundBruteforce(l,r):
    n=len(l)
    for i in range(n):
        if l[i]>r:
            return i
    return n

# TC : O(logN)
# SC : O(1)
def upperBoundOptimal(l,r):
    n = len(l)
    i = 0
    j = n - 1
    ans = n
    while i <= j:
        mid = (i + j) // 2
        if l[mid] > r:
            ans = mid
            j = mid - 1
        elif l[mid] <= r:
            i = mid + 1
    return ans

# given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.
#TC : O(logN)
#SC : O(1)
def searchInsertPos(nums,target):
    n = len(nums)
    i = 0
    j = n - 1
    ans = n
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] > target:
            j = mid - 1
            ans = j + 1
        elif nums[mid] < target:
            i = mid + 1
        else:
            return mid
    return ans

#given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
#TC : O(logN)
#SC : O(1)

def findFloor(l,r):
    n=len(l)
    i=0
    j=n-1
    floor=-1
    while i<=j:
        mid=(i+j)//2
        if l[mid]>r:
            j=mid-1
        elif l[mid]<=r:
            floor=mid
            i=mid+1
    return l[floor]

#TC : O(logN)
#SC : O(1)
def findCeil(l,r):
    n=len(l)
    i=0
    j=n-1
    ceil=-1
    while i<=j:
        mid=(i+j)//2
        if l[mid]>=r:
            ceil=mid
            j=mid-1
        elif l[mid]<r:
            i=mid+1
    return l[ceil]

#TC : O(2logN)
#SC : O(1)
def findFloorCeil(l,r):
    return [findFloor(l,r),findCeil(l,r)]

# find the index of the first and last occurrence of the target key
#TC : O(N)
#SC : O(1)
def firstLastOccuranceBruteforce(l,r):
    n=len(l)
    flag=0
    left=-1
    right=-1
    for i in range(n):
        if l[i]==r:
            if flag:
                right=i
            else:
                left=i
                flag=1
    return [left,right]

#TC : O(2logN)
#SC : O(1)
def firstLastOccuranceOptimal(l,r):
    # print(l)
    n=len(l)
    i=0
    j=n-1
    left=-1
    right=-1
    while i<=j:
        mid=(i+j)//2
        if l[mid]>r:
            j=mid-1
        elif l[mid]<r:
            i=mid+1
        else:
            left = mid
            j = mid - 1
    # print(left)
    i = 0
    j = n - 1
    while i<=j:
        mid=(i+j)//2
        if l[mid]>r:
            j=mid-1
        elif l[mid]<r:
            i=mid+1
        else:
            right = mid
            i = mid + 1
    return [left,right]

#find the occurrences of X in the given sorted array
#TC : O(N)
#SC : O(1)
def countOccuranceBruteforce(l,r):
    n=len(l)
    flag=0
    left=-1
    right=-1
    for i in range(n):
        if l[i]==r:
            if flag:
                right=i
            else:
                left=i
                flag=1
    return right+1-left

#TC : O(2logN)
#SC : O(1)
def countOccuranceOptimal(l,r):
    n=len(l)
    i=0
    j=n-1
    left=-1
    right=-1
    while i<=j:
        mid=(i+j)//2
        if l[mid]>r:
            j=mid-1
        elif l[mid]<r:
            i=mid+1
        else:
            left = mid
            j = mid - 1
    i = 0
    j = n - 1
    while i<=j:
        mid=(i+j)//2
        if l[mid]>r:
            j=mid-1
        elif l[mid]<r:
            i=mid+1
        else:
            right = mid
            i = mid + 1
    return right-left+1


#Sorted distinct ele array is rotated at some pivot point that is unknown.
# Find the index at which k is present and if k is not present return -1.
#TC : O(N)
#SC : O(1)
def sortedRotatedArrayoneBruteforce(l,r):
    n=len(l)
    for i in range(n):
        if l[i]==r:
            return i
    return -1

#TC : O(logN)
#SC : O(1)
def sortedRotatedArrayoneOptimal(l,r):
    n=len(l)
    i=0
    j=n-1
    while i<=j:
        mid=(i+j)//2
        if l[mid]==r:
            return mid
        elif l[i]<=l[mid]: #checking if left part is sorted
            if l[i]<=r<=l[mid]:
                j=mid-1
            else:
                i=mid+1
        else:
            if l[mid]<=r<=l[j]:
                i=mid+1
            else:
                j=mid-1
    return -1

#Sorted duplicate ele array is rotated at some pivot point that is unknown.
# Find the index at which k is present and if k is not present return -1.
# same above code may work but it fails in the example
# [1 0 1 1 1]  where we can't find which part is sorted, as low=mid=high , so we just fix that

#TC : O(N)
#SC : O(1)
def sortedRotatedArrayTwoBruteforce(l,r):
    n=len(l)
    for i in range(n):
        if l[i]==r:
            return i
    return -1

#TC : O(logN)
#SC : O(1)
def sortedRotatedArrayTwoOptimal(l,r):
    n=len(l)
    i=0
    j=n-1
    while i<=j:
        mid=(i+j)//2
        if l[mid]==r:
            return mid
        elif l[i]==l[mid] and l[mid]==l[j]:  #just moving low and high onestep so that we can come out of this complex condition and find sorted part somewhere
            i=i+1
            j=j-1
        elif l[i]<=l[mid]: #checking if left part is sorted
            if l[i]<=r<=l[mid]:
                j=mid-1
            else:
                i=mid+1
        else:
            if l[mid]<=r<=l[j]:
                i=mid+1
            else:
                j=mid-1
    return -1

#Sorted array is rotated at some pivot point that is unknown
# find the minimum ele in array

#TC : O(N)
#SC : O(1)
def findMinEleBruteforce(l):
    n=len(l)
    for i in range(1,n):
        if l[i-1]>l[i]:
            return l[i]
    return l[0]

#TC : O(logN)
#SC : O(1)
def findMinEleOptimal(l):
    n=len(l)
    i=0
    j=n-1
    ans=sys.maxsize
    while i<=j:
        mid=(i+j)//2
        if l[i]<=l[mid]:
            ans=min(ans,l[i])
            i=mid+1
        elif l[mid]<=l[j]:
            ans=min(ans,l[mid])
            j=mid-1
    return ans

#TC : O(logN)
#SC : O(1)
def findMinEleOptimaltwo(l):
    n=len(l)
    i=0
    j=n-1
    ans=sys.maxsize
    while i<=j:
        mid=(i+j)//2
        if l[i]<=l[j]:   # when we see both left and right part of mid are sorted means you are in the sorted part , so either you have found the answer or min in this will be answer
            ans=min(ans,l[i])
            return ans
        elif l[i]<=l[mid]:
            ans=min(ans,l[i])
            i=mid+1
        elif l[mid]<=l[j]:
            ans=min(ans,l[mid])
            j=mid-1
    return ans

#Sorted array is rotated at some pivot point that is unknown
# find the how many times array is
#
# rotated to left   --> n-index
# rotated to right   --> index

def findHowManyTimesRotatedBruteforce(l):
    n = len(l)
    for i in range(1, n):
        if l[i-1] > l[i]:
            return n-i
    return n

def findHowManyTimesRotatedOptimal(l):
    n = len(l)
    i = 0
    j = n - 1
    ans = sys.maxsize
    ansIndex=n
    while i <= j:
        mid = (i + j) // 2
        if l[i] <= l[mid]:
            if l[i]<ans:
                ans=l[i]
                ansIndex=i
            i = mid + 1
        elif l[mid] <= l[j]:
            if l[mid] < ans:
                ans = l[mid]
                ansIndex = mid
            j = mid - 1
    return n-ansIndex


# Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

# TC : O(N)
# SC : O(N/2+1)
def singleNumberBrutforce(l):
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]==1:
            return i

#TC : O(N)
#SC : O(1)
def singleNumberBetter(l):
    x=0
    for i in l:
        x=x^i
    return x


# 1,1,2,2,3,3,4,5,5,6,6
# 0,1,2,3,4,5,6,7,8,9,10
# 0 10 -> 5 -> l[4]=l[5] -> right
# 6 10 -> 8 -> l[8]!=l[9] -> left
# 6 7- > 6 -> l[6]!=l[7] -> left
# 6 5 -> break

# TC : O(logN)
#SC: O(1)
def singleNumberOptimal(l):
    n=len(l)
    ans=n
    if n==1:
        return l[0]
    if l[0]!=l[1]:
        return l[0]
    if l[n-1]!=l[n-2]:
        return l[n-1]
    # Here we removed 1st and last element of arr , so that we can avoid more conditions and edge cases easily
    i = 1
    j = n - 2
    while i<=j:
        mid=(i+j)//2
        if l[mid]!=l[mid-1] and l[mid]!=l[mid+1]:
            return l[mid]
        if mid%2==0:
            if l[mid]!=l[mid+1]:
                j=mid-1
            else:
                i=mid+1
        else:
            if l[mid]!=l[mid-1]:
                j=mid-1
            else:
                i=mid+1
        ans=mid
    return l[ans]

# Given an array of length N, peak element is defined as the element greater than both of its neighbors. Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i].

def findPeakBruteforce(l):
    n=len(l)
    if n==1:
        return 0
    if l[0]>l[1]:
        return 0
    if l[n-1]>l[n-2]:
        return n-1
    for i in range(1,n-2):
        if l[i-1]<l[i]>l[i+1]:
            return i

def findPeakOptimal(l):
    n=len(l)
    if n==1:
        return 0
    if l[0]>l[1]:
        return 0
    if l[n-1]>l[n-2]:
        return n-1
    i=1
    j=n-2
    ans=n
    while i<=j:
        mid=(i+j)//2
        if l[mid-1]<l[mid]>l[mid+1]:
            return mid
        elif l[mid-1]<l[mid]:
            i=mid+1
        else:
            j=mid-1
        ans=mid
    return mid