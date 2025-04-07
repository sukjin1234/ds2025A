# print(1+2))

baskets = {"]":"[","}":"{",")":"("}
                        # 실제 값이 달라도 오류가 안남
def is_valid_parentheses(expression : str) -> bool: #type hint
    stack = list()
    for letter in expression:
        if letter in baskets.values():
            stack.append(letter)
        if letter in baskets.keys():
            if len(stack) == 0:
                return  False
            result = stack.pop()
            if baskets.get(letter) != result:
                return False

    return len(stack) == 0

print(is_valid_parentheses("[(1+2])"))
print(is_valid_parentheses("(1+2))"))
print(is_valid_parentheses("(1+2)"))
print(is_valid_parentheses("((3*2)/2)"))