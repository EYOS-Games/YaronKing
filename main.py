
# Creates a list containing 5 lists, each of 8 items, all set to 0
from random import randint

w, h = 8, 5;
Matrix = [[0 for x in range(w)] for y in range(h)]

for i in range(h):
    for j in range(w):
        Matrix[i][j] = randint(0, 1)


for i in range(h):
    for j in range(w):
        print(Matrix[i][j], end='')
    print()

print()
print('Yaron is my one and only king')