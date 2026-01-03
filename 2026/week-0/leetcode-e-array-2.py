from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        """
        >>> test: Solution = Solution()
        >>> inputs: list[tuple[list[str], int]] = [(["d","b","c","b","c","a"], 2), (["aaa","aa","a"], 1),
        ...                                    (["a","b","a"], 3)]
        >>> for input in inputs:
        ...     test.kthDistinct(*input)
        'a'
        'aaa'
        ''
        """
        result: list[str] = list(v for v, _ in filter(lambda x: x[1] == 1, Counter(arr).items()))
        return result[k-1] if (len(result) >= k) else ("")
    

def test():
    test: Solution = Solution()
    inputs: list[tuple[list[str], int]] = [(["d","b","c","b","c","a"], 2), (["aaa","aa","a"], 1),
                                            (["a","b","a"], 3)]
    outputs: list[str] = ["a", "aaa", ""]
    for input, output in zip(inputs, outputs):
        result: str = test.kthDistinct(*input)
        print("Ok" if (output==result) else ("Fail"))


def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    tests()
    #test()

    # Problem: 2053. Kth Distinct String in an Array
    # Date: 2026-01-03
    # Link: https://leetcode.com/problems/kth-distinct-string-in-an-array/solutions/7460770/2053_e_py-by-sharrrkkk-d9dh/
    # Notes: