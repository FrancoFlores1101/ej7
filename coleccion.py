from nodo import Nodo

class ColeccionPersonal:
    __comienzo = None
    __actual = None
    __tope = 0
    __indice=0
    def __init__(self) :
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice=0
    def insertar(self,n,personal):
        if self.__comienzo != None:
            nodo=Nodo(personal)
            if n==0:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo=nodo
                self.__actual=self.__comienzo
            elif n <= self.__tope:
                aux=self.__comienzo
                for i in range(n-1):
                    aux=aux.getSiguiente()
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
            else:
                print('indice fuera de rango')


    def agregarPersonal(self,personal):
        nodo=Nodo(personal)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice== self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def mostrarPorPosicion(self,n):
        if n==0:
            unPersonal=self.__comienzo.getDato()
        elif n <= self.__tope:
            aux=self.__comienzo
            for i in range(n):
                aux=aux.getSiguiente()
            unPersonal=aux.getDato()
        else:
            print('indice fuera de rango')
            unPersonal=None
        return unPersonal
