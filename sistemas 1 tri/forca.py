palavra = "ESCOLA"
limite_tentativas = len(palavra) + 5

letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_")

contador = 1
while(contador <= limite_tentativas):
    print(letras_acertadas)
    print("tentativas:",contador,"/",limite_tentativas)
    chute = input("Digite e letra: ")

    indice = 0

    for letra in palavra:
        if chute.upper() == letra:
            letras_acertadas[indice] = chute.upper()
        indice = indice +1

    contador = contador + 1

