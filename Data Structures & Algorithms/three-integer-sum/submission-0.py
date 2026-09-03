class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # empty res_list
        # iterate thru list of nums
            # check if i is more than 0 and if the previous i elem is the same as current elem
                # continue
            # L, R
            # while R > L
                # get sum
                # if sum > 0
                    # down r
                # elif sum < 0
                    # up L
                # else
                    # append to res_list
                    # up L
                    # while the prev elem of L is the same as curr elem and R>L
                        # up L

        nums.sort()
        res_array = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L, R = i+1, len(nums)-1

            while R > L :
                prod = nums[L]+nums[R]+nums[i]
                if prod > 0:
                    R-=1
                elif prod < 0:
                    L+=1
                else:
                    res_array.append([nums[i],nums[L],nums[R]])
                    L+=1
                    while nums[L] == nums[L-1] and R > L:
                        L+=1
        return res_array
