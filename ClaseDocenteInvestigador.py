from ClaseDocente import docente
from ClaseInvestigador import investigador

class docenteinvestigador(investigador,docente):
     __categoria=None
     __importeExtra=None
     def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoInvestigacion,carrera,cargo,catedra,categoriaIncentivos,importeExtra):
          super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoInvestigacion,carrera,cargo,catedra)
          self.__categoria=categoriaIncentivos
          self.__importeExtra = importeExtra
     def mostrar(self):
          super().mostrar()
          print('vvvv por desempeñar ambos cargos vvvv')
          cadena='CATEGORIA: {} \n IMPORTE:{}'.format(self.__categoria,self.__importeExtra)
          print(cadena)
     def getArea(self):
          area=super().getArea()
          return area
     def getImprorteExtra(self):
          return float(self.__importeExtra)
