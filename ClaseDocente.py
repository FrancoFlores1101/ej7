from clasepersonal import personal

class docente(personal):
    __carrera=None
    __cargo=None
    __catedra=None
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion='',tipoInvestigacion='',carrera='',cargo='',catedra=''):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoInvestigacion,carrera,cargo,catedra)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
    def mostrar(self):
        super().mostrar()
        print('--------DOCENTE--------')
        cadena='CARRERA: {} \n CARGO: {} \n CATEDRA: {}'.format(self.__carrera,self.__cargo,self.__catedra)
        print(cadena)
    def getPorcentaje(self):
        retorno=None
        if self.__cargo.lower() == 'simple':
            retorno=0.10
        if self.__cargo.lower() == 'semiexclusivo':
            retorno=0.20
        if self.__cargo.lower() == 'exclusivo':
            retorno=0.30
        return retorno
