## Sistema de Gerenciamento Bancário (Python - Console)

Este projeto em Python simula um sistema bancário básico, com interfaces separadas para o **Gerente** e o **Cliente**. O sistema utiliza a biblioteca `pickle` para persistir dados das contas em um arquivo (`dados.pickle`).

### Estrutura do Projeto

O sistema é dividido em dois scripts principais que acessam e manipulam a lista de contas:

1.  **`Gerente.py`**: Funções administrativas (cadastro, busca, alteração de senha).
2.  **`Cliente.py`**: Funções transacionais (saque, depósito, consulta de saldo, simulação de investimento).

### 🗄️ Persistência de Dados

O projeto usa o módulo `pickle` para serializar e salvar a lista de contas (`Contas`) em um arquivo binário chamado **`dados.pickle`**.

* Ao iniciar, o script carrega os dados de `dados.pickle`.
* Após cada operação, os dados modificados são salvos de volta no arquivo.
* A estrutura de uma conta na lista `Contas` é uma tupla com 8 elementos: `(Nome, Profissão, Renda Mensal, Endereço, Telefone, Conta Corrente (CC), Senha, Saldo)`.

---

## 1. Interface do Gerente (`Gerente.py`)

A interface do Gerente foca na manutenção dos dados do cliente e acesso a informações.

### Menu de Serviços
O gerente pode escolher entre as seguintes opções:

* **1 - Cadastramento de conta (`cadastro()`):**
    * Solicita dados pessoais e de contato.
    * Gera um número de **Conta Corrente (CC)** aleatório de 5 ou 6 dígitos (entre 10000 e 100000).
    * O saldo inicial e a senha são vazios.
* **2 - Busca de conta corrente (`busca()` / `listar()`):**
    * Permite buscar contas com base no **Nome Completo** do cliente.
    * Lista as contas encontradas com todos os detalhes cadastrais (exceto senha e saldo).
* **3 - Definição de senha (`alterarsenha()`):**
    * Busca a conta pelo número da **Conta Corrente (CC)**.
    * Define ou altera a senha, exigindo que ela tenha de **4 a 8 caracteres alfanuméricos** (`novasenha.isalnum()==True`).
* **4 - Sair:** Encerra o script.

---

## 2. Interface do Cliente (`Cliente.py`)

A interface do Cliente lida com as transações bancárias e simulações. O acesso às transações requer a **Conta Corrente (CC)** e a **Senha**.

### Menu de Operações
O cliente pode escolher entre as seguintes opções:

* **1 - Saque (`saque()`):**
    * Permite sacar um valor.
    * O valor deve ser maior que zero e menor que o saldo disponível na conta.
* **2 - Depósito (`depositar()`):**
    * Permite depositar um valor.
    * O valor deve ser maior que zero e **menor que R$10.000,00**.
* **3 - Visualização de Saldo (`saldo()` / `listarsaldo()`):**
    * Requer CC e senha para consultar o saldo.
* **4 - Simulação de Investimento:**
    * Simula juros compostos de **1.5% ao mês**.
    * Aplica **taxa de administração** sobre o montante anualizado:
        * 1% de taxa de administração para investimentos menores que 5 anos.
        * 0.5% de taxa de administração para investimentos de 5 anos ou mais.
* **5 - Sair:** Encerra o script.
