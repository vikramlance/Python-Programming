"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.arr.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        arr = self.arr
        if '.' in word:
            for j in arr:
                if len(j) == len(word):
                    for k in range(len(word)):
                        if word[k] != '.' and word[k] != j[k]:
                            return False
                    return True
                            
        else:
            if word in arr:
                return True
            else:
                return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)