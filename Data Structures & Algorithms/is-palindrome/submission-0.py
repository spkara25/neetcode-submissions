import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^a-zA-Z]', '', s).lower()
        return string == string[::-1]