nums = input()
nums = nums.split(" ")

def round_array(nums):
    list = []
    for num in nums:
        list.append(round(float(num)))

    return list

print(round_array(nums))