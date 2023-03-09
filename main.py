def twoSum(nums: list[int], target: int):
    for numA in nums:
        for numB in nums:
            if numA == numB:
                continue
            if numA+numB == target:
                index_A = nums.index(numA)
                index_B = nums.index(numB)
                break

    return index_A, index_B

#print('Input: nums = ')

if __name__ == '__main__':
    num = [3,5,7,8]
    target = 15

    print('Input: nums = {}, target = {}'.format(num, target))
    a, b = twoSum(num, target)
    
    print(a ,b)