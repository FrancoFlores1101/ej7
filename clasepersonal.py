from abc import ABC
import abc
class personal(ABC):
    __cuil=None
    __apellido=None
    __nombre=None
    __sueldo=None
    __antiguedad=None
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion='',tipoInvestigacion='',carrera='',cargo='',catedra=''):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldo=sueldoBasico
        self.__antiguedad=antiguedad
    def mostrar(self):
        cadena='CUIL: {} NOMBRE: {} APELLIDO: {} SUELDO: {}   ANTIGUEDAD: {} '.format(self.__cuil,self.__nombre,self.__apellido,self.__sueldo,self.__antiguedad)
        print(cadena)
    def getSueldo(self):
        return float(self.__sueldo)
    def getAntiguedad(self):
        return float(self.__antiguedad)
