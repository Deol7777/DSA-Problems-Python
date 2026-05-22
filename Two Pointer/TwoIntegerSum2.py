from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while ( l < r):
        cur = numbers[l] + numbers[r]
        if cur <  target:
            l+=1
        elif cur > target:
            r-=1
        else:
            return [l+1, r+1]
    return []



    return []

def main():
    # Your program's logic goes here
    tests = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
    ]

    for numbers, target, expected in tests:
        result = twoSum(None, numbers, target)
        print(f"numbers={numbers}, target={target} -> {result} (expected {expected})")


if __name__ == "__main__":
    main()
