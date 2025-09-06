from menus import gerenciar_filmes, gerenciar_generos
from database import criar_tabelas


def menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Gerenciar Gêneros")
    print("2. Gerenciar Filmes")
    print("0. Sair")
    return input("Escolha uma opção: ")


if __name__ == '__main__':
    criar_tabelas()
    while True:
        opcao_principal = menu_principal()
        if opcao_principal == '1':
            gerenciar_generos()
        elif opcao_principal == '2':
            gerenciar_filmes()
        elif opcao_principal == '0':
            print("Saindo da aplicação. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
