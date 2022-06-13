from clasepersonal import personal

class PersonalApoyo(personal):
    __categoria=None
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad)
        self.__categoria=categoria
    def mostrar(self):
        super().mostrar()
        print('-------APOYO---------')
        cadena='categoria: {}'.format(self.__categoria)
        print(cadena)
    def getPorcentaje(self):
        retorno=None
        if self.__categoria >= 1 and self.__categoria <= 10:
            retorno=0.10
        if self.__categoria >= 11 and self.__categoria <=20:
            retorno=0.20
        if self.__categoria == 21 or self.__categoria == 22:
            retorno=0.30
        return retorno
