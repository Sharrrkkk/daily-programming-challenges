class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        >>> test: Solution = Solution()
        >>> inputs: list[int] = [3, 5, 15]
        >>> for n in inputs:
        ...     test.fizzBuzz(n)
        ['1', '2', 'Fizz']
        ['1', '2', 'Fizz', '4', 'Buzz']
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        """
        result: list[str] = []
        for n in range(1, n+1):
            if n % 3 == 0 and n % 5 == 0:
                result.append("FizzBuzz")
            elif n % 3 == 0:
                result.append("Fizz")
            elif n % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(n))
        return result
    

def test():
    test: Solution = Solution()
    inputs: list[int] = [3, 5, 15]
    outputs: list[list[str]] = [["1","2","Fizz"], ["1","2","Fizz","4","Buzz"],
            ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]]
    for input, output in zip(inputs, outputs):
        result: list[str] = test.fizzBuzz(input)
        print("Ok" if (output==result) else ("Fail"))


def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    tests()
    #test()

    # Problem: 412. Fizz Buzz
    # Date: 2026-02-14
    # Link: https://leetcode.com/problems/fizz-buzz/solutions/7579865/412_e_py-by-sharrrkkk-8enw/
    # Notes: