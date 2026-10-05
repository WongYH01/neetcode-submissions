class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position,speed))
        zipped = sorted(zipped, key=lambda curr_elem: curr_elem[0], reverse=True)

        tmp_stack = []
        for curr_car in zipped:
            curr_post, curr_speed = curr_car[0],curr_car[1]
            time_to_target = (target-curr_post)/curr_speed

            if (not tmp_stack) or tmp_stack[-1] < time_to_target:
                tmp_stack.append(time_to_target)
        
        return len(tmp_stack)