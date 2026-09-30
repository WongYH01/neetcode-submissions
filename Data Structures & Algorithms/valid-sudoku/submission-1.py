class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row, col and square hashmap
        # iterate the row with i
            # iterate the column with j
                # declare the curr elem

                # row check 
                    # check row hashmap with i key exists
                        # create a new set with i as key
                    # check whether the curr elem already in row map key
                        # return false
                    # else
                        # insert inside

                # col check
                    # check col hashmap with j key exists
                        # create a new set with j as key
                    # check whether the curr elem already in col map key
                        # return false
                    # else
                        # insert inside

                # square check
                    # get the square x_axis by floor div i with 3
                    # get the square y_axis by floor div j with 3
                    # get the coords and make it into a tuple

                    # check if the tuple exist in the square hashmap
                        # create a new set with tuple as key
                    # check whether the curr elem already in square map key
                        # return false
                    # else
                        # insert inside
        
        # return true

        row_map, col_map, sqr_map = {},{},{}
        for i in range(len(board)):
            for j in range(len(board[i])):
                curr_elem = board[i][j]

                if curr_elem == ".":
                    continue

                if i not in row_map:
                    row_map[i] = set()
                if curr_elem in row_map[i]:
                    return False
                row_map[i].add(curr_elem)


                if j not in col_map:
                    col_map[j] = set()
                if curr_elem in col_map[j]:
                    return False
                col_map[j].add(curr_elem)

                sqr_x = i//3
                sqr_y = j//3
                sqr_coord = (sqr_x,sqr_y)
                if sqr_coord not in sqr_map:
                    sqr_map[sqr_coord] = set()
                if curr_elem in sqr_map[sqr_coord]:
                    return False
                sqr_map[sqr_coord].add(curr_elem)
        return True
