class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums array
        # set storing previous first post
        # iterate thru nums with i
            # check if the element not in set
                # get the combined with 0 - sum
                # set L to be next elem and R to be len -1
                # while L < R
                    # if bigger than 0
                        # move right down
                    # elif lesser than 0
                        # move left up
                    # else
                        # add the 3 nums into array into res array
                        # move L up by 1
                        # while L elem was the same as prev L elem and L is still smaller than R 

        nums.sort()
        prev_first = set()
        res_arr = []

        for i in range(len(nums)):
            if nums[i] not in prev_first:
                prev_first.add(nums[i])
                L,R = i+1, len(nums)-1

                while L < R:
                    total = nums[i] + nums[L] + nums[R]
                    if total > 0:
                        R -= 1
                    elif total < 0:
                        L += 1
                    else:
                        res_arr.append([nums[i],nums[L],nums[R]])

                        L += 1
                        while nums[L] == nums[L-1] and L < R:
                            L+=1
        
        return res_arr

