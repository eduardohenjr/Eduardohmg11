# programa para simular a operação de um terminal bancário, com as seguintes operações:
# saque
# depósito
# histórico de saques e depósitos
# informar o saldo disponível

dic = {100:100,50:100,20:100,10:100,5:100,2:100,1:100}

lista_notas = list(dic.keys())
lista_qtd = list(dic.values())
lista_saques_depositos = []


def saque(valor,saldo):
        if valor >= 1:
            if saldo >= valor:
                lista_saques_depositos.append('-{}'.format(valor))
                for i in range(len(lista_notas)):
                    qtd = valor // lista_notas[i]
                    if qtd >= 1:
                        lista_qtd[i] -= qtd
                        valor = valor % lista_notas[i]
                        saldo_final = saldo - qtd * lista_notas[i]
                        saldo = saldo_final
                print('\nSaque efetuado\n')
            else:
                print('\nSaldo insuficiente\n')
        else:
            print('\nPor favor, Digite um valor maior que ou igual a 1\n ')

lista_soma = []

def deposito(valor,saldo,qtd):
    mult = valor*qtd
    saldo_final = mult + saldo
    if mult > 0:
        lista_soma.append(mult)
    return saldo_final


def historico():
    soma = 0
    if len(lista_soma) > 0 :
        for i in range(len(lista_soma)):
            soma += lista_soma[i]
        lista_saques_depositos.append('+{}'.format(soma))
    if len(lista_saques_depositos) == 0:
        print('\nNenhum valor foi sacado ou depositado ainda\n')
    else:
        print('\nHisórico: {}\n'.format(lista_saques_depositos))


def saldo_disponivel(valor,saldo):
    for i in range(len(lista_notas)):
        qtd = valor // lista_notas[i]
        if qtd >= 1:
            lista_qtd[i] -= qtd
            valor = valor%lista_notas[i]
            saldo_final = saldo - qtd * lista_notas[i]
            saldo = saldo_final
    print('\nSeu saldo é de R${},00\n '.format(saldo))


def main():
    saldo = 1200
    valor = 0
    print('\nDigite S para "sim" ou N para "não"\n')
    continua = input('Deseja começar?\n ')
    while continua == 's' or continua == 'S':
        print('\n1 - Sacar\n2 - Depósito\n3 - Histórico de saques e depósitos\n4 - Saldo_siponível\n')
        opcao = int(input('Digite um número:\n'))
        if opcao == 1:
            valor = int(input('\nDigite o valor que deseja sacar:\n R$'))
            print(saque(valor,saldo))
        elif opcao == 2:
            print('\nSó pode ser desositado esses valores: 100,50,20,10,5,2 e 1\n')
            for i in range(len(lista_notas)):
                qtd = int(input('Quantas notas de {} há? '.format(lista_notas[i])))
                lista_qtd[i] += qtd
                saldo = deposito(lista_notas[i],saldo,qtd)
            print('\nDepósito efetuado')
        elif opcao == 3:
            print(historico())
            lista_soma.clear()
        elif opcao == 4:
            print(saldo_disponivel(valor,saldo))

        print('\nDigite S para "sim" ou N para "não"')
        continua = input('Deseja escolher novamente?\n ')

    print('\nATÉ A PRÓXIMA!!!')
