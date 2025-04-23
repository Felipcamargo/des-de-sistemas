palavra = "ESCOLA"
limite_tentativas = len(palavra) + 5
acertou = False
enforcou = False

letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_")

contador = 1
while(not acertou and not enforcou):
    print(letras_acertadas)
    print("tentativas:",contador,"/",limite_tentativas)
    chute = input("Digite e letra: ")

    indice = 0

    for letra in palavra:
        if chute.upper() == letra:
            letras_acertadas[indice] = chute.upper()
        indice = indice +1

        if contador == limite_tentativas:
            enforcou = True
            print("voce perdeu :( \n4 palavra era:",palavra)

        if letras_acertadas.count("_") == 0:
           acertou = True
           print("Parabens voce acertou")
           print(letras_acertadas)

    contador = contador + 1

