# 	• Pre-storing and Fetching
#
# Ex:
# Q: given an array of integers length Nand give the count for which are given in list of K
#
# Bruteforce :
# 	• Iterating over given array N
# 	• And count using count variable for every integer of K
# 	• TC: O(K * N)
#
# Better:
# Hash Array
# 	• Can we say it as count array
# 	• We take a new array with size of Max(integers in K) +1
# 	• Here we do pre-storing of the count of each integer at index=integer
# 	• And when count is required we fetch from this new Array
# 	• Cons
# 		○ As we are using int array
# 		○ Inside main
# 			§  max we can create an int array (10 pow 6)
# 			§ max we can create an bool array (10 pow 7)
# 		○ Globally
# 			§  max we can create an int array (10 pow 7)
# 			§  max we can create an bool array (10 pow 8)
#
#
#
# Character hashing
#
# Ex:
# Q: given an String of char length N and give the count for char which are given in list of K
#
# Bruteforce :
# 	• Iterating over given array N
# 	• And count using count variable for every integer of K
# 	• TC: O(K * N)
#
#
# Better:
# Character hashing
# 	• Just same as hash array
# 	• But here use ascii values
# 	• So if given string has all lower case, you can da a thing
# 	• Index= ascii(char) - ascii(a)
# 	• And store count accordingly
#
#
# Optimal
# 	• Using pre defined DS like
# 		○ Map, unordered map -  C++
# 		○ Hashmap - Java
# 		○ Dict - Python
#
#
# Map
# 	• Key , value pairs
# 	• It is better than array because we just store what we required
#
# TC:
# 	• Map - Storing and fetching = logn
# 	• Unordered map
# 		○ Avg/best - Storing and fetching = O(1)
# 		○ Worst - Storing and fetching = O(N) - once in a blue moon , when collision occurs (refer how it works page)


## How it works

# Three methods
# 	• Divison Method
# 	• Folding Method
# 	• Mid square method
#
#
# Divison Method
#
# Ex: when hash size is only 10
# 	• Storing the arr[i] count in arr[i]%10
# 	• When you have mutiple numbers at same , linear chaing concept is used
# 	• It is done by linked list
# 	• And while these are linked in linear chaining thoes will be ordered in sorted order
# 	• It will be easy to find and get count
# 	• Collisions
# 		○ When every give number falls into same index and they are all linked in a same linear chain
# 		○ Then search time will take us more time
# 		○ So in that is called collision and in this case we have worst TC

# Q: Problem statement: Given an array, we have found the number of occurrences of each element in the array.

#TC : O(N * N) - N - for 1st for loop , N - for 2nd for loop which is counting
#SC : O(N)
def integersCountBf(l):
    visited=[0 for i in range(len(l))]
    for i in range(len(l)):
        if visited[i]!=1:
            c=1
            visited[i]=1
            for j in range(i+1,len(l)):
                if l[i]==l[j]:
                    visited[j]=1
                    c+=1
            print(l[i],c)


#TC : O(N) - for iterating over N size array and storing and printing
#SC : O(N) - worst case all unique elemnts in given array N , so map size N
def integersCountOptimal(l):
    map ={}
    for i in l:
        if i in map.keys():
            map[i]+=1
        else:
            map[i]=1
    for i in map.keys():
        print(i,map[i])

#TC : O(N*N) - two for loops
#SC : O(N) - visited array
def highAndLowFrequencyBF(l):
    n=len(l)
    maxcontEle=0
    mincontEle=0
    maxCont=0
    minCont=n
    visited = [0 for i in range(len(l))]
    for i in range(len(l)):
        if visited[i] != 1:
            c = 1
            visited[i] = 1
            for j in range(i + 1, len(l)):
                if l[i] == l[j]:
                    visited[j] = 1
                    c += 1
                if c >= maxCont:
                    maxCont = c
                    maxcontEle = l[i]
                if c <= minCont:
                    minCont = c
                    mincontEle = l[i]
                # print(c,mincontEle,minCont,maxcontEle,maxCont,l[i],l[j])
    print(maxcontEle,mincontEle)

#TC : O(N) - loop for storing count of all
#SC : O(N) - visited array
def highAndLowFrequencyOptimal(l):
    n=len(l)
    map = {}
    for i in l:
        if i in map.keys():
            map[i] += 1
        else:
            map[i] = 1
    maxcontEle = 0
    mincontEle = 0
    maxCont = 0
    minCont = n
    for i in map:
        if map[i]>=maxCont:
            maxCont=map[i]
            maxcontEle=i
        if map[i]<=minCont:
            minCont=map[i]
            mincontEle=i
    print(maxcontEle, mincontEle)


