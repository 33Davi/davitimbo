#Considere que voce esta implementando jogos de cartas em qeu tanto um baralho convencional
#quanto um baralho UNO devem ser suportados
#Crie uma classe CardSet que armazena uma lista de cartas
#A classe CardSet deve suportar tanto as cartas de UNO quanto as cartas convencionais
#Considere que cada carta em um valor, que é um númeor ou uma leta ( 2-10 , A, K,Q,K) e um naipe (O E P C)
#Considere que cada carta de UNO tem um valor (0 - 9), ou que são cartas especiais(+2,+4, qualquer cor, inverter ,bloquear)
#A classe CardSet deve ser capz de adicionar e imprimir qualquer conjunto de cartas válido ~
#Cada carta deve ser capaz de imprimir a si mesma
from abc import abstractmethod

class CardSet():
    def __init__(self, CardType):
        self.cartas = []
    
    def add(self , cartas):
        if len(self.cartas) == 0 and isinstance(cartas, (ConvCard, UNOCard)):
            self.__card.apppend(cartas)
        elif len(self.cartas) > 0:
            if isinstance(self.cartas[0], (UNOCard)) and isinstance(cartas, (UNOCard)):
                self.__card.apppend(cartas)
            elif isinstance(self.cartas[0], (ConvCard)) and isinstance(cartas, (ConvCard)):
                self.__card.apppend(cartas)
            else:
                raise ValueError("cartas de tipos diferentes")
    def __str__(self):
        res = ' '
        for c in self.cartas:



class ConvCard(): #definir oque é uma carta convencional validar a "cor"
    def __init__(self,valor,cor):
        self.value = valor
        self.color = cor

    @property
    def zuza(self):
        return self.cartas

    @zuza.setter
    def zuza(self, value):
        if
    
    def __str__(self):
        return f'{self.value} / {self.color}'



class NumberCard(): #definir os paramentros para a mesma ser um numero
    def __init__(self,valor,cor):
        self.value = valor
        self.color = cor



class LetterCard(): #definir os paramentros para a mesma ser uma letra
    def __init__(self,valor,cor):
        self.value = valor
        self.color = cor




class UNOCard(): #definir oque é uma carta de  UNO abs 
    def __init__(self,valor,cor):
        self.value = valor
    @abstractmethod
    def __str__(self):
        pass



class UNONumberCard(): #definir os paramentros para a mesma ser um numero / validar value
    def __init__(self,valor,cor):
        self.value = valor
        self.color = cor
    def __str__(self):
        return f'{self.value} / {self.color}'

class UNOSpecialCard(): #definir os paramentros para a mesma ser especial / validar value
    def __init__(self,valor,cor):
        self.value = valor
        self.color = cor
    def __str__(self):
        return f'{self.value} / {self.color}'


'''
    @property
    def zuza(self):
        return self.cartas

    @zuza.setter
    def zuza(self, value):
        if not value in []

    @property
    def zuza2(self):
        return self.cardtipe

    @zuza.setter
    def zuza2(self, value):
        if not value in []
'''