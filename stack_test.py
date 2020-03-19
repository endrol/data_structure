from utils.stack import Stack


'''a function reverse a string by stack'''
def reverse_string(str):
    temp = Stack()
    str2 = []
    for i in str:
        temp.push(i)
    print(temp.size())
    i = 0
    while temp.size() > 0:
        str2.append(temp.pop())

    return str2

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # valid parentheses
        # first check empty string
        if len(s) == 0:
            return True
        # using stack for check parentheses
        stack = Stack()  # call for a stack structure
        for i in s:
            if i in ['{', '[', '(']:
                stack.push(i)
            elif i in ['}', ']', ')']:
                if stack.size() == 0:
                    return False
                chFromstack = stack.pop()
                if not ((chFromstack == '{' and i == '}')
                        or (chFromstack == '[' and i == ']')
                        or (chFromstack == '(' and i == ')')):
                    # one of the above conditions
                    return False

        return stack.isEmpty()

'''
baseConverter, from decimal base to binary base, or hexadecimal(base 16)
'''
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString




# solution in web
class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


if __name__ == '__main__':
    # print('programming starts')
    # print(reverse_string('hello world'))
    solution = Solution()
    solution2 = Solution2()
    print(solution.isValid('{'))
    print(solution2.isValid('((()((nihaoguapi))))'))

    print(baseConverter(25,16))



