def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    sol = []
    for i in range(len(nums) -2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        if nums[i] > 0:
            break
        j,k = i+1, len(nums)-1
        while(j < k):
            cur = nums[i] + nums[j] + nums[k]
            if cur < 0:
                j+=1
            elif cur > 0:
                k-=1
            else:
                sol.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j+1] == nums[j]:
                    j+=1
                j+=1
    return sol




    return [[1,2]]




def main():
    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
    ]

    for nums, expected in tests:
        result = threeSum(None, nums)
        print(f"nums={nums} -> {result} (expected {expected})")
    # nums = [1,2,3,4]
    # for i in range(len(nums)):
    #     print(i)

if __name__ == "__main__":
    main()
