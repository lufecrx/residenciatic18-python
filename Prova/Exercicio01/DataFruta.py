
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        pass

    @abstractmethod
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        pass
    
    @abstractmethod
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        pass

    @abstractmethod
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        n = int(input("Quantos elementos deseja adicionar à lista? "))
        for _ in range(n):
            elemento = input("Digite um elemento: ")
            self.__lista.append(elemento)

    def mostraMediana(self):
        # Ordenar a lista e mostrar a string que está na metade da lista
        sorted_list = sorted(self.__lista)
        middle_index = len(sorted_list) // 2
        
        if len(sorted_list) % 2 == 0:
            # Se a lista tiver um número par de elementos, retorna o primeiro elemento do meio
            median = sorted_list[middle_index - 1]
        else:
            median = sorted_list[middle_index]
        return median        
        
    def mostraMenor(self):
        # Mostrar o menor elemento da lista
        min_value = min(self.__lista)
        return min_value
        
    def mostraMaior(self):
        # Mostrar o maior elemento da lista
        max_value = max(self.__lista)
        return max_value

    def __str__(self):
        # Retornar a lista como uma string
        return str(self.__lista)
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        n = int(input("Quantos elementos deseja adicionar à lista? "))
        # Adicionar elementos do tipo Data à lista
        try:
            for _ in range(n):
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))
                data = Data(dia, mes, ano)
                self.__lista.append(data)    
        except ValueError as e:
            print(str(e))        
    
    def mostraMediana(self):
        # Ordenar a lista e mostrar a Data que está na metade da lista
        sorted_list = sorted(self.__lista)
        middle_index = len(sorted_list) // 2
        
        if len(sorted_list) % 2 == 0:
            # Se a lista tiver um número par de elementos, retorna o primeiro elemento do meio
            median = sorted_list[middle_index - 1]
        else:
            median = sorted_list[middle_index]
        return median
     
    def mostraMenor(self):
        # Mostrar a menor Data da lista
        min_value = min(self.__lista, key=lambda data: data)
        return  str(min_value)
    
    def mostraMaior(self):
        # Mostrar a maior Data da lista
        max_data = max(self.__lista, key=lambda data: data)
        return str(max_data)
    
    def __str__(self):
        # Retornar a lista como uma string
        return str(self.__lista)

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        n = int(input("Quantos elementos deseja adicionar à lista? "))
        for _ in range(n):
            elemento = float(input("Digite um elemento: "))
            self.__lista.append(elemento)

    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        if len(sorted_list) % 2 == 0:
            # Se for par, a mediana é calculada como a média dos dois elementos do meio.
            median = (sorted_list[len(sorted_list) // 2] + sorted_list[len(sorted_list) // 2 - 1]) / 2
        else:
            # Se for ímpar, a mediana é o valor do elemento do meio.
            median = sorted_list[len(sorted_list) // 2]
        return median    

    def mostraMenor(self):
        min_value = min(self.__lista)
        return min_value
        
    def mostraMaior(self): 
        max_value = max(self.__lista)
        return max_value

    def __str__(self):
        return str(self.__lista)
    
class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        n = int(input("Quantos elementos deseja adicionar à lista? "))
        for _ in range(n):
            elemento = int(input("Digite um elemento: "))
            self.__lista.append(elemento)        
    
    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        if len(sorted_list) % 2 == 0:
            # Se for par, a mediana é calculada como a média dos dois elementos do meio
            median = (sorted_list[len(sorted_list) // 2] + sorted_list[len(sorted_list) // 2 - 1]) / 2
        else:
            # Se for ímpar, a mediana é o valor do elemento do meio
            median = sorted_list[len(sorted_list) // 2]
        return median
            
    def mostraMenor(self):
        min_value = min(self.__lista)
        return min_value
            
    def mostraMaior(self):
        max_value = max(self.__lista)
        return max_value
    
    def __str__(self):
        return str(self.__lista)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        print("Entrada de Dados")
        lista.entradaDeDados()
        print("Resultados")
        print("Mediana: ", lista.mostraMediana())
        print("Menor valor: ", lista.mostraMenor())        
        print("Maior valor: ", lista.mostraMaior())
        print("_______________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()