class Solution:
    """
    >>> test: Solution = Solution()
    >>> inputs: list[tuple[str, str]] = [("abc", "bac"), ("abcde", "edbac")]
    >>> for input in inputs:
    ...     test.findPermutationDifference(*input)
    2
    12
    """
    def findPermutationDifference(self, s: str, t: str) -> int:
        result: int = 0
        cache: dict[str, int] = {char:i for i, char in enumerate(t)}
        for i, char in enumerate(s):
            result += abs(i - cache[char]) 
        return result
    

def test():
    test: Solution = Solution()
    inputs: list[tuple[str, str]] = [("abc", "bac"), ("abcde", "edbac")]
    outputs: list[int] = [2, 12]
    for input, output in zip(inputs, outputs):
        result: int = test.findPermutationDifference(*input)
        print("Ok" if (output==result) else ("Fail"))


def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    tests()
    #test()

    # Problem: 3146. Permutation Difference between Two Strings
    # Date: 2026-01-10
    # Link: https://leetcode.com/problems/permutation-difference-between-two-strings/solutions/7484616/3146_e_py-by-sharrrkkk-ryze/
    # Notes:








"""class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result: str = ""
        cache_s: list[str] = sorted(list(s))
        cache_t: list[str] = sorted(list(s))
        for i in range(len(s)):
            if cache_s[i] != cache_t[i]:
                result = cache_t[i]
                break

        return result
    
    

def test():
    test: Solution = Solution()
    inputs: list[tuple[str, str]] = [("abcd", "abcde"), ("", "y")]
    outputs: list[str] = ["e", "y"]
    for input, output in zip(inputs, outputs):
        result: str = test.findTheDifference(*input)
        print("Ok" if (output==result) else ("Fail"))


def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    #tests()
    test()

    # Problem: 3750. Minimum Number of Flips to Reverse Binary String
    # Date: 2026-01-06
    # Link: 
    # Notes:"""