class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row hashmap
        # col hashmap
        # square hashmap
        
        # iterate thru rows with i
            # row map w/ i as key and empty set
            
            # iterate thru columns with j
                # col map w/ j as key and empty set
                # floor divide i and j as square coords and make into tuple

                # bool
                # check if curr elem is not "."
                    # set bool to true
                # check if bool
                    # check if int of elem exists in 
        row_map = {}
        col_map = {}
        sqr_map = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                curr_elem = board[i][j]

                if i not in row_map:
                    row_map[i] = set()
                if curr_elem != "." and curr_elem in row_map[i]:
                    return False
                row_map[i].add(curr_elem)

                if j not in col_map:
                    col_map[j] = set()
                if curr_elem != "." and curr_elem in col_map[j]:
                    return False
                col_map[j].add(curr_elem)
                
                sqr_coords = tuple([i//3,j//3])
                if sqr_coords not in sqr_map:
                    sqr_map[sqr_coords] = set()
                if curr_elem != "." and curr_elem in sqr_map[sqr_coords]:
                    return False
                sqr_map[sqr_coords].add(curr_elem)
        return True





