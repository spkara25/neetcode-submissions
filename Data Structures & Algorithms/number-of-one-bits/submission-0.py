class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)
        #print(num[2:])
        binary_no = list(num)
        count=0
        #len_binary = len(binary_no)
        for c in binary_no:
            if c == '1':
                count +=1
        return count