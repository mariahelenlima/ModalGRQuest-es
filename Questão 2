#QUESTÃO 2
import datetime
data_atual = datetime.datetime.now()
mes_corrente = data_atual.month
with open('consultores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
aniversariantes_do_mes = []
for linha in linhas:
    dados = linha.strip().split('|')
    nome = dados[0]
    email = dados[1]
    data_nascimento = datetime.datetime.strptime(dados[2], '%d/%m/%Y')
    
    if data_nascimento.month == mes_corrente:
        aniversariantes_do_mes.append(f'{nome}|{email}|{dados[2]}')
nome_arquivo_aniversariantes = f'aniversariantes_{mes_corrente}.txt'
with open(nome_arquivo_aniversariantes, 'w') as arquivo_aniversariantes:
    for aniversariante in aniversariantes_do_mes:
        arquivo_aniversariantes.write(aniversariante + '\n')
