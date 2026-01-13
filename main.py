from algorithms.search import *
# from algorithms.sortings import *
from algorithms.kadane import *
from algorithms.threeSum import *
from algorithms.twoSum import *
from algorithms.dnf import *
from algorithms.mooresVoting import *
from algorithms.juggling import *
from arrays.easy import *
from arrays.hard import *
from arrays.medium import *
from basicHashing.basicHashing import *
from basicMath.basicMath import *
from basicRecursion.basicRecursion import *
from binarySearch.bsOnOneDimension import *
from sorting.sorting import *

# l=list(map(int,input().split()))
# k=int(input())
# l = [9,23 ,56 ,7 ,2 ,4 ,8 ,1]
# k=2
#
# # Search
# print(linerSearch(l,k))
# print(binarySearch(sorted(l),k))
# print(binarySearchRecurrsion(sorted(l),k,0,len(l)-1))
#
# # Sorting
# bubbleSort(l.copy())
# selectionSort(l.copy())
# insertionSort(l.copy())
# mergeSort(l.copy(),0,len(l)-1)
# quickSort(l.copy(),0,len(l)-1)

# #algorithms

##Kadane
# l=[2, 3, -8, 7, -1, 2, 3]
# # l=[-7,-8,-3,-1,-14]
# kadaneBruteForce(l.copy(),len(l))
# kadaneBruteForce2(l.copy(),len(l))
# kadaneBruteForce3(l.copy(),len(l))
# kadane(l.copy(),len(l))
# flipBits(l.copy(),len(l))
# l=[
#     [2,1,-3,-4,5],
#     [0,6,3,4,1],
#     [2,-2,-1,4,-5],
#     [-3,3,1,0,3]
# ]
# kadane2D(l.copy(),4,5)


#2Sum ##Twosum
# l=[1,5,3,10,7]
# print(twoSumBruteForce(l.copy(),len(l),17))
# print(twoSumBruteForce2(mergeSort(l.copy(),0,len(l)-1),len(l),17))
# print(twoSum(mergeSort(l.copy(),0,len(l)-1),len(l),17))

# #3sum ##threesum
# l=[2,1,10,5,7]
# n=len(l)
# print(threeSumBruteForce(l.copy(),len(l),17))
# arr=mergeSort(l.copy(),0,n-1)
# print(threeSumBurteForce2(arr,len(l),17))
# print(threeSumBurteForce3(arr,len(l),17))
# print(threeSum(arr,len(l),17))


# #DNF Algo
# l=[2,0,2,1,1,0]
# print(dnf(l.copy()))


#moore voting
# l=[1,3,2,1,1,2,2,5,6,2]
# print(mostRepeatedNumBruteforce2(l))


# #juggling algo
# l=[9,4,2,7,1,6]
# jugglingBruteforce(l.copy(),3)
# jugglingBruteforce2(l.copy(),3)
# jugglingBetter1(l.copy(),3)
# jugglingBetter2(l.copy(),3)
# juggling(l.copy(),3)


# # basic maths
# n=9288349
# countDigitsBf(n)
# countDigitsOptimal(n)
# reverseNumber(n)
# checkPalindrom(n)
# n=371
# armstrongNum(n)
# divisorBf(36)
# divisorOptimal(36)
# primnumberBf(13)
# primnumberOptimal(53)
# n1=9
# n2=12
# gcdBf(n1,n2)
# gcdBetter(20,40)
# gcdOptimal(13,71)
# gcdOptimalRec(13,71)



# basic of recursion
# fun()
# funname(6)
# fun1ton(6)
# funnto1(6)
# print(sumRec(7))
# print(factRec(3))
# l=[1,2,3,4,5,6,7,9]
# print(revArrayRec(l.cop(),0,len(l)-1))
# s='TrreeT'
# print(checkPalendromRec(s,0,len(s)-1))
# print("ans",fibonaciRec(4))



# # basicHashing
# l=[10,5,10,15,10,5]
# integersCountBf(l.copy())
# integersCountOptimal(l.copy())
# highAndLowFrequencyBF(l.copy())
# highAndLowFrequencyOptimal(l.copy())



# # Sortings
# l = [9,23 ,56 ,7 ,2 ,4 ,8 ,1]
# n=len(l)
# print(l)
# selectionSort(l.copy())
# bubbleSortBF(l.copy())
# bubbleSortOptimal(l.copy())
# insertionSort(l.copy())
# mergeSort(0,n-1,l.copy())
# recurssiveBubbleSort(l.copy(),n-1)
# recurssiveBubbleSortOptimal(l.copy(),n-1)
# recurssiveInsertionSort(l.copy(),1,n)
# quickSort(l.copy(),0,n-1)


# # Array
# # Easy
# l = [9,23 ,56 ,7 ,2 ,4 ,8 ,1,56]
# largestNum(l.copy())
# secondLargestNumBF(l.copy())
# secondLargestNumBetter(l.copy())
# secondLargestNumOptimal(l.copy())
# print(checkArraySorted(l.copy()))
# l=[1,9,8,3,8,9,3,4,1,3,1]
# l.sort()
# removeDupSortBF(l.copy())
# removeDupSortOptimal(l.copy())
# l = [9,23 ,56 ,7 ,2 ,4 ,8 ,1,56]
# leftRotateByOne(l.copy())
# RotateByKBF(l.copy(),9,'right')
# RotateByKBetter(l.copy(),9,'right')
# RotateByKOptimal(l.copy(),9,'right')
# l=[1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# moveZerosToLastBF(l.copy())
# moveZerosToLastBetter(l.copy())
# moveZerosToLastOptimal(l.copy())
# linerSearch(l,k)
# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[2,3,4,4,5,11,12]
# unionOfSortedArraysBF(l1,l2)
# unionOfSortedArraysOptimal(l1,l2)
# l=[1,2,4,5]
# missingNumInArrayBF(l)
# missingNumInArrayBetter(l,5)
# missingNumInArrayOptimal1(l,5)
# missingNumInArrayOptimal2(l)
# l=[1, 1, 0, 1, 1, 1]
# countMaxConsOnes(l)
# l=[4,1,2,1,2]
# numAppersOnceBF(l)
# numAppersOnceBetter1(l)
# numAppersOnceBetter2(l)
# numAppersOnceOptimal(l)
# l=[2,3,5,1,9]
# l=[1,8,2,3,5]
# k=10
# longestSubarraySumBF1(l,k)
# longestSubarraySumBF2(l,k)
# longestSubarraySumBetter(l,k)
# longestSubarraySumOptimal(l,k)
# l=[-1, 1, 1]
# k=1
# longestSubarraySumNegNumBF(l,k)
# longestSubarraySumNegNumBetter(l,k)
# longestSubarraySumNegNumOptimal(l,k)



# #Medium
# l=[2,1,3,4]
# k=4
# sumOfTwoNumbersBF(l,k)
# sumOfTwoNumbersBetter(l,k)
# sumOfTwoNumbersOptimal(l,k)
# l=[2,0,1]
# n=len(l)
# print(sortingArrayOf012BF(l))
# print(sortingArrayOf012Better(l,n))
# print(sortingArrayOf012Optimal(l,n))
# l=[2,2,1,1,1,2,2]
# n=7
# print(majorityEleBF(l,n))
# print(majorityEleBetter1(l,n))
# print(majorityEleBetter2(l,n))
# print(majorityEleOptimal(l,n))
# l=[-2,1,-3,4,-1,2,1,-5,4]
# l=[-2,-1,-3,-4]
# n=len(l)
# largestSumSubArrayBF(l,n)
# largestSumSubArrayBetter(l,n)
# largestSumSubArrayOptimal(l,n)
# largestSumSubArrayOptimalExtended(l,n)
# l=[1,2,-3,-1,-2,3]
# n=len(l)
# rearrangeArrayEleBySignBF(l,n)
# rearrangeArrayEleBySignOptimal(l,n)
# l=[1,2,4,-4,-5,3]
# n=len(l)
# rearrangeArrayEleBySignType2BF(l,n)
# l=[1,2,3]
# n=len(l)
# nextPermutation(l,n)
# l=[10, 22, 12, 3, 0, 6]
# n=len(l)
# leadersInArrayBF(l,n)
# leadersInArrayOptimal(l,n)
# l=[9,1,4,7,3,-1,0,5,8,-1,6]
# n=len(l)
# longConsSeqinArrBF(l,n)
# longConsSeqinArrBetter(l,n)
# longConsSeqinArrOptimal(l,n)
# l=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# n=len(l)
# m=len(l[0])
# setMarixZeroBF(l,n,m)
# l=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# n=len(l)
# m=len(l[0])
# setMarixZeroBetter(l,n,m)
# l=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# n=len(l)
# m=len(l[0])
# setMarixZeroOptimal(l,n,m)
# l=[[1,2,3],[4,5,6],[7,8,9]]
# n=len(l)
# rotateMatrix90BF(l,n)
# rotateMatrix90Optimal1(l,n)
# l=[[1,2,3],[4,5,6],[7,8,9]]
# n=len(l)
# rotateMatrix90Optimal2(l,n)
# l=[[1, 2, 3, 4 ],
#    [ 5, 6, 7, 8 ],
#    [9, 10, 11, 12 ],
#    [ 13, 14, 15, 16]]
# n=len(l)
# m=len(l[0])
# print(spiralMatrix(l,n,m))
# l=[3, 1, 2, 4]
# k=6
# n=len(l)
# print(noSubArrayBruteForce(l,n,k))
# print(noSubArrayBetter(l,n,k))
# print(noSubArrayOptimal(l,n,k))



# #Hard
# n=5
# print(nthLineOfPascalTriangleBruteForce(n))
# print(nthLineOfPascalTriangleOptimal(n))
# nums= [1, 2, 1, 1, 3, 2, 2]
# print(eleMoreThanBruteForce(nums))
# print(eleMoreThann3Better(nums))
# print(eleMoreThann3Optimal(nums))
# l=[-1,0,1,2,-1,-4]
# n=len(l)
# print(threeSumBruteForce(l,n))
# print(threeSumBetter(l,n))
# print(threeSumOptimal(l,n))
# l=[1,0,-1,0,-2,2]
# target=0
# print(fourSumBruteforce(l,target))
# print(fourSumBetter(l,target))
# print(fourSumOptimal(l,target))
# l=[9, -3, 3, -1, 6, -5]
# n=len(l)
# print(largestSubArraySumWithZeroBruteforce(l,n))
# print(largestSubArraySumWithZeroOptimal(l,n))
# l=[4, 2, 2, 6, 4]
# target=6
# print(noOfSubarraysHavingBitwiseXORBruteforce(l,target))
# print(noOfSubarraysHavingBitwiseXOROptimal(l,target))
# l=[[1,3],[2,6],[8,10],[15,18]]
# print(mergeIntervalsBetter(l))
# print(mergeIntervalsBetter2(l))
# print(mergeIntervalsOptimal(l))
# nums1 = [-5, -2, 4, 5, 0, 0, 0]
# nums2 = [-3, 1, 8]
# m=4
# n=3
# print(mergeTwoSortedArraysWithoutExtraSpace(nums1,nums2,m,n))
# l=[3, 5, 4, 1, 1]
# print(repeatingAndMissingNumbersBruteforce(l))
# print(repeatingAndMissingNumbersBetter(l))
# print(repeatingAndMissingNumbersBetter2(l))
# print(repeatingAndMissingNumbersOptimal(l))
# print(repeatingAndMissingNumbersOptimal2(l))
# l=[5,3,2,1,4]
# n=len(l)
# print(countInversionBruteforce(l,n))
# print(countInversionOptimal(l,n))
# l=[2,4,3,5,1]
# n=len(l)
# print(countReverseBruteforce(l,n))
# print(countReverseOptimal(l,n))


# #binary search
# l=[1,3,6,7,10,12]
# print(binarySearchIterative(l,4))
# print(binarySearchRecurssive(l,4))
# l=[1,2,2,3]
# r=3
# print(lowerBoundBruteforce(l,r))
# print(lowerBoundOptimal(l,r))
# l=[1,2,2,3]
# r=1
# print(upperBoundBruteforce(l,r))
# print(upperBoundOptimal(l,r))
# l=[1,2,4,7]
# r=3
# print(searchInsertPos(l,r))
# l=[3, 4, 4, 7, 8, 10]
# r=9
# print(findFloorCeil(l,r))
# l=[3, 4, 13, 13, 13,13,13,13, 20, 40]
# r=13
# print(firstLastOccuranceBruteforce(l,r))
# print(firstLastOccuranceOptimal(l,r))
# print(countOccuranceBruteforce(l,r))
# print(countOccuranceOptimal(l,r))
# l=[4,5,6,7,0,1,2]
# r=0
# print(sortedRotatedArrayoneBruteforce(l,r))
# print(sortedRotatedArrayoneOptimal(l,r))
# l=[1,0,1,1,1]
# r=0
# print(sortedRotatedArrayTwoBruteforce(l,r))
# print(sortedRotatedArrayTwoOptimal(l,r))
# l=[3,1,2]
# print(findMinEleBruteforce(l))
# print(findMinEleOptimal(l))
# print(findMinEleOptimaltwo(l))
# l=[1,1,2,3,3,4,4,8,8]
# print(singleNumberBrutforce(l))
# print(singleNumberBetter(l))
# print(singleNumberOptimal(l))
l=[1,2,1,3,5,6,4]  # here we have 2 peaks at index 1 and 5
print(findPeakBruteforce(l))
print(findPeakOptimal(l))