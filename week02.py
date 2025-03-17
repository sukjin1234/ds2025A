import random

n = random.randrange(1,101)
win = True
for i in range(7,0,-1):
    guess = int(input(f"{i}번 남았습니다. 정답을 입력하세요 : "))
    if guess == n:
        win = True
        break
    else:
        if guess > n:
            print("정답보다 큽니다.")
        else:
            print("정답보다 작습니다.")
        win = False
if win:
    print("정답입니다.")
else:
    print(f"정답은 {n}이였습니다.")
