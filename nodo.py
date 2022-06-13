from clasepersonal import personal
class Nodo:
    __personal=None
    __siguiente=None
    def __init__(self,personal):
        self.__personal=personal
        self.__siguiente=None
    def setSiguiente(self,nodo):
        self.__siguiente=nodo
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__personal
