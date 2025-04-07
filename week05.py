# print(1+2))
                        # 실제 값이 달라도 오류가 안남
def is_valid_parentheses(expression : str) -> bool: #type hint
    stack = list()
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(is_valid_parentheses(")(1+2))"))
print(is_valid_parentheses("(1+2))"))
print(is_valid_parentheses("(1+2)"))
print(is_valid_parentheses("((3*2)/2)"))