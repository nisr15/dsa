#sum of two numbers in the given array is the target number

from algorithms.sortings import mergeSort
from algorithms.search import binarySearch


#TC : O(n2) - two for loops ,loop within loop
def twoSumBruteForce(arr,arrlen,target):
    for i in range(arrlen):
        for j in range(i+1,arrlen):
            if(arr[i]+arr[j]==target):
                return (i,j)

    return ()

#TC : O(nlogn+n)  - nlogn-merge sorting , n -two pointers
def twoSumBruteForce2(arr,arrlen,target):
    i=0
    j=arrlen-1
    while(i<j):
        if(arr[i]+arr[j]>target):
            j-=1
        elif(arr[i]+arr[j]<target):
            i+=1
        else:
            return [i,j]
    return

# def twoSumBruteForce2(arr,arrlen,target):
#     #when given paramter is unsorted
#     sortedArr=mergeSort(arr,0,arrlen-1)
#     i=0
#     j=arrlen-1
#     while(i<j):
#         if(arr[i]+arr[j]>target):
#             j-=1
#         elif(arr[i]+arr[j]<target):
#             i+=1
#         else:
#             return (i,j)
#     return ()

#TC : O(nlogn+nlogn) - nlogn - for merge sort ,n for iteration , logn for binarys earch
def twoSum(arr,arrlen,target):
    for i in range(arrlen):
        k=target-arr[i]
        ans=binarySearch(arr,k)
        if ans and ans!=i:
            return [i,ans]
    return


# def twoSum(arr,arrlen,target):
#     #when given parameter arr is unsorted
#     sortedArr = mergeSort(arr, 0, arrlen - 1)
#     for i in range(arrlen):
#         k=target-arr[i]
#         ans=binarySearch(arr,k)
#         if ans and ans!=i:
#             return (i,ans)
