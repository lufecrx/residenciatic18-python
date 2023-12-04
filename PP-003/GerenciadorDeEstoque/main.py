import os
import manager

def run():
    # Define o caminho do diretório e o caminho do arquivo
    dir_path = "data/"
    file_path = os.path.join(dir_path, "products.txt")
    # Verifica se o diretório não existe e criar
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # Verifica se o arquivo não existe e criar
    if not os.path.exists(file_path):
        open(file_path, "w").close()
    # Carregar os dados
    manager.load_from_file(file_path)
    
    # Execução da aplicação
    choice = -1
    while choice != "0":
        display_menu()
        print()
        choice = input("Escolha uma opção: ")   
        print()
        if choice == "1":
            print("Inserir um novo produto")
            manager.create_product()
        elif choice == "2":
            print("Excluir um produto cadastrado")
            manager.delete_product()
        elif choice == "3":
            print("Listar todos os produtos")
            manager.list_products()
        elif choice == "4":
            print("Consultar protudo pelo código")
            manager.search_product()
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
    manager.save_to_file(file_path)
    
def display_menu():
    print()
    print("=======SUPERMERCADO======")
    print("1. Inserir um novo produto")
    print("2. Excluir um produto cadastrado")
    print("3. Listar todos os produtos")
    print("4. Consultar protudo pelo código")
    print("0. Sair e salvar os dados")
    print("=========================")

def main():
    run()
    
if __name__ == "__main__":
    main()
    