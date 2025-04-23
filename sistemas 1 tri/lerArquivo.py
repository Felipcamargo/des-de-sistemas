palavras = []
arquivo = open("times.txt", "r")
for linha in arquivo:
    print(linha)
    palavras.append(linha.strip())

print(palavras)