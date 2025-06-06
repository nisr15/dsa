#To get largest subarray sum
#Q : Given an array find largest subarray sum
#subarray : segment of array which is continuos
import sys

#TC : O(n3)
def kadaneBruteForce(arr,arrlen):
    ans=-sys.maxsize-1
    left=0
    right=0
    for i in range(arrlen):
        for j in range(i,arrlen):
            sumOfSubArray = 0
            for k in range(i,j+1):
                sumOfSubArray+=arr[k]
            if(ans<sumOfSubArray):
                ans=sumOfSubArray
                left=i
                right=j
    print(left,right,ans)

#TC : O(n3) - using sum func may be , check once
def kadaneBruteForce2(arr,arrlen):
    ans=-sys.maxsize-1
    left=0
    right=0
    for i in range(arrlen):
        sumOfSubArray=0
        for j in range(i,arrlen):
            sumOfSubArray=sum(arr[i:j+1])
            if(ans<sumOfSubArray):
                ans=sumOfSubArray
                left=i
                right=j
    print(left,right,ans)

#TC : O(n2) - carry forwarding sum
def kadaneBruteForce3(arr,arrlen):
    ans=-sys.maxsize-1
    left=0
    right=0
    for i in range(arrlen):
        sumOfSubArray=0
        for j in range(i,arrlen):
            sumOfSubArray+=arr[j]
            if(ans<sumOfSubArray):
                ans=sumOfSubArray
                left=i
                right=j
    print(left,right,ans)

#TC : O(n)
def kadane(arr,arrlen):
    maxSum=-sys.maxsize-1
    curSum=0
    left=0
    right=0
    for i in range(arrlen):
        curSum+=arr[i]
        if (maxSum < curSum):
            maxSum = curSum
            right = i
        if(curSum<0):
            curSum=0
            left=i+1
    # print(left,right,maxSum)
    return [left,right,maxSum]


def kadane2D(arr,row,col):
    left=0
    right=0
    up=0
    down=0
    maxSum=-sys.maxsize-1
    for i in  range(col):
        temp = [0 for u in range(row)]
        for j in range(i,col):
            for k in range(row):
                temp[k]+=arr[k][j]
            tempup,tempdown,tempmaxSum=kadane(temp,row)
            if(maxSum<tempmaxSum):
                maxSum=tempmaxSum
                up=tempup
                down=tempdown
                left=i
                right=j
        # print(up, left, down, right, maxSum)
    print("final",up,left,down,right,maxSum)



