import random
i = random.randint(1, 5)

strin = "abcdefg"
print(strin[:i:-1] + "_" + strin[i + 1:-1])