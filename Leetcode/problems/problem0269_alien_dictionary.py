"""
https://leetcode.com/problems/alien-dictionary/
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
Input:
[
 "wrt",
 "wrf",
 "er",
 "ett",
 "rftt"
]
"""
input_list = ["wrt", "wrf", "er", "ett", "rftt"]

def char_list(input_str_list):
  out_char_list= []
  for i in input_str_list:
    if i not in out_char_list:
      out_char_list.append(i)
  return(out_char_list)

# O(n)
letters = char_list(''.join(input_list))


topological_dict = {}
print(letters)

for j in letters:
  after_ltters = []
  for k in input_list:
    if j not in k:
      continue
    all_after_letters_in_word = k.split(j,1)[1]
    after_ltters.append(all_after_letters_in_word)
  
  topological_dict[j] =  let(''.join(after_ltters))

print (topological_dict)



