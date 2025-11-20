import pickle
arq = open('dados.pickle', 'rb')
Contas = pickle.load(arq)

def menu():
    print('\nBom dia! Seja bem vindo(a) ao seu, ao meu, ao nosso melhor banco!')
    print('-' * 70)
    print('Por favor, digite o número da operação que deseja realizar:')
    print('1 - Saque\n2 - Depósito\n3 - Visualização de Saldo\n4 - Simulação de Investimento\n5 - Sair')
    print('-' * 70)
def saque(Contas):
    CCbusca = int(input('Digite o número da conta corrente: '))
    senhabusca = input('Digite a senha: ')
    alt = -1
    for i in range(len(Contas)):
        conta = Contas[i]
        if CCbusca == conta[5] and senhabusca == conta[6]:
            alt = i
            break
    if alt != -1:
        saque = int(input('Digite o valor do saque: '))
        conta = Contas[alt]
        x = int(conta[7])
        valor = x - saque
        if 0 < saque < conta[7]:
            conta = conta[0], conta[1], conta[2], conta[3], conta[4], conta[5], conta[6], valor
            Contas[alt] = conta
            print('Saque realizado com sucesso!')
        else:
            print('O valor escolhido é maior do que seu saldo, tente novamente!')
    else:
        print("Não há contas registradas com esse número de Conta Corrente e/ou senha, tente novamente!")
    return Contas
def depositar(Contas):
    CCbusca = int(input('Digite o número da conta corrente: '))
    senhabusca = input('Digite a senha: ')
    alt = -1
    for i in range(len(Contas)):
        conta = Contas[i]
        if CCbusca == conta[5] and senhabusca == conta[6]:
            alt = i
            break
    if alt != -1:
        print('Deposite um valor de no máximo R$10000,00')
        deposito= int(input('Valor do depósito: '))
        conta = Contas[alt]
        x = int(conta[7])
        valor = x + deposito
        if 0< deposito <10000:
            conta = conta[0], conta[1], conta[2], conta[3], conta[4], conta[5], conta[6], valor
            Contas[alt] = conta
            print('Valor depositado com sucesso!')
        else:
            print('Sua senha não está de acordo com nossos requisitos, reinicie o processo.')
    else:
        print("Não há contas registradas com esse número de Conta Corrente, tente novamente!")
    return Contas
def saldo(Contas, CCbusca, senhabusca):
    listaresultados=[]
    for conta in Contas:
        if CCbusca==conta[5] and senhabusca==conta[6]:
                listaresultados.append(conta)
    return listaresultados

def listarsaldo(Contas):
    for conta in Contas:
        print(f'\tNome: {conta[0]} \t  Conta Corrente: {conta[5]} \t Saldo: {conta[7]} ')

while True:
    menu()
    x = int(input('>>>>> '))
    # --SAQUE
    #CONTA CORRENTE E SENHA, VALOR QUE DESEJA SACAR MAIOR QUE ZERO E DENTRO DO VALOR DA CONTA
    if x==1:
        Contas = saque(Contas)
    # --DEPOSITO
    #CONTA CORRENTE E SENHA, MAIOR QUE ZERO MENOR QUE DEZ MIL
    elif x==2:
        Contas = depositar(Contas)
    # --VISUALIZAÇAO DE SALDO
    #CONTA CORRENTE E SENHA, APARECE O NOME, CONTA CORRENTE E SALDO
    elif x==3:
        CC_busca = int(input('Digite o número da Conta Corrente: '))
        senha_busca = input('Digite sua senha: ')
        resultado = saldo(Contas, CC_busca, senha_busca)
        listarsaldo(resultado)
    # --INVESTIMENTO
    #número de meses do investimento,valor inicial, 1,5% ao mês juros compostos
    #investimento  menor que 1 ano, 1% de taxa de administração, mais que 5 anos taxa deadministração anual  0,5%.
    elif x==4:
        t = int(input('Quantos meses deseja investir?'))
        vi = int(input('Qual o valor do aporte inicial?'))
        tt = t // 12
        tp = t % 12
        M = 0
        if t>=12:
            if tt<5:
                for i in range(0, tt):
                    M = vi * 1.015 ** 12
                    M -= M * 0.01
            else:
                for i in range(0, tt):
                    M = vi * 1.015 ** 12
                    M -= M * 0.005
            if tp==0:
                pass
            else:
                M = M + vi * 1.015 ** tp
        else:
            M = vi * 1.015 ** t
        print(f'Simulando um investimento de juros compostos de {t} meses, com valor inicial de R${vi:.2f} você recolherá como montante final R${M:.2f}!')


    elif x==5:
        exit()
    else:
        print('Por favor digite um número válido!')

    arqsaida = open('dados.pickle', 'wb')
    pickle.dump(Contas, arqsaida)
    arqsaida.close()