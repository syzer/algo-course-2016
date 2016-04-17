# python3
import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    fails = []

    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i + 1))
            pass

        if next == ')' or next == ']' or next == '}':
            if opening_brackets_stack and opening_brackets_stack.pop().Match(next):
                pass
            else:
                fails.append(i + 1)

    if len(opening_brackets_stack) == 0 and len(fails) == 0:
        print('Success')
    else:
        if len(fails):
            print(fails[0])
        else:
            print(opening_brackets_stack.pop().position)
