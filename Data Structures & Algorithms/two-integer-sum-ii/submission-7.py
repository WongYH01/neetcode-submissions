class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # L and R pointer start and end

        # while R > L
            # get the sum
            # check if the sum bigger than target

            # elif sum smaller than target

            # else
                # return 
        L,R = 0, len(numbers)-1

        while R > L:
            summed = numbers[L] + numbers[R]

            if summed > target:
                R -= 1
            elif summed < target:
                L += 1
            else:
                return [L+1,R+1]