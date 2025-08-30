import re


def check_parentheses(a_string):
    brackets = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    stack = []
    for c in a_string:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack or stack.pop() != brackets[c]:
                return False
    return not stack


if __name__ == '__main__':
    # print(check_parentheses("()[]{}"))
    assert check_parentheses("([)]") is False
    assert check_parentheses("()[]{}") is True
    assert check_parentheses("aasd()asd[asd]{}") is True
    assert check_parentheses("(]") is False
