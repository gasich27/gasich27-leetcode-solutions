class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1

        for _ in range(len(numbers)):
            if (numbers[a] + numbers[b]) < target:
                a += 1
            elif (numbers[a] + numbers[b]) > target:
                b -= 1
            elif (numbers[a] + numbers[b]) == target:
                return [a + 1, b + 1]
            
