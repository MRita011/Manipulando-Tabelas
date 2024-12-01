import pandas as pd

def criar_nova_tabela():
    nova_tabela = pd.DataFrame()

    for i in range(1, 4):  # Para 3 tabelas
        print(f"\n--- Configuração para a tabela {i} ---")
        caminho_tabela = input("Digite o caminho do arquivo CSV da tabela: ").strip()

        try:
            tabela = pd.read_csv(caminho_tabela, sep=",")  # Configuração do separador como ";"
            print(f"Tabela {i} carregada com sucesso!")
            print(f"Colunas disponíveis: {list(tabela.columns)}")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")
            continue

        # Perguntar o nome da coluna que contém o ano
        while True:
            coluna_ano = input("Digite o nome da coluna que contém os anos (ou pressione Enter se não houver): ").strip()
            if not coluna_ano:
                print("Nenhuma coluna de ano especificada. Todos os dados serão considerados.")
                break
            elif coluna_ano in tabela.columns:
                try:
                    tabela[coluna_ano] = tabela[coluna_ano].astype(int)  # Garantir que os dados estão no formato numérico
                    if 2020 in tabela[coluna_ano].values:
                        tabela = tabela[tabela[coluna_ano] == 2020]
                        print("Filtrando para dados de 2020.")
                    elif 2021 in tabela[coluna_ano].values:
                        tabela = tabela[tabela[coluna_ano] == 2021]
                        print("2020 não encontrado. Filtrando para dados de 2021.")
                    elif 2019 in tabela[coluna_ano].values:
                        tabela = tabela[tabela[coluna_ano] == 2019]
                        print("2020 e 2021 não encontrados. Filtrando para dados de 2019.")
                    else:
                        print("Nenhum dado para 2020, 2021 ou 2019 encontrado. Todos os dados serão considerados.")
                    break
                except ValueError:
                    print("A coluna de ano contém valores não numéricos. Verifique o arquivo e tente novamente.")
            else:
                print("Coluna de ano inválida. Escolha uma coluna existente ou pressione Enter para ignorar.")

        while True:
            try:
                num_colunas = int(input("Quantas colunas você deseja adicionar da tabela? "))
                if num_colunas <= 0:
                    print("Por favor, insira um número válido.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Insira um número inteiro.")

        for _ in range(num_colunas):
            while True:
                coluna = input("Digite o nome da coluna que deseja adicionar: ").strip()
                if coluna in tabela.columns:
                    novo_nome = input(f"Digite o novo nome para a coluna '{coluna}' (ou pressione Enter para manter o nome atual): ").strip()
                    novo_nome = novo_nome if novo_nome else coluna  # Mantém o nome atual se o usuário não fornecer um novo
                    nova_tabela[novo_nome] = tabela[coluna]
                    break
                else:
                    print("Coluna inválida. Escolha uma coluna existente.")

        encerrar = input("Deseja encerrar a adição de colunas desta tabela? (s/n): ").strip().lower()
        if encerrar == "s":
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
    criar_nova_tabela()
