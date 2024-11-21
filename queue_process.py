from collections import deque


palavras = input()

stackPalavras = deque()

palavraSplit = palavras.split(" ")

for x in palavraSplit:
    stackPalavras.append(x)

print(stackPalavras)

for y in stackPalavras:
    hasO = str(y).find("o")
    if hasO != -1:
        print(y)
            



