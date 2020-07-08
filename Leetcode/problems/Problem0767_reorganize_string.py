
class Solution:
    def reorganizeString(self, S: str) -> str:

        S = list(S)

        for i in range(1, len(S) - 1):

            if S[i] == S[i - 1]:

                for j in range(i + 1, len(S)):
                    if S[j] != S[i]:
                        S[i], S[j] = S[j], S[i]
                        break
                    if j == len(S) - 1:
                        for k in range(1, i - 1):
                            if S[k] != S[i] and S[k - 1] != S[i]:
                                curr_element = S.pop(i)
                                S.insert(k, curr_element)
                                break
                            if k == i - 2:
                                return ""

        if S[-1] == S[-2]:
            if S[-1] != S[0]:
                last_element = S.pop()
                S.insert(0, last_element)
            else:
                for k in range(1, len(S) - 2):
                    if S[k] != S[-1] and S[k - 1] != S[-1]:
                        curr_element = S.pop(-1)
                        S.insert(k, curr_element)
                        break
                    if k == len(S) - 3:
                        return ""

        return ''.join(S)
