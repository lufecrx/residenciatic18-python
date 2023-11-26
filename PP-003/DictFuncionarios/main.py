import os

funcionario = {
    'nome': "",
    'sobrenome': "",
    'ano_nascimento': "",
    'rg': "",
    'ano_admissao': "",
    'salario': float
}

funcionarios = []

def adicionar_funcionario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    ano_nascimento = input("Ano de nascimento: ")
    rg = input("RG: ")
    ano_admissao = input("Ano de admissão: ")
    salario = float(input("Salário: "))
    funcionario = {
        'nome': nome,
        'sobrenome': sobrenome,
        'ano_nascimento': ano_nascimento,
        'rg': rg,
        'ano_admissao': ano_admissao,
        'salario': float(salario)
    }
    funcionarios.append(funcionario)
    
def excluir_funcionario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    for funcionario in funcionarios:
        if funcionario['nome'] == nome and funcionario['sobrenome'] == sobrenome:
            funcionarios.remove(funcionario)

def exibir_funcionarios():
    for funcionario in funcionarios:
        print(f"Nome: {funcionario['nome']}")
        print(f"Sobrenome: {funcionario['sobrenome']}")
        print(f"Ano de nascimento: {funcionario['ano_nascimento']}")
        print(f"RG: {funcionario['rg']}")
        print(f"Ano de admissão: {funcionario['ano_admissao']}")
        print(f"Salário: R${funcionario['salario'].__format__('.2f')}")
        print()

def alterar_funcionario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    for funcionario in funcionarios:
        if funcionario['nome'] == nome and funcionario['sobrenome'] == sobrenome:
            novo_nome = input("Novo nome: ")
            novo_sobrenome = input("Novo sobrenome: ")
            novo_ano_nascimento = input("Novo ano de nascimento: ")
            novo_rg = input("Novo RG: ")
            novo_ano_admissao = input("Novo ano de admissão: ")
            novo_salario = float(input("Novo salaário: "))
            funcionario['nome'] = novo_nome
            funcionario['sobrenome'] = novo_sobrenome
            funcionario['ano_nascimento'] = novo_ano_nascimento
            funcionario['rg'] = novo_rg
            funcionario['ano_admissao'] = novo_ano_admissao
            funcionario['salario'] = novo_salario

def reajuste_salarial_porcentagem():
    porcentagem = float(input("Porcentagem: "))
    for funcionario in funcionarios:
            novo_salario = funcionario['salario'] * (1 + porcentagem / 100)
            funcionario['salario'] = novo_salario

def display_menu():
    print()
    print("1. Adicionar funcionário")
    print("2. Excluir funcionário")
    print("3. Exibir funcionários")
    print("4. Alterar funcionário")
    print("5. Reajuste salarial pela porcentagem")
    print("6. Sair e salvar os dados")
    print()

def save_funcionarios(file_path):
    with open(file_path, "w") as f:
        for funcionario in funcionarios:
            f.write(f"{funcionario['nome']};{funcionario['sobrenome']};{funcionario['ano_nascimento']};{funcionario['rg']};{funcionario['ano_admissao']};{funcionario['salario']}\n")

def load_funcionarios(file_path):
    with open(file_path, "r") as f:
        for line in f:
            nome, sobrenome, ano_nascimento, rg, ano_admissao, salario = line.strip().split(';')
            funcionario = {
                'nome': nome,
                'sobrenome': sobrenome,
                'ano_nascimento': ano_nascimento,
                'rg': rg,
                'ano_admissao': ano_admissao,
                'salario': float(salario)
            }
            funcionarios.append(funcionario)

def main():
    # Define o caminho do diretório e o caminho do arquivo
    dir_path = "data/"
    file_path = os.path.join(dir_path, "funcionarios.txt")
    # Verifica se o diretório não existe e criar
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # Verifica se o arquivo não existe e criar
    if not os.path.exists(file_path):
        open(file_path, "w").close()
    # Carregar os dados
    load_funcionarios(file_path)
    
    choice = -1
    while (choice != 0):
        display_menu()
        choice = int(input("Escolha uma opção: "))
        print()
        if choice == 1:
            adicionar_funcionario()
        elif choice == 2:
            excluir_funcionario()
        elif choice == 3:
            exibir_funcionarios()
        elif choice == 4:
            alterar_funcionario()
        elif choice == 5:
            reajuste_salarial_porcentagem()
        elif choice == 6:
            break    
    
    save_funcionarios(file_path)

if __name__ == '__main__':
    main()