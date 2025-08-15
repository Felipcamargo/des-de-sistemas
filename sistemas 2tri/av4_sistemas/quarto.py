from quarto import Quarto

q = Quarto(101, "Casal", 200, True)
q.exibir_detalhes()
q.reservar()
q.exibir_detalhes()
q.liberar()
q.alterar_preco(250)
q.exibir_detalhes()
