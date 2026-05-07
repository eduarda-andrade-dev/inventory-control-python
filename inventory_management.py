# Disciplina: Engenharia de Software
# Aluno(a): Eduarda Andrade
# Trabalho: Sistema de Controle de Estoque
#-----------------------------------------------------------

# Importa da data atual do usuário
from datetime import datetime

# Dicionário simples para guardar o estoque
estoque = {
    "caderno": 50,
    "caneta": 100,
    "borracha": 60,
    "tesoura": 20
}

# Registra a entrada de um produto
def registrar_entrada():
    print("\n--- ENTRADA DE PRODUTO ---")

    # Pede o produto até o usuário digitar um válido
    while True:
        produto = input("Informe o nome do produto: ").lower().strip() # Transforma o que o usuário digitar em minúsculo e evitar problemas com espaços vazios
        if produto in estoque:
            break
        else:
            print("Erro! Produto não cadastrado. Tente novamente.\n")

    # Pede a quantidade até o usuário digitar um número inteiro válido
    while True:
        try:
            quantidade = int(input("Informe a quantidade recebida: "))

            # Validação de data
            while True:
                data_entrada = input("Informe a data da entrada (DD/MM/AAAA): ")
                try:
                    # Verifica se a data segue o padrão correto
                    datetime.strptime(data_entrada, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Erro! Formato de data inválido. Use o padrão DD/MM/AAAA.\n")


            # Soma a quantidade no estoque
            estoque[produto] = estoque[produto] + quantidade

            print(f"\nSucesso! Entrada de {quantidade}x '{produto}' registrada em {data_entrada}.")
            print(f"Novo saldo: {estoque[produto]}")
            break # Sai do laço
        except ValueError:
            print("Erro! A quantidade informada deve ser um número inteiro. Tente novamente.\n")

# Registra a saída de um produto
def registrar_saida():
    print("\n--- SAÍDA DE PRODUTO ---")

    # Pede o produto até o usuário digitar um válido
    while True:
        produto = input("Informe o nome do produto: ").lower().strip() # Transforma o que o usuário digitar em minúsculo e evitar problemas com espaços vazios
        if produto in estoque:
            break
        else:
            print("Erro! Produto não cadastrado. Tente novamente.\n")

    # Pede a quantidade até o usuário digitar um número inteiro válido
    while True:
        try:
            quantidade = int(input("Informe a quantidade a ser retirada: "))

            # Só permite a movimentação se houver saldo suficiente
            if quantidade <= estoque[produto]:
                responsavel = input("Informe o nome do responsável: ")
                data_saida = datetime.now().strftime("%d/%m/%Y %H:%M")

                # Subtrai a quantidade do estoque
                estoque[produto] = estoque[produto] - quantidade

                print(f"\nSucesso! Saída registrada para {responsavel} em {data_saida}.")
                print(f"Novo saldo: {estoque[produto]}")
                break # Sai do laço após o sucesso
            else:
                print(f"\nErro! Saldo insuficiente! O estoque de '{produto}' é {estoque[produto]}. Tente uma quantidade menor.\n")
                # Aqui ele voltará para o início do laço para pedir a quantidade novamente
        except ValueError:
            print("Erro! A quantidade informada deve ser um número inteiro. Tente novamente.\n")

# Exibe o estoque atual
def exibir_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    for item, qtd in estoque.items():
        print(f"Produto: {item} | Quantidade: {qtd}")

# Menu principal
def menu():
    while True:
        print("\n--------------------------------------")
        print(" SISTEMA DE CONTROLE DE ESTOQUE")
        print(" ALUNA: EDUARDA ANDRADE")
        print("--------------------------------------")
        print("1. Registrar Entrada")
        print("2. Registrar Saída")
        print("3. Visualizar Estoque")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            registrar_entrada()
        elif opcao == '2':
            registrar_saida()
        elif opcao == '3':
            exibir_estoque()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Erro! Opção inválida. Retornando ao menu principal...")

# Inicia o programa, chamando o menu principal
menu()