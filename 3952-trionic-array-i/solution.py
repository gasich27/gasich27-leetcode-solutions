class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        phase = 0
        up1 = down = up2 = 0

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return False

            if phase == 0:
                if nums[i] > nums[i - 1]:
                    up1 += 1
                else:
                    if up1 == 0:
                        return False
                    phase = 1
                    down += 1

            elif phase == 1:
                if nums[i] < nums[i - 1]:
                    down += 1
                else:
                    if down == 0:
                        return False
                    phase = 2
                    up2 += 1
            else: 
                if nums[i] > nums[i - 1]:
                    up2 += 1
                else:
                    return False

        return up1 > 0 and down > 0 and up2 > 0
