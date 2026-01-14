class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        """
        >>> test: Solution = Solution()
        >>> inputs: list[list[str]] = [["abc","car","ada","racecar","cool"], ["notapalindrome","racecar"], ["def","ghi"]]
        >>> for input in inputs:
        ...     test.firstPalindrome(input)
        'ada'
        'racecar'
        ''
        """
        result: str = ""
        for word in words:
            if word == word[::-1]:
                result = word
                break
        return result
    

def test():
    test: Solution = Solution()
    inputs: list[list[str]] = [["abc","car","ada","racecar","cool"], ["notapalindrome","racecar"], ["def","ghi"]]
    outputs: list[str] = ["ada", "racecar", ""]
    for input, output in zip(inputs, outputs):
        result: str = test.firstPalindrome(input)
        print("Ok" if (output==result) else ("Fail"))


def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    tests()
    #test()

    # Problem: 2108. Find First Palindromic String in the Array
    # Date: 2026-01-14
    # Link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/solutions/7495322/2108_e_py-by-sharrrkkk-9mp9/
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