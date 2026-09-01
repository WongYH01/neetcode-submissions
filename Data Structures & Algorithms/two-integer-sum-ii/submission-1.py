class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # L and R, start and end
        # while the sum of L and R dont equals to target
            # check if sum is bigger than target
                # move R down
            # check if sum is smaller
                # move L up

        L, R = 0, len(numbers)-1
        summed = numbers[L] + numbers[R]
        while summed != target:
            if summed > target:
                R-=1
            elif summed < target:
                L+=1
            summed = numbers[L] + numbers[R]
        
        return [L+1,R+1]