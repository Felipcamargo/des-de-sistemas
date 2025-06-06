import random
import getpass
from conta import Conta

import csv
def escreverArquivo(agencia, numero, titular, saldo, senha):
    with open('contas. csv', 'a', newline='') as csvfile:
        escritor = csv.writer(csvfile,delimiter=',')
        escritor.writerow([agencia,numero,titular,saldo,senha])

while True:
    print("### CADASTRO DE CONTA BANCÁRIA ###\nDigite os dados necessários:")
    agencia = int(input("Número da agência: "))
    numero = random.randint(10000, 99999)
    titular = input( "Nome completo do cliente: ")
    saldo = float(input("Saldo inicial: "))
    senha = getpass.getpass("Solicite uma nova senha:")
    novaConta = Conta(agencia, numero, titular, saldo, senha)
    escreverArquivo(agencia,numero,titular,saldo, senha)
    print(f'Conta cadastrada com sucesso!\n Número da conta {novaConta.numero}\n')