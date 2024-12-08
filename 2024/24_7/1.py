data = open('24_7/input.txt').read().splitlines()

solution = 0
for row in data:
    result, nums = row.split(': ')
    result, nums = int(result), nums.split()
    
    for mask in range(2**(len(nums) - 1)):
        current = int(nums[0])

        for i in range(len(nums) - 1):
            if (mask >> i) & 1:
                current *= int(nums[i + 1])
            else:
                current += int(nums[i + 1])
        
        if current == result:
            solution += result
            break

print(solution)
