class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zip up position and speed
        # sort the zipped based on position
        # itermediate stack
        # fleet counter = 0

        # iterate thru zipped
            # get the Time to Target
            # check if stack is empty
                # push TTT into stack
            # elif the stack have stuff and the TTT is > stack element TTT
                # up fleet counter by 1
                # pop the stack
                # push new TTT into stack
        zipped_post_speed = list(zip(position, speed))
        zipped_post_speed.sort(key = lambda curr_veh: curr_veh[0], reverse= True)
        inter_stack = []

        for curr_veh in zipped_post_speed:
            veh_post, veh_speed = curr_veh
            time_to_target = (target - veh_post) / veh_speed
            if not inter_stack:
                inter_stack.append(time_to_target)
            elif inter_stack and time_to_target > inter_stack[-1]:
                inter_stack.append(time_to_target)
        
        fleet_counter = 0
        while inter_stack:
            inter_stack.pop()
            fleet_counter += 1

        return fleet_counter
        
