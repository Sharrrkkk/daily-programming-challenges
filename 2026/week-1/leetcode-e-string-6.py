class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        result: str = "".join(list(s)[0:k][::-1] + list(s)[k:])
        return result
    
    

def test():
    test: Solution = Solution()
    inputs: list[tuple[str, int]] = [("abcd", 2), ("xyz", 3), ("hey", 1)]
    outputs: list[str] = ["bacd", "zyx", "hey"]
    for input, output in zip(inputs, outputs):
        result: str = test.reversePrefix(*input)
        print("Ok" if (output==result) else ("Fail"))


def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    #tests()
    test()

    # Problem: 3794. Reverse String Prefix
    # Date: 2026-01-09
    # Link: https://leetcode.com/problems/reverse-string-prefix/solutions/7481986/3794_e_py-by-sharrrkkk-x8t6/
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