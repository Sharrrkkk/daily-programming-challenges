class Solution:
    def minimumFlips(self, n: int) -> int:
        """
        >>> test: Solution = Solution()
        >>> inputs: list[int] = [7, 10, 6]
        >>> for input in inputs:
        ...     test.minimumFlips(input)
        0
        4
        2
        """
        result: int = 0
        cache: list[str] = list(bin(n)[2:])
        reverse_cache: list[str] = list(cache[::-1])
        for i, char in enumerate(cache):
            if cache == reverse_cache:
                break
            if char != reverse_cache[i]:
                reverse_cache[i] = char
                result += 1
        return result
    

def test():
    test: Solution = Solution()
    inputs: list[int] = [7, 10, 6]
    outputs: list[int] = [0, 4, 2]
    for input, output in zip(inputs, outputs):
        result: int = test.minimumFlips(input)
        print("Ok" if (output==result) else ("Fail"))


def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    tests()
    #test()

    # Problem: 3750. Minimum Number of Flips to Reverse Binary String
    # Date: 2026-01-06
    # Link: 
    # Notes: