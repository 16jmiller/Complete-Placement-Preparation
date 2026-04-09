# Input:   nums = [8, 7, 2, 5, 3, 1] target = 10  
# Output:   Pair found (8, 2) or Pair found (7, 3)    
# Input:   nums = [5, 2, 6, 8, 1, 9] target = 12  
# Output: Pair not found

def pairs_for_target_sort(nums, target):
    # If we sort the array first, we can early return. nlog(n) big o for sort
    nums.sort()
    # Now we can use two pointers to go through the array. If we just used for loops, we could get nlogn,
    # but we wouldn't have short circuit and be able to go through the array in order for n big o
    left_side = 0
    right_side = len(nums) - 1

    found = False

    while left_side < right_side:
        if nums[left_side] + nums[right_side] == target:
            print('Pair found', (nums[left_side], nums[right_side]))
            left_side += 1
            found = True
        elif nums[left_side] + nums[right_side] < target:
            left_side += 1
        else:
            right_side -= 1

    if not found:
        print('No pair found')

# big o of n with hash
def pairs_for_target_hash(nums, target):
    nums_dict = {}
    found = False

    for i, num in enumerate(nums):
        # if the difference is seen before, print the pair
        if target - num in nums_dict:
            print('Pair found', (target - num, num))
            found = True
 
        nums_dict[num] = i
 
    if not found:
        print('Pair not found')

if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    pairs_for_target_hash(nums, target)
    pairs_for_target_sort(nums, target)
    