class Solution:
    def reverseVowels(self, s: str) -> str:
        vow= [i for i in s if i in "aeiouAEIOU"]
        res=[vow.pop() if i in "aeiouAEIOU" else i for i in s]
        return "".join(res)