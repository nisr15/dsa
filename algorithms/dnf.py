#dnf
#sorting 0s,1s,2s(or any threenums) in order without using sorting algorithm

# Sol1
#TC O(nlogn) - merge sort and space 0(n) - temp used in merge sort

# sol2
#TC O(2n) - by using three varibles n- iteration to count , n- to modify the given array into sorted array



# sol3
#TC O(n) - 3 pointers

#This algo works on below rules
#(1) 0 to low-1 = will have 0s
#(2) low to mid-1 = will have 1s
#(3) mid to high = unsorted array
#(4) high+1 to n-1 = will have 2s
#
# Now we need to sort array which is from mid to high
# 0000 1111 01212120021 2222

# So intially as the whole array will be unsorted so mid=0,high=n-1 and as low needs to be low,so low=0
# now by iterating mid we check and sort as per below
# mid can have 0 or 1 or 2
# if mid=0
#     according to rule 1
#     we can swap the 1 at low with 0 at mid , so that part remains sorted
#     so , mid+=1 , low+=1
#
# if mid=1
#     according to rule 2,it is in correct order so
#     mid+=1
#
# if mid=2
#     according to rule 4
#     high also have on value which will be unsorted
#     we can swap the 2 at mid 0 or 1 or 2 at high
#     now mid may have any value from 0|1|2 , so we only change high and perform same operations on mid
#     high-=1



#TC : O(n) - n for iterating by pointers on array
def dnf(nums):
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        # print(low, mid, high, nums)
    return nums