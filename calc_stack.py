from collections import deque

numInteiros = input()

StackNum = deque()

numSeparado = numInteiros.split(" ")

for x in numSeparado:
    StackNum.append(int(x))

print(StackNum)

while StackNum:
    print(StackNum.pop()**2)










