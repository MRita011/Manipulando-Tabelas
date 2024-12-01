import pandas as pd

def unir_tabelas():
    nova_tabela = pd.DataFrame()

    while True:  # Laço que permite adicionar tabelas indefinidamente
        print(f"\n--- Configuração para uma nova tabela ---")
        caminho_tabela = input("Digite o caminho do arquivo CSV da tabela: ").strip()

        try:
            tabela = pd.read_csv(caminho_tabela, sep=",")  # Configuração do separador como ";"
            print(f"Tabela carregada com sucesso!")
            print(f"Colunas disponíveis: {list(tabela.columns)}")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")
            continue

        while True:
            try:
                num_colunas = int(input("Quantas colunas você deseja adicionar da tabela? "))
                if num_colunas <= 0:
                    print("Por favor, insira um número válido.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Insira um número inteiro.")

        colunas_selecionadas = []
        for _ in range(num_colunas):
            while True:
                coluna = input("Digite o nome da coluna que deseja adicionar: ").strip()
                if coluna in tabela.columns:
                    colunas_selecionadas.append(coluna)
                    break
                else:
                    print("Coluna inválida. Escolha uma coluna existente.")

        # Adiciona as colunas selecionadas à nova tabela na ordem especificada
        for coluna in colunas_selecionadas:
            novo_nome = input(f"Digite o novo nome para a coluna '{coluna}' (ou pressione Enter para manter o nome atual): ").strip()
            novo_nome = novo_nome if novo_nome else coluna  # Mantém o nome atual se o usuário não fornecer um novo
            nova_tabela[novo_nome] = tabela[coluna]

        # Perguntar se deseja adicionar outra tabela
        continuar = input("Deseja adicionar outra tabela? (s/n): ").strip().lower()
        if continuar != "s":
            break

    # Salvar o resultado final
    nome_arquivo = input("\nDigite o nome para salvar a nova tabela (sem extensão): ").strip()
    caminho_saida = f"{nome_arquivo}.csv"
    try:
        nova_tabela.to_csv(caminho_saida, sep=";", index=False)  # Configuração do separador como ";"
        print(f"\nNova tabela salva com sucesso no arquivo: {caminho_saida}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    unir_tabelas()
