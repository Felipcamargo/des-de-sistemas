class Quarto:
    def __init__(self, numero, tipo, valor_diaria, disponivel=True):
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel

    def exibir_detalhes(self):
        print(self.numero, self.tipo, self.valor_diaria, "Disponível" if self.disponivel else "Ocupado")

    def reservar(self):
        self.disponivel = False

    def liberar(self):
        self.disponivel = True

    def alterar_preco(self, novo_valor):
        self.valor_diaria = novo_valor
