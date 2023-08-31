from abc import ABC, abstractclassmethod

class IAnimal(ABC):
    def falar(self):
        """defina a classe filha"""

    def andar(self):
        """defina a classe filha"""

class Cachorro(IAnimal):
    def falar(self):
        print("AUAUAU")

    def andar(self):
        print("ANDO COM 4 PATAS")
        