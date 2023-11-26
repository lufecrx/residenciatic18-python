import os
import manager

def run():
    # Define o caminho do diretório e o caminho do arquivo
    dir_path = "data/"
    filePath = os.path.join(dir_path, "products.txt")
    # Verifica se o diretório não existe e criar
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # Verifica se o arquivo não existe e criar
    if not os.path.exists(filePath):
        open(filePath, "w").close()
    # Carregar os dados
    manager.loadFromFile(filePath)
    
    # Execução da aplicação
    displayMenu()
    choice = -1
    while choice != "0":
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
        displayMenu()
    manager.saveToFile(filePath)
    
def displayMenu():
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
    