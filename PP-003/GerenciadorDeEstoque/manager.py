product = {
    "code": "",
    "name": "",
    "price": 0.00
}
products = []

# Criar um novo produto
def create_product():
    try:
        code = input("Código: ")
        validate_code(code) # Validar o código inserido
        for product in products:
            if (product["code"] == code):
                raise ValueError("Erro: Este código já foi atribuido a um produto.")
        name = input("Nome: ")
        validate_name(name) # Validar o nome inserido
        price = float(input("Preço: "))
        validate_price(price) # Validar o preço inserido
             
        product = {
            "code": code,
            "name": name,
            "price": price
        }
        products.append(product)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

# Remover um produto da lista, se existir
def delete_product():
    try:
        code = input("Código: ")
        validate_code(code)
        for product in products:
            if (product["code"] == code):
                products.remove(product)
                print("Produto excluído com sucesso!")
                return
        raise ValueError("Erro: Este código não foi atribuido a nenhum produto.")
    except ValueError as e:
        print(e)

# Exibir todos os pedidos cadastrados, se existirem
def list_products():
    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return
    for product in products:
        print(f"[{product['code']}] - {product['name']}: R${product['price'].__format__('.2f')}")

# Procurar um produto pelo código e retornar suas informações de nome e preço
def search_product():
    code = input("Código: ")
    validate_code(code)
    for product in products:
        if (product["code"] == code):
            print(f"{product['name']}: R${product['price'].__format__('.2f')}")
            return

# Validar códigos inseridos pelo usuário
def validate_code(code):
    if " " in code:
        raise ValueError("Erro: O código não deve conter espaços.")
    if not code.isnumeric():
        raise ValueError("Erro: O código deve conter apenas números.")
    if (len(code) != 13):
        raise ValueError("Erro: O código deve ter treze números.")

# Validar nomes inseridos pelo usuário
def validate_name(name):
    for product in products:
        if name in product["name"]:
            raise ValueError("Erro: Este nome já foi atribuido a um produto.")
    if name == "" or name.isspace():
        raise ValueError("Erro: O nome não pode ser vazio.")

# Validar preços inseridos pelo usuário
def validate_price(price):
    if (price <= 0.00):
        raise ValueError("Erro: O preço deve ser maior que zero.")

# Salvar os produtos da lista para o arquivo passado como parametro
def save_to_file(filePath):
    try:
        with open(filePath, "w") as file:
            for product in products:
                file.write(f"{product['code']}|{product['name']}|{product['price']}\n")
    except Exception as e:
        print(f"Erro ao salvar os dados: {str(e)}")
    
# Carregar os produtos do arquivo passado como parametro para a lista
def load_from_file(filePath):
    try: 
        with open(filePath, "r") as file:
            for line in file:
                code, name, price = line.strip().split("|")
                product = {
                    "code": code,
                    "name": name,
                    "price": float(price)
                }
                products.append(product)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado")
    except Exception as e:
        print(f"Erro ao carregar os dados: {str(e)}")
    