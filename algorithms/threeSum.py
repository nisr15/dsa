#sum of three numbers in the given array is the target number

# from algorithms.twoSum import twoSum,twoSumBruteForce2
from algorithms.sortings import mergeSort

#TC : O(n3) - 3 for loops
def threeSumBruteForce(arr,arrlen,target):
    for i in range(arrlen):
        for j in range(i+1,arrlen):
            for k in range(j+1,arrlen):
                if(arr[i]+arr[j]+arr[k]==target):
                    return (i,j,k)
    return ()

#TC : O(n2+nlogn)
# O(n2) - n for iterating i , n for two pointers ( nlogn can be ignored )
def threeSumBurteForce2(arr,arrlen,target):
    for r in range(arrlen):
        k=target-arr[r]
        l=twoSumBruteForce2(arr[r+1:],arrlen-1-r,k)
        if l:
            a,b=l
            return (a+r+1, b+r+1, r)
            # print(a+r+1, b+r+1, r)
    return ()


def threeSumBurteForce3(arr,arrlen,target):
    for r in range(arrlen):
        k=target-arr[r]
        i = r+1
        j = arrlen - 1
        while (i < j):
            if (arr[i] + arr[j] > k):
                j -= 1
            elif (arr[i] + arr[j] < k):
                i += 1
            else:
                return [r,i, j]
    return



#TC : O(nlogn+n2logn) - nlogn - for merge sort ,n2 for two loops , logn for binarys earch
#O(n2logn)
def threeSum(arr,arrlen,target):
    for r in range(arrlen):
        k = target - arr[r]
        l=twoSum(arr[r+1:],arrlen-1-r,k)
        if l:
            a, b = l
            return (a+r+1, b+r+1, r)
    return ()