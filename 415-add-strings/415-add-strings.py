class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # fb interview and variations!!!
        return str(sum([int(num1), int(num2)]))
        
# Overview
# Facebook interviewers like this question and propose it in four main variations. The choice of algorithm should be based on the input format:

# Strings (the current problem). Use schoolbook digit-by-digit addition. Note, that to fit into constant space is not possible for languages with immutable strings, for example, for Java and Python. Here are two examples:

# Add Binary: sum two binary strings.

# Add Strings: sum two non-negative numbers in a string representation without converting them to integers directly.

# Integers. Usually, the interviewer would ask you to implement a sum without using + and - operators. Use bit manipulation approach. Here is an example:

# Sum of Two Integers: Sum two integers without using + and - operators.
# Arrays. The same textbook addition. Here is an example:

# Add to Array Form of Integer.
# Linked Lists. Sentinel Head + Textbook Addition. Here are some examples:

# Plus One.

# Add Two Numbers.

# Add Two Numbers II.

