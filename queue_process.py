from collections import deque


palavras = input()

stackPalavras = deque()

palavraSplit = palavras.split(" ")

hasO = -1

for x in palavraSplit:
    stackPalavras.appendleft(x)

print(stackPalavras)

for o in range(len(stackPalavras)-1, -1, -1):
    hasO = str(stackPalavras[o]).find("o")
    if hasO != -1:
        print(stackPalavras[o])

# for y in stackPalavras:
#     hasO = str(y).find("o")
#     if hasO != -1:
#         print(y)
            



