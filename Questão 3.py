#QUESTÃO 3
from datetime import datetime, timedelta
 
def adesao(nome, dt_adm, salario, emprestimo):
    data_atual = datetime.now()
    data_limite = data_atual - timedelta(days=365 * 5)
 
    if dt_adm > data_limite:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return
 
    if emprestimo > 2 * salario:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return
 
    if emprestimo % 2 != 0:
        print("Insira um valor válido!")
        return
 
    opcao = int(input("Escolha uma opção:\n1 - Notas de maior valor\n2 - Notas de menor valor\n3 - Notas meio a meio\n> "))
    switch_case(opcao, emprestimo)
 
def notas_maior_valor(emprestimo):
    print(f"Valor empréstimo: {emprestimo} reais\n")
    print("Notas de maior valor:")
    cedulas = [100, 50]
    for cedula in cedulas:
        quantidade = emprestimo // cedula
        emprestimo %= cedula
        if quantidade > 0:
            print(f"{quantidade} x {cedula} reais")
 
def notas_menor_valor(emprestimo):
    print(f"Valor empréstimo: {emprestimo} reais\n")
    print("Notas de menor valor:")
    cedulas = [20, 10, 5, 2]
    for cedula in cedulas:
        quantidade = emprestimo // cedula
        emprestimo %= cedula
        if quantidade > 0:
            print(f"{quantidade} x {cedula} reais")
 
def notas_mistas(emprestimo):
    print(f"Valor empréstimo: {emprestimo} reais\n")
    metade = emprestimo // 2
    notas_maior_valor(metade)
    print("\nNotas de menor valor:")
    notas_menor_valor(metade)
 
def switch_case(opcao, emprestimo):
    switcher = {
        1: notas_maior_valor,
        2: notas_menor_valor,
        3: notas_mistas
    }
    func = switcher.get(opcao, lambda: "Opção inválida")
    return func(emprestimo)
 
print("SIMULAÇÃO DE EMPRÉSTIMO\n\n")
 
nome = input("Escreva seu nome: ")
dt_adm = input("Digite sua data de admissão (dd/mm/aaaa): ")
data_adm = datetime.strptime(dt_adm, "%d/%m/%Y")
salario = float(input("Informe seu salário atual: "))
emprestimo = int(input("Informe o valor do seu empréstimo: "))
adesao(nome, data_adm, salario, emprestimo)
 
