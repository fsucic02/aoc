data = open('24_7/input.txt').read().splitlines()

def p2(result, nums):
    for mask in range(3**(len(nums) - 1)):
        current = int(nums[0])
        
        for i in range(len(nums) - 1):
            op = mask % 3
            mask //= 3
            
            if op == 0:
                current += int(nums[i + 1])
            elif op == 1:
                current *= int(nums[i + 1])
            elif op == 2:
                current = int(str(current) + nums[i + 1])
        
        if current == result:
            return result
    
    return 0

solution = 0
for row in data:
    result, nums = row.split(': ')
    result, nums = int(result), nums.split()
    
    solution += p2(result, nums)

print(solution)