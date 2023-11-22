import os

class Program:
    def run(self):
        # Define o caminho do diretório e o caminho do arquivo
        dir_path = "data/"
        filePath = os.path.join(dir_path, "tasks.txt")
        # Verifica se o diretório não existe e criar
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        # Verifica se o arquivo não existe e criar
        if not os.path.exists(filePath):
            open(filePath, "w").close()
        
        # Cria uma instância do Manager e carrega os dados do arquivo
        manager = Manager(filePath)
        manager.load()
        
        print("\nBEM VINDO AO GERENCIADOR DE TAREFAS")
        manager.listAllTasks()
    
        while True:
            print("\nO que deseja fazer?")
            print("1. Criar tarefa")
            print("2. Listar tarefas")
            print("3. Concluir tarefa")
            print("4. Remover tarefa")
            print("5. Editar tarefa")
            print("0. Sair e salvar os dados")
            option = input("Escolha uma opção: ")
            print()
            try:
                option = int(option)
                if option == 1:
                    manager.createTask()
                elif option == 2:
                    manager.listAllTasks()
                elif option == 3:
                    manager.markTask()
                elif option == 4:
                    manager.removeTask()
                elif option == 5:
                    manager.editTask()
                elif option == 0:
                    manager.save()
                    break
                else:
                    print("Opcão inválida")
            except ValueError:
                print("Por favor, insira um número válido")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {str(e)}")
    
class Manager:
    def __init__(self, filePath):
        # Inicializa a lista de tarefas e o caminho do arquivo
        self.tasks = []
        self.filePath = filePath
    
    def save(self):
        # Salva as tarefas no arquivo
        try:
            with open(self.filePath, "w") as file:
                for task in self.tasks:
                    file.write(f"{task.id}|{task.description}|{task.completed}" + "\n")
        except Exception as e:
            print(f"Erro ao salvar os dados: {str(e)}")
    
    def load(self):
        # Carrega as tarefas do arquivo para a lista
        try: 
            with open(self.filePath, "r") as file:
                for line in file:
                    id, description, completed  = line.strip().split("|")
                    task = Task(description)
                    task.id = int(id)
                    task.completed = True if completed == "True" else False
                    self.tasks.append(task)
        except FileNotFoundError:
            print("Arquivo de dados não encontrado")
        except Exception as e:
            print(f"Erro ao carregar os dados: {str(e)}")


    def createTask(self):
        # Cria uma nova tarefa e a adiciona à lista de tarefas
        description = input("Descrição: ").capitalize()
        try: 
            task = Task(description)
            self.tasks.append(task)        
            print("Tarefa criada!")
        except Exception as e:
            print(f"Erro ao criar a tarefa: {str(e)}")

    def addTask(self, task):
        # Adiciona uma tarefa à lista
        self.tasks.append(task)
    
    def removeTask(self):
        # Permite remover uma tarefa por descrição ou ID
        print("Deseja remover pela descrição ou pelo ID?")
        print("1. Descrição")
        print("2. ID")
        print("0. Voltar")
        option = input("Escolha uma opção: ")

        try:
            option = int(option)            
            if option == 1:
                descricao = input("Descrição: ").capitalize()
                for t in self.tasks:
                    if t.description == descricao:
                        self.tasks.remove(t)
                        print("Tarefa removida!")   
            elif option == 2:
                taskToRemove = self.getTaskById()
                if taskToRemove != None: self.tasks.remove(taskToRemove)
                print("Tarefa removida!")
            else:
                return
        except ValueError:
            print("Por favor, insira um número válido")
    
    def markTask(self):
        # Marca ou desmarca uma tarefa por ID
        print("Insira o ID da tarefa que você deseja marcar ou desmarcar.")
        taskToMark = self.getTaskById()
        if taskToMark is not None: taskToMark.toggleComplete(manager = self)
    
    def editTask(self):
        # Edita a descrição de uma tarefa por ID
        print("Insira o ID da tarefa que você deseja editar.")
        taskToEdit = self.getTaskById()
        if taskToEdit != None: description = input("Nova descrição: ").capitalize()
        print("Tem certeza que deseja alterar a descrição da tarefa? (S/n)")
        confirm = input("Responda com S ou N: ")
        if confirm.upper() == "S":
            taskToEdit.description = description
            print("Tarefa editada!")
        else:
            print("Tarefa não editada!")

    def listConcludedTasks(self):
        # Lista as tarefas concluídas
        print("\nTAREFAS CONCLUÍDAS")
        concludedTasksIsEmpty = True
        for t in self.tasks:
            if t.completed:
                print(t)
                concludedTasksIsEmpty = False
        if concludedTasksIsEmpty: print("Nenhuma tarefa concluída!")
    
    def listUnconcludedTasks(self):
        # Lista as tarefas não concluídas
        print("\nTAREFAS NÃO CONCLUÍDAS")
        unconcludedTasksIsEmpty = True
        for t in self.tasks:
            if not t.completed:
                print(t)
                unconcludedTasksIsEmpty = False
        if unconcludedTasksIsEmpty: print("Nenhuma tarefa pendente!")

    def listAllTasks(self):
        # Lista todas as tarefas (concluídas e não concluídas)
        self.listConcludedTasks()
        self.listUnconcludedTasks()

    def getTaskById(self):
        # Obtém uma tarefa da lista por ID
        id = int(input("ID: "))
        for t in self.tasks:
            if t.id == id:
                return t
        print("Tarefa não encontrada!")
        return None

class Task:
    nextId = 1

    def __init__(self, description):
        # Inicializa uma tarefa com descrição, ID, e estado inicial não concluído
        self.id = Task.nextId
        self.description = description
        self.completed = False
        Task.nextId += 1

    def toggleComplete(self, situation=None, manager=None):
        # Alterna o estado de conclusão da tarefa
        if situation is not None:
            self.completed = situation
        else:
            self.completed = not self.completed
                
        # Atualiza a ordem das tarefas na lista com base no estado de conclusão
        if manager:
            manager.tasks.remove(self)
            manager.tasks.insert(0 if self.completed else len(manager.tasks), self)

    def __str__(self):
        # Representação em string da tarefa
        return str(self.id) + ". " + self.description + " [" + ("X" if self.completed else " ") + "]"

# Cria uma instância do programa e executa
taskManagerProgram = Program()
taskManagerProgram.run()
    