class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        """
        >>> test: Solution = Solution()
        >>> inputs: list[str] = ["K1:L2", "A1:F1"]
        >>> for input in inputs:
        ...     test.cellsInRange(input)
        ['K1', 'K2', 'L1', 'L2']
        ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']
        """
        cache: list[str] = s.split(":")
        start_n: int = int(cache[0][1:])
        end_n: int = int(cache[1][1:])
        start_l: str = cache[0][0]
        end_l: str = cache[1][0]
        data: list[tuple[str, str]] = [(chr(j), str(i)) for i in range(start_n, end_n + 1) for j in range(ord(start_l), ord(end_l)+1)]
        result: list[str] = ["".join(x) for x in sorted(data, key=lambda x: x[0])] 
        return result
    

def test():
    test: Solution = Solution()
    inputs: list[str] = ["K1:L2", "A1:F1"]
    outputs: list[list[str]] = [["K1","K2","L1","L2"], ["A1","B1","C1","D1","E1","F1"]]
    for input, output in zip(inputs, outputs):
        result: list[str] = test.cellsInRange(input)
        print("Ok" if (output==result) else ("Fail"))


def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    tests()
    #test()

    # Problem: 2194. Cells in a range on an excel sheet
    # Date: 2026-01-02
    # Link: https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/solutions/7457796/2194_e_py-by-sharrrkkk-6czh/
    # Notes: