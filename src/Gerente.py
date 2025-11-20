import pickle
import random
arq = open('dados.pickle', 'rb')
Contas = pickle.load(arq)

print('\nBom dia!')
def menu():
    print('-'*100)
    print('-Escolha um de seus serviços:')
    print('"Cadastramento de conta - 1" / "Busca de conta corrente - 2" / "Definição de senha - 3" / "Sair - 4"')
    print('-'*100)
def cadastro():
    nome = input('Nome completo-> ')
    prof = input('Profissão-> ')
    renda = input('Renda Mensal-> R$')
    end = input('Endereço-> ')
    tel = input('Telefone-> ')
    CC = random.randint(10000, 100000)
    print('A conta foi registrada com sucesso!')
    print(f'O número da Conta Corrente do(a) cliente {nome} é: {CC}')
    conta = nome, prof, renda, end, tel, CC, '', 0
    return conta
def busca(Contas, nomebusca):
    listaresultados=[]
    for conta in Contas:
        if nomebusca in conta[0]:
            listaresultados.append(conta)
    return listaresultados
def listar(Contas):
    for conta in Contas:
        print(f'Contas associadas a este nome:\n Nome: {conta[0]} \t Profissão: {conta[1]} \t Renda Mensal: {conta[2]} \t Endereço: {conta[3]} \t Telefone: {conta[4]} \t Conta Corrente: {conta[5]}')
def alterarsenha(Contas):
    CCbusca=input('Digite o número da conta corrente que deseja alterar a senha: ')
    alt=-1
    for i in range(len(Contas)):
        conta = Contas[i]
        if CCbusca == conta[5]:
            alt= i
            break
    if alt!=6:
        print('Sua senha deve conter apenas de 4 a 8 caracteres alfanúmericos!')
        novasenha = input('Digite a nova senha: ')
        if 4<=len(novasenha)<=8 and novasenha.isalnum()==True:
            conta = Contas[alt]
            conta = conta[0], conta[1], conta[2], conta[3], conta[4], conta[5], novasenha, conta[7]
            Contas[alt]= conta
            print('Senha registrada com sucesso!')
        else:
            print('Sua senha não está de acordo com nossos requisitos, reinicie o processo.')
    else:
        print("Não há contas registradas com esse número de Conta Corrente, tente novamente!")
    return Contas

while True:
    menu()
    x = int(input('Qual opção você deseja? '))
# --CADASTRAR NOVAS CONTAS
# NOME COMPLETO, PROFISSÃO, RENDA MENSAL, ENDEREÇO E TELEFONE, GERA CONTA CORRENTE COM 5 DIGITOS
    if x == 1:
        conta = cadastro()
        Contas.append(conta)

# --BUSCAR UMA CONTA EXISTENTE
#PEDE NOME PRA BUSCAR CONTA
    elif x == 2:
        nome_busca = input('Digite o nome que deseja buscar: ')
        resultado = busca(Contas, nome_busca)
        listar(resultado)

# --DEFINIR A NOVA SENHA DE UMA CONTA EXISTENTE
#PEDE NUMERO DA CONTA CORRENTE E VERIFICA SE A CONTA EXISTE, SE SIM, NOVA SENHA DE 4 A 8 ALFANUMERICO, REJEITANDO ACENTOS E CARACTERES ESPECIAIS
    elif x == 3:
        Contas = alterarsenha(Contas)

    elif x == 4:
        exit()
    else:
        print('Por favor digite um número válido!')

    arqsaida = open('dados.pickle', 'wb')
    pickle.dump(Contas, arqsaida)
    arqsaida.close()

