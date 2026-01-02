class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        """
        >>> test: Solution = Solution()
        >>> inputs: list[tuple[list[str], list[int]]] = [(["Mary","John","Emma"],[180,165,170]),
        ... (["Alice","Bob","Bob"], [155,185,150])]
        >>> for input in inputs:
        ...     test.sortPeople(*input)
        ['Mary', 'Emma', 'John']
        ['Bob', 'Alice', 'Bob']
        """
        data: list[tuple[str, int]] = sorted([(n, h) for n, h in zip(names, heights)], key=lambda x: x[1], reverse=True)
        return [n for n, _ in data]


def test():
    test: Solution = Solution()
    inputs: list[tuple[list[str], list[int]]]
    inputs = [(["Mary","John","Emma"],[180,165,170]),
               (["Alice","Bob","Bob"], [155,185,150])]
    outputs: list[list[str]] = [["Mary","Emma","John"], ["Bob","Alice","Bob"]]
    for input, output in zip(inputs, outputs):
        result: list[str] = test.sortPeople(*input)
        print("Ok" if (output==result) else ("Fail"))


def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    tests()
    #test()

    # Problem: 2418. Sort the People
    # Date: 2026-01-01
    # Link: https://leetcode.com/problems/sort-the-people/solutions/7454548/2418_e_py-by-sharrrkkk-ytu2/
    # Notes: