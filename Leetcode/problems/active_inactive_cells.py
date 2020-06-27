from copy import deepcopy
"""
def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    next_day_states = [0] * 8
    for i in range(8):
        next_day_states[i] = states[i]

    for j in range(days):
        
        for k in range(1, 7):
            print(k)

            next_day_states[k] = states[k-1] ^ states[k+1]

        for i in range(8):
            states[i] = next_day_states[i]
        
        states[0] = 0 
        
        states[7] = 0 
        print(states) 
        #01000100

    return states

# working javascript code 
function cellCompete(states, days)
{
    let cells = states;
let numOfDays = days;

let changeState = (cellarr)=> cellarr.map((cur, idx, arr)=> (arr[idx-1] ||0) + (arr[idx+1] || 0)===1?1:0);

let newCells =cells;
for (let i = 0 ; i <numOfDays; i++) newCells = changeState(newCells);

return newCells
}

"""


class solution:
    def final_state(self, states, days):

        next_day_states = [0] * 8

        for j in range(days):
            next_day_states[0] = states[1]
            next_day_states[7] = states[6]
            for x in range(1, 7):

                if states[x - 1] + states[x + 1] == 1:
                    next_day_states[x] = 1
                else:
                    next_day_states[x] = 0

            for i in range(8):
                states[i] = next_day_states[i]
        return states

    #     for i in range(days):
    #         if i == 0:
    #             curr_states = deepcopy(states)

    #         next_day_states = []

    #         for j in range(8):

    #             if j == 0:
    #                 if curr_states[j + 1] == 0:
    #                     next_day_states.append(0)
    #                 else:
    #                     next_day_states.append(1)
    #             elif j == 7:
    #                 if curr_states[j - 1] == 0:
    #                     next_day_states.append(0)
    #                 else:
    #                     next_day_states.append(1)
    #             else:
    #                 if curr_states[j - 1] == curr_states[j + 1]:
    #                     next_day_states.append(0)
    #                 else:
    #                     next_day_states.append(1)

    #         curr_states = deepcopy(next_day_states)

    #     return curr_states

    # def final_state_1(self, states, days):

    #     for i in renge(days):
    #         if i == 0:
    #             curr_states = deepcopy(states)

    #         next_day_states = []

    #         for j in range(8):

    #             if j == 0:
    #                 if curr_states[j + 1] == 0:
    #                     next_day_states.append(0)
    #                 else:
    #                     next_day_states.append(1)
    #             elif j == 7:
    #                 if curr_states[j - 1] == 0:
    #                     next_day_states.append(0)
    #                 else:
    #                     next_day_states.append(1)
    #             else:
    #                 if curr_states[j - 1] == curr_states[j + 1]:
    #                     next_day_states.append(0)
    #                 else:
    #                     next_day_states.append(1)

    #         curr_states = deepcopy(next_day_states)

    #     return curr_states

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


states = [0, 1, 0, 1, 0, 1, 0, 1]
days = 7
test = solution()

print(test.final_state(states, days))
