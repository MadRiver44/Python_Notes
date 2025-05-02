# Exercise 1: Unique Integers That Sum to Zero
def sum_zero(n):
    return list(range(1, n // 2 + 1)) + list(range(-1, -n // 2 - 1, -1)) + ([0] if n % 2 else [])


# Exercise 2: Maximum Product of Two Elements
def max_product(nums):
    nums.sort()
    return (nums[-1] - 1) * (nums[-2] - 1)


# Exercise 3: Running Sum
def running_sum(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result


# Exercise 4: Replace Elements with Greatest on Right
def replace_elements(arr):
    max_val = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], max_val = max_val, max(max_val, arr[i])
    return arr


# Exercise 5: Move Zeroes to End
def move_zeroes(nums):
    pos = 0
    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1
    for i in range(pos, len(nums)):
        nums[i] = 0
    return nums


# Exercise 6: Find Disappeared Numbers
def find_disappeared_numbers(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))


# Exercise 7: Third Maximum Number
def third_max(nums):
    unique = sorted(set(nums), reverse=True)
    return unique[2] if len(unique) >= 3 else unique[0]


# Exercise 8: Partition Array into Three Parts With Equal Sum
def can_three_parts_equal_sum(arr):
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


# Exercise 9: Maximum Subarray Sum (Kadane's Algorithm)
def max_subarray(nums):
    current = maximum = nums[0] # assigns the same value to multiple variables
    for num in nums[1:]:
        current = max(num, current + num)
        maximum = max(maximum, current)
    return maximum


# Exercise 10: Sort List by Parity
def sort_by_parity(nums):
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]

# Exercise 11: Replace Even Numbers with Their Index
def replace_evens_with_index(nums):
    return [i if num % 2 == 0 else num for i, num in enumerate(nums)]


# Exercise 12: Spiral Order
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result


# Exercise 13: Find All Duplicates
def find_duplicates(nums):
    from collections import Counter
    return [num for num, count in Counter(nums).items() if count > 1]


# Exercise 14: Count Number of Teams
def count_teams(rating):
    n = len(rating)
    count = 0
    for i in range(n):
        less = greater = 0
        for j in range(i):
            if rating[j] < rating[i]:
                less += 1
            elif rating[j] > rating[i]:
                greater += 1
        for k in range(i+1, n):
            if rating[i] < rating[k]:
                count += less
            elif rating[i] > rating[k]:
                count += greater
    return count


# Exercise 15: First Missing Positive
def first_missing_positive(nums):
    nums = set(nums)
    for i in range(1, len(nums) + 2):
        if i not in nums:
            return i


# Exercise 16: Merge Intervals
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        prev = merged[-1]
        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)
    return merged

# Exercise 17: Find Pivot Index
def pivot_index(nums):
    total = sum(nums)
    left = 0
    for i, num in enumerate(nums):
        if left == total - left - num:
            return i
        left += num
    return -1


# Exercise 18: Largest Perimeter Triangle
def largest_perimeter(nums):
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0


# Exercise 19: Top K Frequent Elements
def top_k_frequent(nums, k):
    from collections import Counter
    return [item for item, _ in Counter(nums).most_common(k)]

# Exercise 20: Maximum Consecutive Ones
def max_consecutive_ones(nums):
    count = max_count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count


# Exercise 21: Count Increasing Triplets
def count_increasing_triplets(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                for k in range(j+1, n):
                    if nums[j] < nums[k]:
                        count += 1
    return count


# Exercise 22: Rotate List by K Steps
def rotate(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


# Exercise 23: Find Minimum in Rotated Sorted Array
def find_min(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# Exercise 24: Maximum Average Subarray (Fixed Length)
def find_max_average(nums, k):
    current = sum(nums[:k]) # we take the first avg from 0 to k
    max_sum = current # keep track of the avg
    for i in range(k, len(nums)): # the range starts at k and stops at the end of the array
        current += nums[i] - nums[i-k] # increment current by 
        max_sum = max(max_sum, current) # reset the max avg
    return max_sum / k


# Exercise 25: Longest Harmonious Subsequence
def find_lhs(nums):
    from collections import Counter
    counts = Counter(nums)
    max_len = 0
    for num in counts:
        if num + 1 in counts:
            max_len = max(max_len, counts[num] + counts[num + 1])
    return max_len


# Exercise 26: Split Array into Consecutive Subsequences
def is_possible(nums):
    from collections import Counter, defaultdict
    freq = Counter(nums)
    append_freq = defaultdict(int)

    for num in nums:
        if freq[num] == 0:
            continue
        if append_freq[num - 1] > 0:
            append_freq[num - 1] -= 1
            append_freq[num] += 1
        elif freq[num + 1] > 0 and freq[num + 2] > 0:
            freq[num + 1] -= 1
            freq[num + 2] -= 1
            append_freq[num + 2] += 1
        else:
            return False
        freq[num] -= 1
    return True


# Exercise 27: Count Smaller Numbers After Self
def count_smaller(nums):
    result = []
    sorted_list = []

    def insert_pos(x):
        left, right = 0, len(sorted_list)
        while left < right:
            mid = (left + right) // 2
            if sorted_list[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left

    for num in reversed(nums):
        idx = insert_pos(num)
        result.append(idx)
        sorted_list.insert(idx, num)
    return result[::-1]


# Exercise 28: Binary Search Insert Position
def search_insert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


# Exercise 29: Product of Array Except Self
def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    left_prod = 1
    for i in range(n):
        res[i] = left_prod
        left_prod *= nums[i]
    right_prod = 1
    for i in reversed(range(n)):
        res[i] *= right_prod
        right_prod *= nums[i]
    return res


# Exercise 30: Longest Mountain in Array
def longest_mountain(arr):
    n = len(arr)
    max_len = 0
    i = 1
    while i < n - 1:
        if arr[i-1] < arr[i] > arr[i+1]:
            left = i
            right = i
            while left > 0 and arr[left-1] < arr[left]:
                left -= 1
            while right < n-1 and arr[right] > arr[right+1]:
                right += 1
            max_len = max(max_len, right - left + 1)
            i = right + 1
        else:
            i += 1
    return max_len
