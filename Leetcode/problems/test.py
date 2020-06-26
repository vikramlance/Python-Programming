from copy import deepcopy


class solution:
    def final_state(self, states, days):

        next_day_states = [] * 8
        for i in range(8):
            next_day_states[i] = states[i]

        for j in range(days):
            next_day_states[0] = 0 ^ states[1]
            next_day_states[7] = 0 ^ states[6]
            for k in range(1, 7):
                print(k)

                next_day_states[0] = 0 ^ states[1]

        for i in range(days):
            if i == 0:
                curr_states = deepcopy(states)

            next_day_states = []

            for j in range(8):

                if j == 0:
                    if curr_states[j + 1] == 0:
                        next_day_states.append(0)
                    else:
                        next_day_states.append(1)
                elif j == 7:
                    if curr_states[j - 1] == 0:
                        next_day_states.append(0)
                    else:
                        next_day_states.append(1)
                else:
                    if curr_states[j - 1] == curr_states[j + 1]:
                        next_day_states.append(0)
                    else:
                        next_day_states.append(1)

            curr_states = deepcopy(next_day_states)

        return curr_states

    def final_state_1(self, states, days):

        for i in renge(days):
            if i == 0:
                curr_states = deepcopy(states)

            next_day_states = []

            for j in range(8):

                if j == 0:
                    if curr_states[j + 1] == 0:
                        next_day_states.append(0)
                    else:
                        next_day_states.append(1)
                elif j == 7:
                    if curr_states[j - 1] == 0:
                        next_day_states.append(0)
                    else:
                        next_day_states.append(1)
                else:
                    if curr_states[j - 1] == curr_states[j + 1]:
                        next_day_states.append(0)
                    else:
                        next_day_states.append(1)

            curr_states = deepcopy(next_day_states)

        return curr_states


  # wrong answer  
# class Solution:
#     def prisonAfterNDays(self, cells : List[int], N: int) -> List[int]:
        
#         next_day_states = [0] * 8
#         print(next_day_states)
#         print(cells)
        
#         for i in range(8):
#             next_day_states[i] = cells[i]
            
            
#         for i in range(N):
               
#             for j in range(8):
#                 if j == 0:
#                     if cells[j + 1] == 0:
#                         next_day_states[0] = 0
#                     else:
#                         next_day_states[0] = 1
#                 elif j == 7:
#                     if cells[j - 1] == 0:
#                         next_day_states[7] = 0
#                     else:
#                         next_day_states[7] = 1
#                 else:
#                     if cells[j - 1] == cells[j + 1]:
#                         next_day_states[7] = 0
#                     else:
#                         next_day_states[7] = 1

#             for k in range(8):
#                 cells[k] = next_day_states[k]

#         return cells
        


states = []

test = solution()

print(test.is_valid(input_str))
