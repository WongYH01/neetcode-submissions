class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row for dupes
        # Check Column for dupes
        # Check the 3x3 for dupes

        # iterate thru each row with i
            # iterate thru each column with j
                # check if the value is a number
                    # check if the key in row dict exists in the first place
                        # 
                    # else
                        # empty set
                        # dump number into set
                        # dump set as value to key
        
        row_dict = {}
        col_dict = {}
        sqr_dict = {}
        for curr_row_index in range(len(board)):
            for curr_col_index in range(len(board[curr_row_index])):
                curr_val = board[curr_row_index][curr_col_index]
                if curr_val == ".":
                    continue
                
                # row
                if curr_row_index in row_dict:
                    if curr_val in row_dict[curr_row_index]:
                        return False
                    else:
                        row_dict[curr_row_index].add(curr_val)
                else:
                    row_dict[curr_row_index] = {curr_val}

                # col
                if curr_col_index in col_dict:
                    if curr_val in col_dict[curr_col_index]:
                        return False
                    else:
                        col_dict[curr_col_index].add(curr_val)
                else:
                    col_dict[curr_col_index] = {curr_val}

                # 3x3
                curr_sqr_row_index = curr_row_index // 3
                curr_sqr_col_index = curr_col_index // 3
                curr_sqr_coords = (curr_sqr_row_index, curr_sqr_col_index)
                if curr_sqr_coords in sqr_dict:
                    if curr_val in sqr_dict[curr_sqr_coords]:
                        return False
                    else:
                        sqr_dict[curr_sqr_coords].add(curr_val)
                else:
                    sqr_dict[curr_sqr_coords] = {curr_val}
        return True