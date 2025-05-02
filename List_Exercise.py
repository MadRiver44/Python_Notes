"""
Exercise 1: Unique Integers That Sum to Zero

Write a function that takes an integer `n` and returns a list of `n` unique integers that sum up to 0.

Example:
Input: 5
Output: [-2, -1, 0, 1, 2]
"""
# def sum_to_zero(n):
    

"""
Exercise 2: Maximum Product of Two Elements

Given a list of integers, return the maximum product of any two distinct elements after subtracting 1 from each.

Example:
Input: [3, 4, 5, 2]
Output: 16  # (5-1) * (4-1)
"""
def max_product(lst):
    results = sorted(lst, reverse=True)
    return (results[0] - 1) * (results[1] - 1)
# Solution
    # lst.sort()
    # return (lst[-1] - 1) * (lst[-2] - 1)


"""
Exercise 3: Running Sum

Given a list of numbers, return a new list where the i-th element is the sum of the first i+1 elements.

Example:
Input: [1, 2, 3, 4]
Output: [1, 3, 6, 10]
"""
def running_sum(lst):
    count = 0
    results = []
    for num, index in enumerate(lst):
        if index == 0:
            count = 0 + lst[index]
            results.append(count)
        else:
            count = count + lst[index - 1]
            results.append(count)
    return results

# Solution
    # total = 0
    # result = []
    # for num in lst:
    #     total += num
    #     result.append(total)
    # return result



    

"""
Exercise 4: Replace Elements with Greatest on Right

Given a list of integers, replace every element with the greatest element among the elements to its right, and replace the last element with -1.

Example:
Input: [17, 18, 5, 4, 6, 1]
Output: [18, 6, 6, 6, 1, -1]
"""
def greatest_on_right(lst):
    max_val = -1
    # we are starting at the end of the range and stepping down -1 and stopping when we get to -1 (past index 0)
    for i in range(len(lst) -1, -1, -1):
        lst[i], max_val = max_val, max(max_val, lst[i]) #comma operator and multiple assignments and no need for swap function in python
    return lst

"""
Exercise 5: Move Zeroes to End

Write a function that moves all zeroes in a list to the end while maintaining the order of non-zero elements.

Example:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
"""
def move_zeros(lst):
    zeroes = []
    for item in lst:
        if item == 0:
            lst.remove(item)
            zeroes.append(item)
    lst.extend(zeroes)
    return lst
"""
Exercise 6: Find Disappeared Numbers

Given a list of integers from 1 to n (with duplicates), find all the numbers that are missing from the list.

Example:
Input: [4, 3, 2, 7, 8, 2, 3, 1]
Output: [5, 6]
"""
def missing_numbers(nums):
    print(set(range(1, len(nums) + 1)))
    print(set(nums))
# Solution
# The first set creates a range of numbers from 1 - 8
# One can them either use subtraction or difference() method to
# return a new set, elements that are in the first set but not in the second!!!
    return list(set(range(1, len(nums) + 1)) - set(nums))


"""
Exercise 7: Third Maximum Number

Return the third distinct maximum number in the list. If it does not exist, return the maximum number.

Example:
Input: [2, 2, 3, 1]
Output: 1
"""
def third_max_number(nums):
    # constraints: list is [], list is less than 3, all same numbers
    items = set(nums)
    if len(items) < 3:
        return max(items)
    else:
        return list(sorted(items, reverse=True))[2]
        

"""
Exercise 8: Partition Array into Three Parts With Equal Sum

Return True if the array can be partitioned into three non-empty parts with equal sum.

Example:
Input: [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
Output: True
"""
# constraints: the sum of all arrays must be equal, the arrays can be different lengths
# get the total from the array and see if it divides evenly by 3
# if we have a remaider, return false
# else: we use floor divisor operator to get a target sum that the individual arrays must equal
# assign count and temp_sum to 0 initially
# loop over the array until temp_sum equals target
# if it does increment the count as if it was another array and reset temp_sum = 0 ( we are not actually creating arrays as we go)
# when we get to three arrays we are done
def three_equal_arrays(arr):
    total = sum(arr)
    if total % 3 != 0:
        return False
    target = total // 3
    count, temp_sum = 0, 0
    for num in arr:
        temp_sum += num
        if temp_sum == target:
            count += 1
            temp_sum = 0
    return count >= 3



"""
Exercise 9: Maximum Subarray Sum (Kadane's Algorithm)

Write a function that finds the contiguous subarray with the largest sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6  # Subarray: [4,-1,2,1]
"""
# This an example of dynamic programming. Kadane's Algo tracks the maximum sum at each position
# in a one dimensional array, building up to the maximum sum
# Running Time O(n), O(1) space

# if the array consists of all positive integers, the max is the sum of the whole array
# if the array consists of all negative integers, then the solution is any subarray of size 1
# several different subarrays may have the same maximum sum

# The application of this algorithm is useful for genomic sequencing and computer vision


def max_subarray_sum(arr):
    current = maximum = arr[0]
    for num in arr[1:]:
        current = max(num, num + current)
        maximum = max(maximum, current)
    return maximum
        
    
"""
Exercise 10: Sort List by Parity

Return a list where all even integers come before odd integers, preserving relative order within each group.

Example:
Input: [3, 1, 2, 4]
Output: [2, 4, 3, 1]
"""

def sort_list_parity(arr):
    # create an even list and concatenate it with a created odd list
    return [even for even in arr if even % 2 == 0] + [odd for odd in arr if odd % 2 != 0]



    """
Exercise 11: Replace Even Numbers with Their Index

Given a list, replace each even number with its index in the list.

Example:
Input: [5, 8, 7, 6, 10]
Output: [5, 1, 7, 3, 4]
"""
def replace_evens_wtih_index(arr):
    # can place if/else statements in front of for in loop
    # variable assignment is placed before if conditional, with the else conditional, after
    return [index if element % 2 == 0 else element for index, element in enumerate(arr) ]



"""
Exercise 12: Spiral Order

Given a 2D list (matrix), return all elements in spiral order.

Example:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
[1,2,3],
[4,5,6],
[7,8,9]
"""
def spiral_matrix(matrix):
    results = []
    while matrix:
        # we are traversing the outer array and removing the inner arrays by popping
        # them at index 0. Eventually, the 2d array is flattened and we are
        # left with a 1d array of all the elements
        results += matrix.pop(0)
        #results == [1,2,3]
        # if we still have a 2d array and we have an array at index 0
        if matrix and matrix[0]:
            for row in matrix:
                # we go from inner array to inner array popping the last element
                # first row = [4,5,6]
                # which leaves first row [4,5] and [7,8]
                results.append(row.pop())
                # results = [1,2,3,6,9]
            if matrix:
                # print('matrix',matrix) [[4,5], [7,8]]
                results += matrix.pop()[::-1]
                #print('results', results) [1,2,3,6,9,8,7]
            if matrix and matrix[0]:
                # if we have anything left, loop over the last item and reverse it
                for row in matrix[::-1]:
                    results.append(row.pop(0))
    return results
                


"""
Exercise 13: Find All Duplicates

Return a list of all elements that appear more than once.

Example:
Input: [4,3,2,7,8,2,3,1]
Output: [2,3]
"""
def remove_duplicates(arr):
    table = {}
    for item in arr:
        if item not in table:
            table[item] = 1
        else:
            table[item] += 1
    return [elem for elem in table if table[elem] > 1] 
# Solution
# Counter is a dict subclass for counting hashable objects where elements are stored as dictionary
# keys and counts are stored as values. The Counter class is simalar to bags as a data structure
# https://docs.python.org/3/library/collections.html#collections.Counter
# Counter has the ability to remember insertion order
#! add counter info to the md along with common patterns

    from collections import Counter
    return [num for num, count in Counter(nums).items() if count > 1]   
    
    
    

"""
Exercise 14: Count Number of Teams

Given a list of ratings, count the number of teams of 3 people that can be formed where the ratings are strictly increasing or decreasing.

Example:
Input: [2,5,3,4,1]
Output: 3
"""




"""
Exercise 15: First Missing Positive

Given a list of integers, find the smallest missing positive integer.

Example:
Input: [3, 4, -1, 1]
Output: 2
"""
def smallest_postive_int(nums):
    # postive_items = list(set(range(0, len(arr)+ 1)) - set(arr))
    # if 0 in postive_items:
    #     postive_items.remove(0)
    # return min(postive_items)

    # not unxerstanding the plus 2?
    nums = set(nums)
    for i in range(1, len(nums) + 2):
        print(i)
        if i not in nums:
            return i


"""
Exercise 16: Merge Intervals

Given a list of intervals, merge all overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""
def merge_intervals(arr):
    if not arr:
        return []
    # sort the 2d array by index 0 of inner arrays!!!
    # sort with the key arg to specify what we are using to sort with
    # here we are passing a lambda function as a key
    # the lambda takes one arg, x and one expression, x[0]
    # this means that as we are looping on each inner array we are sorting based on index 0
    # of each inner array.
    arr.sort(key=lambda x: x[0])
    # we start with merging the the first array
    merged = [arr[0]]
    # loop over the rest of the inner arrays from index 1 on...
    for current in arr[1:]:
        # create another varaiable, prev, set to the last item in merged
        prev = merged[-1]
        # test if current item in the loop at index 0 < index 1 of prev
        if current[0] <= prev[1]:
            # if so, set prev[1] to the max of current[1] or prev[1]
            prev[1] = max(prev[1], current[1])
        else:
            # if not, just append current
            merged.append(current)
    return merged


"""
Exercise 17: Find Pivot Index

Find the index where the sum of the elements on the left is equal to the sum on the right.

Example:
Input: [1, 7, 3, 6, 5, 6]
Output: 3
"""

def find_pivot(arr):
    total = sum(arr)
    left = 0
    for index, item in enumerate(arr):
        print(total, left, item)
        if left == total - left - item: 
            return index
        left += item
    return -1

"""
Exercise 18: Largest Perimeter Triangle

Return the largest perimeter of a triangle with non-zero area formed from 3 sides in the list.

Example:
Input: [2,1,2]
Output: 5
"""
# A triangle with a non-zero area is one where the three vertices 
# are not collinear, meaning they don't all lie on the same straight line. 
# This results in a closed, two-dimensional shape with a measurable area. 
# area of a triangle is 1/2 b x h

def largest_perimeter(nums):
    # sort nums from largest to smallest [2,2,1]
    nums.sort(reverse=True)
    # why are we doing a range of 1?
    for i in range(len(nums) - 2):
        # if index 0 < index 1 + index 2
        if nums[i] < nums[i+1] + nums[i+2]:
            # add them up
            return nums[i] + nums[i+1] + nums[i+2]
    return 0


"""
Exercise 19: Top K Frequent Elements

Given a list, return the `k` most frequent elements.

Example:
Input: [1,1,1,2,2,3], k=2
Output: [1,2]
"""

from collections import Counter
def k_frequent_elements(arr, k):
    # results = []
    # counter = Counter(arr)
    # items = counter.most_common(k)
    # for item in items:
    #     results.append(item[0])
    # return results
    
    # you use the underscore if you do not need to use the variable
    # This is a convention that tells other programmers that the
    # loop variable isn't actually used
    return [item for _, item in Counter(arr).most_common(k)]



"""
Exercise 20: Maximum Consecutive Ones

Given a binary list, return the maximum number of consecutive 1s.

Example:
Input: [1,1,0,1,1,1]
Output: 3
"""

def max_consecutive_ones(arr):
    count = max_count = 0
    for item in arr:
        if item == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
        
           
           
           
"""
Exercise 21: Count Increasing Triplets

Count the number of increasing subsequences of length 3 in the list.

Example:
Input: [1, 2, 3, 4]
Output: 4  # [1,2,3], [1,2,4], [1,3,4], [2,3,4]
"""

def increasing_subsequence(arr):
    from itertools import combinations
    results = subsequence = []
    combos = combinations(arr, 3)
    for combo in combos:
        subsequence = list(combo)
        results.append(subsequence)
    return len(results)

# Solution
    # count = 0
    # n = len(nums) # 4
    # for i in range(n): # loop over the range (0 - 4)
    #     for j in range(i+1, n): # create another range from outer loop start + 1 to 4, looping over a shorter range (1 - 4)
    #         if nums[i] < nums[j]: # compare the first two items 
    #             for k in range(j+1, n): # create another range from inner loop start + 1 again to 4, another shoter range (2 - 4)
    #                 if nums[j] < nums[k]: # compare the 2nd and 3rd numbers
    #                     count += 1 # if all lines up, increase the count
    # return count
    



"""
Exercise 22: Rotate List by K Steps

Rotate a list to the right by k steps (in-place if possible).

Example:
Input: [1,2,3,4,5,6,7], k=3
Output: [5,6,7,1,2,3,4]
"""

def rotate_by_k(arr, k):
    index = 0
    while k-1 != index - 1:
        item = arr.pop()
        arr.insert(index, item)
        k -= 1
    return arr

# Solution
    # k = k % len(nums) k % len(nums) uses the remainder to section a portion of the array to rotate   
    # return nums[-k:] + nums[:-k]


"""
Exercise 23: Find Minimum in Rotated Sorted Array

Given a rotated sorted array (no duplicates), return the minimum element.

Example:
Input: [3,4,5,1,2]
Output: 1
"""
# use binary search
def find_min(arr):
    left, right = 0, len(arr) - 1 # left = 0, right = len(arr) - 1
    while left < right: # we keep sliding right
        mid = (left + right) // 2 # set the midpoint in the rotated/ sorted array
        if arr[mid] > arr[right]: # if the middle num > the furthest to the right
            left = mid + 1 # set the left most to mid + 1
        else:
            right = mid # move the right most to the mid
    return arr[left]


"""
Exercise 24: Maximum Average Subarray (Fixed Length)

Given a list and integer k, return the maximum average value of any contiguous subarray of length k.

Example:
Input: [1,12,-5,-6,50,3], k=4
Output: 12.75
"""
def max_average_subarray(arr, k):
    # mine feels more intuitive
    start, max_index = 0, len(arr) - k
    results = []
    print('start:', start, 'max_index:', max_index)
    while start != max_index + 1:
        results.append(sum(arr[start:start + k])/ k)
        print(results, start)
        start += 1
    final = sorted(results, reverse=True)
    return final[0]
    
    
    # current = sum(arr[:k]) # we take the first sum, not avg from 0 to k
    # max_sum = current # keep track of the avg
    # for i in range(k, len(arr)): # the range starts at k and stops at the end of the array 4,6
    #     current += arr[i] - arr[i-k] # increment current by 
    #     print('current is:', current, arr[i],arr[i - k] )
    #     max_sum = max(max_sum, current) # reset the max avg
    # return max_sum / k


"""
Exercise 25: Longest Harmonious Subsequence

Return the length of the longest harmonious subsequence where the difference between max and min is exactly 1.

Example:
Input: [1,3,2,2,5,2,3,7]
Output: 5  # [3,2,2,2,3]
"""



"""
Exercise 26: Split Array into Consecutive Subsequences

Return True if the array can be split into subsequences of consecutive numbers of at least length 3.

Example:
Input: [1,2,3,3,4,5]
Output: True
"""
def consecutive_subsequences(arr, k):
    # naive solution that misses 2,3,4 or skipped intervals of 1
    results, subsequence = [], []
    for i in range(0, len(arr)):
        if arr[i] + 1 == arr[i+1] and arr[i+1] + 1 == arr[i+2]:
            subsequence = [arr[i], arr[i+1], arr[i+2]]
            results.append(subsequence)
            print(results)
            if len(results) > 1: 
                return True
        else:
            return False
    return False


"""
Exercise 27: Count Smaller Numbers After Self

For each element, count how many numbers to its right are smaller than it.

Example:
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
"""



"""
Exercise 28: Binary Search Insert Position

Given a sorted list and a target, return the index where the target should be inserted to keep it sorted.

Example:
Input: [1,3,5,6], target=5
Output: 2
"""



"""
Exercise 29: Product of Array Except Self

Return an array where each element is the product of all other elements, without using division.

Example:
Input: [1,2,3,4]
Output: [24,12,8,6]
"""



"""
Exercise 30: Longest Mountain in Array

Find the length of the longest mountain (strictly increasing then decreasing sequence, at least 3 elements).

Example:
Input: [2,1,4,7,3,2,5]
Output: 5  # [1,4,7,3,2]
"""




            

if __name__ == '__main__':
    # print(max_product([1,2,3,4,5]))
    # print(running_sum([1,2,3,4,5,6]))
    # print(greatest_on_right([17, 17, 19, 5, 4, 6, 1]))
    # print(move_zeros([0, 1, 0, 3, 12, 3, 0, 4]))
    # print(missing_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
    # print(third_max_number([4, 2, 2, 3, 1]))
    # print(three_equal_arrays([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
    # print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
    # print(sort_list_parity([3, 1, 2, 4]))
    # print(replace_evens_wtih_index([5, 8, 7, 6, 10]))
    # print(remove_duplicates([4,3,2,7,8,2,3,1]))
    # print(max_consecutive_ones([1,1,0,1,1,1,0,1,1,1,1,1,1]))
    # print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))
    # print(merge_intervals([[2,6],[8,10],[1,3],[15,18]]))
    # print(largest_perimeter([2,1,2]))
    
    print(increasing_subsequence([1,2,3,4]))
    print(rotate_by_k([1,2,3,4,5,6,7], 3))
    print(max_average_subarray([1,12,-5, -6, 50, 3], 4))
    print(consecutive_subsequences([1,2,3,3,4,6,7,8], 3))
    
