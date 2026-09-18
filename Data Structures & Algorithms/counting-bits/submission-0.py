class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            c = i
            c_b = bin(c)
            bin_list = list(c_b)
            count = 0
            for a in bin_list:
                if a == '1':
                    count += 1
            l.append(count)
        return l