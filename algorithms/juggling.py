# Q: shifting the given array by d times to right
from math import gcd


#arr          : 9 4 2 7 6   , d=3
#index        : 0 1 2 3 4
#index+n      : 3 4 5 6 7
#(index+n)%len: 3 4 0 1 2   , where the present indesx should shift
#arr          : 9 4 2 7 6
#Shiftted arr : 2 7 6 9 4

# TC : O(n)
#space : O(n)
def jugglingBruteforce(arr,d):
    arrlen=len(arr)
    d=d%arrlen
    temp = [0 for i in range(arrlen)]
    for i in range(arrlen):
        k=(i+d)%arrlen
        temp[k]=arr[i]
    print(temp)

#shifting for one index every time for d times

# TC: O(d*n)
#space : O(1)
def jugglingBruteforce2(arr,d):
    arrlen = len(arr)
    d = d % arrlen
    for k in range(d):
        temp=arr[arrlen-1]
        for i in range(arrlen-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
    print(arr)


#TC : O(d+n) - d for temp and n for shifting and replacing
#space : O(d)
def jugglingBetter1(arr,d):
    arrlen=len(arr)
    d=d%arrlen
    temp=[]
    for i in range(arrlen-d,arrlen):
        temp.append(arr[i])
    for i in range(arrlen-1,d-1,-1):
        arr[i]=arr[i-d]
    for i in range(0,d):
        arr[i]=temp[i]
    print(arr)


#arr          : 9 4 2 7 6   , d=3
#index        : 0 1 2 3 4
#arr          : 9 4 2 7 6
#indv reversed: (4 9) (6 7 2) , reverse the elements from arrlen-d to arrlen and rev the elements 0 to d
#total reverse: 2 7 6 9 4 , will be same as ans
#Shiftted arr : 2 7 6 9 4

#TC : O(2n)
# Space : O(1)
def jugglingBetter2(arr,d):
    arrlen=len(arr)
    d=d%arrlen
    # print(arr)
    # print(arr[d-1::-1])
    # print(arr[:d-1:-1])
    arr=arr[d-1::-1]+arr[:d-1:-1]
    print(arr[::-1])


#Using cycle that happpens in shifting
#example : for index shifted by 3 in len of 10 will be
#0-> (0+3) -> 3 -> (3+3) -> 6 -> (6+3) -> 9 -> (9+3)=12%10=2 -> 2 -> (2+3) -> 5 -> (5+3) -> 8 -> (8+3)==11%10=1 -> 1 -> (1+3) -> 4 -> (4+3) -> 7 -> (7+3)=10%10=0
# reached where you start , if you observe it covered all index from 0 to 9

#example : for index shifted by 2 in len of 10 will be
#0-> (0+2) -> 2 -> (2+2) -> 4 -> (4+2) -> 6 -> (6+2) -> (8+2)=10%10=0 ---- end , didn't cover all , now start from next  index
#1 -> (1+2) -> 3 -> (3+2) -> 5 -> (5+2) -> 7 -> (7+2) -> 9 -> (9+2)=11%10=1 -- end , covered all by including both

#which started with O covered all index which are having reminder 0 when len divided by d
#which started with 1 covered all index which are having reminder 1 when len divided by d


#example : for index shifted by 8 in len of 12 will be
#0-> (0+8) -> 8 -> (8+8)=16%12=4 -> 4 -> (4+8)=12%12=0 -- end
#1-> (1+8) -> 9 -> (9+8)=17%12=5 -> 5 -> (5+8)=13%12=1 --end
#2-> (2+8) -> 10 -> (10+8)=18%12=6 -> 6 -> (6+8)=14%12=2 --end
#3-> (3+8) -> 11 -> (11+8)=19%12=7 -> 7 -> (7+8)=15%12=3 --end , covered all index till here


#if you observe they are cycle which are exactly equals to gcd(n,(d%n))

#TC:O(n)
#space: O(1)
def juggling(arr,d):
    arrlen = len(arr)
    d = d % arrlen
    k=gcd(d,arrlen)
    for i in range(k):
        temp=arr[i]
        j=i
        while True:
            t=(j-d)%arrlen   #(j-d) shifting value from which is d index back , so it is right shifting
                             # (j+d) shifting value from which is d index front, so it is left shifting
            if t==i:
                break
            arr[j]=arr[t]
            j=t
            # print(j," ")
        arr[j]=temp
    print(arr)



#left shifting array

#TC : O(d+n) - d for temp and n for shifting and replacing
#space : O(d)
def jugglingBetterLeft1(arr,d):
    arrlen=len(arr)
    d=d%arrlen
    temp=[]
    for i in range(d):
        temp.append(arr[i])
    for i in range(d,arrlen):
        arr[i-d]=arr[i];
    for i in range(arrlen-d,arrlen):
        arr[i]=temp[i-(arrlen-d)]
    print(arr)