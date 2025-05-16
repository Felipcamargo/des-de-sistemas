nome = "Felipe Camargo Pereira"
numero_chamada = 10

print("## BEM VINDO AO SISTEMA ##") 
print("sistema criado por aluno: Felipe Camargo Pereira ", nome, "n° chamada: 10 ", numero_chamada)

altura = 1.79
musica_favorita = "Hungria" 
filme_favorito = "Velozes e furioses"
nota_imdb = 6.8 

altura_usuario = float(input("Digite sua altura: "))
if altura_usuario > altura:
    print("Você é mais alto que o desenvolvedor.")
elif altura_usuario < altura:
     print("Você é mais baixo que o desenvolvedor.") 
else: print("Você tem a mesma altura que o desenvolvedor.")

contador = 0 
gosta_mesma_musica = False 

while contador < 3:
     print("Digite o nome da música que você gosta",  contador, "/ 3:")
     musica = input()
     if musica == musica_favorita:
         gosta_mesma_musica = True 
         contador = contador + 1 
         
if gosta_mesma_musica: 
        print("Você também gosta da minha música favorita!")
else: 
    print("Parece que temos gostos musicais diferentes.")
if gosta_mesma_musica:
    print("Você também gosta da minha música favorita!")
else:
    print("Parece que temos gostos musicais diferentes.")


filmes = []
notas = []

for i in range(3):
    filme = input("Digite o nome do filme " + str(i+1) + ": ")
    nota = float(input("Digite a nota do filme " + filme + " no IMDb: "))
    
    filmes.append(filme)
    notas.append(nota)

for i in range(3):
    if filmes[i] == filme_favorito:
        print("O filme " + filmes[i] + " é o meu filme favorito!")
    elif notas[i] > nota_imdb:
        print("O filme " + filmes[i] + " tem uma nota maior que o meu filme favorito!")
    else:
        print("O filme " + filmes[i] + " tem uma nota menor que o meu filme favorito!")
