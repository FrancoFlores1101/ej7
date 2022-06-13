from clasepersonal import personal

class investigador(personal):
    __AreaDeInvestigacion=None
    __TipoDeInvestigacion=None
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoInvestigacion,carrera='',cargo='',catedra=''):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoInvestigacion,carrera,cargo,catedra)
        self.__AreaDeInvestigacion=areaInvestigacion
        self.__TipoDeInvestigacion=tipoInvestigacion
    def mostrar(self):
        super().mostrar()
        print('-------INVESTIGADOR--------')
        cadena='AREA: {} \n TIPO: {}'.format(self.__AreaDeInvestigacion,self.__TipoDeInvestigacion)
        print(cadena)
    def getArea(self):
        return self.__AreaDeInvestigacion
