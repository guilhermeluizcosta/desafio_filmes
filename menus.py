from models.generos import Genero
from models.filmes import Filme
import os

def menu_generos():
    print("\n--- Gerenciar Gêneros ---")
    print("1. Listar Gêneros")
    print("2. Buscar Gênero por ID")
    print("3. Adicionar Gênero")
    print("4. Atualizar Gênero")
    print("5. Deletar Gênero")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def menu_filmes():
    print("\n--- Gerenciar Filmes ---")
    print("1. Listar Filmes")
    print("2. Buscar Filme por ID")
    print("3. Adicionar Filme")
    print("4. Atualizar Filme")
    print("5. Deletar Filme")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def gerenciar_generos():
    limpar_tela()
    while True:
        opcao = menu_generos()
        if opcao == "1":
            generos = Genero.listar()
            if not generos:
                print("Nenhum gênero cadastrado.")
            else:
                for g in generos:
                    print(f"[{g.id}] {g.nome}")
            input("Pressione Enter para continuar...")
            limpar_tela()
                    
        elif opcao == "2":
            while True:
                id_busca_str = input("ID do gênero: ")
                try:
                    id_busca = int(id_busca_str)
                    if id_busca <= 0:
                        print("ID inválido. Por favor, insira um número inteiro positivo.")
                    else:
                        g = Genero.buscar_por_id(id_busca)
                        print(f"[{g.id}] {g.nome}" if g else "Gênero não encontrado.")
                        input("Pressione Enter para continuar...")
                        limpar_tela()
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para o ID.")
            
        elif opcao == "3":
            nome = input("Nome do gênero: ")
            try:
                novo = Genero(nome=nome)
                novo.salvar()
                print("Cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
            input("Pressione Enter para continuar...")
            limpar_tela()
                
        elif opcao == "4":
            while True:
                id_atualizar_str = input("ID do gênero a atualizar: ")
                try:
                    id_atualizar = int(id_atualizar_str)
                    if id_atualizar <= 0:
                        print("ID inválido. Por favor, insira um número inteiro positivo.")
                    else:
                        g = Genero.buscar_por_id(id_atualizar)
                        if g:
                            novo_nome = input(f"Novo nome para \'{g.nome}\': ")
                            try:
                                g.nome = novo_nome
                                g.salvar()
                                print("Atualizado com sucesso!")
                            except ValueError as e:
                                print(f"Erro: {e}")
                            input("Pressione Enter para continuar...")
                            limpar_tela()
                        else:
                            print("Gênero não encontrado.")
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para o ID.")

        elif opcao == "5":
            while True:
                id_del_str = input("ID do gênero a deletar: ")
                try:
                    id_del = int(id_del_str)
                    if id_del <= 0:
                        print("ID inválido. Por favor, insira um número inteiro positivo.")
                    else:
                        g = Genero.buscar_por_id(id_del)
                        if g:
                            try:
                                g.deletar()
                                print("Deletado com sucesso!")
                            except ValueError as e:
                                print(f"Erro: {e}")
                            input("Pressione Enter para continuar...")
                            limpar_tela()
                        else:
                            print("Gênero não encontrado.")
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para o ID.")
                
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def gerenciar_filmes():
    limpar_tela()
    while True:
        opcao = menu_filmes()
        if opcao == '1':
            filmes = Filme.listar()
            if not filmes:
                print("Nenhum filme cadastrado")
            else:
                    for f in filmes:
                        avaliacao_exibicao = f.avaliacao if f.avaliacao is not None else "Sem avaliação"
                        print(f"[{f.id}] {f.nome} - {f.duracao}min - Lançamento: {f.data_lancamento} - Gênero: {f.genero_nome} - Avaliação: {avaliacao_exibicao}")
            input("Pressione Enter para continuar...")
            limpar_tela()
                        
        elif opcao == "2":  
            while True:
                id_busca_str = input("ID do filme: ")
                try:
                    id_busca = int(id_busca_str)
                    if id_busca <= 0:
                        print("ID inválido. Por favor, insira um número inteiro positivo.")
                    else:
                        f = Filme.buscar_por_id(id_busca)
                        if f:
                            sinopse_exibicao = f.sinopse if f.sinopse else "Sem sinopse"
                            avaliacao_exibicao = f.avaliacao if f.avaliacao is not None else "Sem avaliação"
                            print(f"[{f.id}] {f.nome} - {f.duracao}min - Lançamento: {f.data_lancamento} - Gênero: {f.genero_nome} - Avaliação: {avaliacao_exibicao}\nSinopse: {sinopse_exibicao}")
                        else:
                            print("Filme não encontrado.")
                        input("Pressione Enter para continuar...")
                        limpar_tela()
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para o ID.")
        
        elif opcao == "3":  
            nome = input("Nome: ")
            while True:
                try:
                    duracao = int(input("Duração (minutos): "))
                    if duracao <= 0:
                        print("Duração inválida. Deve ser um número inteiro positivo.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número inteiro para a duração.")

            while True:
                data_lanc = input("Data de lançamento (YYYY-MM-DD): ")
                try:
                    if not data_lanc:
                        print("A data de lançamento não pode ser vazia.")
                    else:
                        break
                except ValueError:
                    print("Formato de data inválido. Use YYYY-MM-DD.")

            while True:
                try:
                    genero_id = int(input("ID do gênero: "))
                    if genero_id <= 0:
                        print("ID do gênero inválido. Deve ser um número inteiro positivo.")
                    elif not Genero.buscar_por_id(genero_id):
                        print("Gênero não encontrado. Por favor, insira um ID de gênero existente.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número inteiro para o ID do gênero.")

            while True:
                avaliacao_str = input("Avaliação (0.5 a 5.0) [opcional]: ")
                if not avaliacao_str:
                    avaliacao = None
                    break
                try:
                    avaliacao = float(avaliacao_str)
                    if not (0.5 <= avaliacao <= 5.0):
                        print("Avaliação inválida. Deve estar entre 0.5 e 5.0.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para a avaliação.")
            sinopse = input("Sinopse [opcional]: ")
            try:
                f = Filme(nome=nome, duracao=duracao, data_lancamento=data_lanc, genero_id=genero_id, avaliacao=avaliacao, sinopse=sinopse)
                f.salvar()
                print("Filme cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
            input("Pressione Enter para continuar...")
            limpar_tela()

        elif opcao == "4":  
            while True:
                id_atualizar_str = input("ID do filme a atualizar: ")
                try:
                    id_atualizar = int(id_atualizar_str)
                    if id_atualizar <= 0:
                        print("ID inválido. Por favor, insira um número inteiro positivo.")
                    else:
                        f = Filme.buscar_por_id(id_atualizar)
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para o ID.")
            if f:
                nome = input(f"Nome [{f.nome}]: ") or f.nome
                while True:
                    duracao_str = input(f"Duração [{f.duracao}]: ")
                    if not duracao_str:
                        duracao = f.duracao
                        break
                    try:
                        duracao = int(duracao_str)
                        if duracao <= 0:
                            print("Duração inválida. Deve ser um número inteiro positivo.")
                        else:
                            break
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número inteiro para a duração.")
                while True:
                    data_lanc_str = input(f"Data de lançamento [{f.data_lancamento}]: ")
                    if not data_lanc_str:
                        data_lanc = f.data_lancamento
                        break
                    try:
                        if not data_lanc_str:
                            print("A data de lançamento não pode ser vazia.")
                        else:
                            data_lanc = data_lanc_str
                            break
                    except ValueError:
                        print("Formato de data inválido. Use YYYY-MM-DD.")
                while True:
                    genero_id_str = input(f"ID do gênero [{f.genero_id}]: ")
                    if not genero_id_str:
                        genero_id = f.genero_id
                        break
                    try:
                        genero_id = int(genero_id_str)
                        if genero_id <= 0:
                            print("ID do gênero inválido. Deve ser um número inteiro positivo.")
                        elif not Genero.buscar_por_id(genero_id):
                            print("Gênero não encontrado. Por favor, insira um ID de gênero existente.")
                        else:
                            break
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número inteiro para o ID do gênero.")
                while True:
                    avaliacao_str = input(f"Avaliação [{f.avaliacao}]: ")
                    if not avaliacao_str:
                        avaliacao = f.avaliacao
                        break
                    try:
                        avaliacao = float(avaliacao_str)
                        if not (0.5 <= avaliacao <= 5.0):
                            print("Avaliação inválida. Deve estar entre 0.5 e 5.0.")
                        else:
                            break
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número para a avaliação.")
                sinopse = input(f"Sinopse [{f.sinopse}]: ") or f.sinopse
                try:
                    f.nome = nome
                    f.duracao = duracao
                    f.data_lancamento = data_lanc
                    f.genero_id = genero_id
                    f.avaliacao = avaliacao
                    f.sinopse = sinopse
                    f.salvar()
                    print("Filme atualizado com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")
                input("Pressione Enter para continuar...")
                limpar_tela()
            else:
                print("Filme não encontrado.")

        elif opcao == "5":  
            while True:
                id_del_str = input("ID do filme a deletar: ")
                try:
                    id_del = int(id_del_str)
                    if id_del <= 0:
                        print("ID inválido. Por favor, insira um número inteiro positivo.")
                    else:
                        f = Filme.buscar_por_id(id_del)
                        if f:
                            try:
                                f.deletar()
                                print("Filme deletado com sucesso!")
                            except ValueError as e:
                                print(f"Erro: {e}")
                            input("Pressione Enter para continuar...")
                            limpar_tela()
                        else:
                            print("Filme não encontrado.")
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para o ID.")
        
        elif opcao == "0":
            break
        
        else: 
            print("Opção inválida!")
    


import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")