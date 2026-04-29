class Solution:
    def reverseWords(self, s: str) -> str:
        words= s.split()
        res=[words.pop() for i in range(len(words))]
        return " ".join(res)