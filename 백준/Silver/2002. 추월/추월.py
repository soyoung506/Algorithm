import sys

n = int(input())
carIn = []
carOut = []
tempCar = []
count = 0

for _ in range(n):
    carNum = sys.stdin.readline().strip()
    carIn.append(carNum)

for _ in range(n):
    carNum = sys.stdin.readline().strip()
    carOut.append(carNum)

while carIn:
    carA = carIn.pop()
    carB = carOut[-1]
    while carB in tempCar:
        carOut.pop()
        carB = carOut[-1]
    if carA == carB:
        carOut.pop()
    else:
        count += 1
    tempCar.append(carA)

print(count)
