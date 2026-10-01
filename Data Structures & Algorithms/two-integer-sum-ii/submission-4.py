class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R = 0, len(numbers)-1
        summed = numbers[L] + numbers[R]

        while summed != target:
            if summed < target:
                L+=1
            else:
                R-=1
            summed = numbers[L] + numbers[R]

        return[L+1, R+1]