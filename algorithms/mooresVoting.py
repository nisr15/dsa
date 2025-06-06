#moores voting algorithm
#Q: Find the most repeated number in the array when that number is >N/2


#TC : O(nlongn + n) - sorting nlogn , iterating over array n
#O(nlogn)
def mostRepeatedNumBruteforce2(arr):
    arr.sort()
    maxCount=0
    c=1
    maxNumber=arr[0]
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            c+=1
        elif c>maxCount:
            maxCount=c
            maxNumber=arr[i]
            c=1   # becasue as i and i+1 is not equal we identified the 1st element of next series s
        # print(maxNumber,maxCount,arr[i],c,arr)
    if c>maxCount:
        maxCount=c
        maxNumber=arr[-1]
    return (maxNumber,maxCount)


#Using map or dictionary
#TC : O(n)
#Space : O(n)
def mostRepeatedNumBruteforce3(arr):
    pass

#TC : O(n) - no space

#basic thing here is a just
# assume if a number is more than n/2 and if we are cancelling count with other numbers which are collectivly <n/2
#so at last count will remain for it
#so to verify at end we check if that num is really >n/2
def moorevoting(arr):
    c=0
    n=len(arr)
    for i in arr:
        if c==0:
            maxNum=i
            c+=1
        else:
            if maxNum!=i:
                c-=1
            else:
                c+=1
    c=0
    for i in arr:
        if maxNum==i:
            c+=1
    if c>(n//2):
        return maxNum
    return -1

