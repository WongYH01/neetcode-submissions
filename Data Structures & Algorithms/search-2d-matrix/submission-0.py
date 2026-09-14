class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # set L out and R out
        # while L out <= R out
            # get middle out index
            # check if target is bigger than last value
                # L out = mid + 1
            # check if target is smaller than first value
                # R out = mid -1
            # else
                # set L and R based on the mid index array
                # while L<R
                    # get middle
                    # check if ....

        L_out, R_out = 0, len(matrix)-1
        while L_out <= R_out:
            mid_out = (L_out + R_out)//2
            if target > matrix[mid_out][-1]:

                L_out = mid_out+1
            elif target < matrix[mid_out][0]:

                R_out = mid_out-1
            else:


                matrix_in = matrix[mid_out]
                L_in, R_in = 0, len(matrix_in)-1

                while L_in<=R_in:

                    mid_in = (L_in+R_in)//2
                    if matrix_in[mid_in] < target:
                        L_in = mid_in+1
                    elif matrix_in[mid_in] > target:
                        R_in = mid_in-1
                    else:
                        return True
                return False
        return False



