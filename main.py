from objectencoder import ObjectEncoder
from ClasePersonalDeApoyo import PersonalApoyo
from ClaseInvestigador import investigador
from ClaseDocente import docente
from ClaseDocenteInvestigador import docenteinvestigador

if __name__ == '__main__':
    jsonF=ObjectEncoder()
    dicc=jsonF.leerJSON()
    coleccion=jsonF.decodificar(dicc)
#PUNTO 5
    area=input('ingrese area a contar y mostrar')
    contador=0
    for persona in coleccion:
        if isinstance(persona,docenteinvestigador) or isinstance(persona,investigador):
            if persona.getArea().lower() == area.lower():
                persona.mostrar()
                contador+=1
                print('+++++++++++++++++++++++++++++++++++')
    print('CANTIDAD TOTAL= {}'.format(contador))
#PUNTO 5
#PUNTO 6
    for persona in coleccion:
        if isinstance(persona,docenteinvestigador):
            persona.mostrar()
            print('SUELDO : {}'.format(persona.getSueldo()+persona.getSueldo()*(persona.getAntiguedad()/100)+persona.getSueldo()*persona.getPorcentaje()+persona.getImprorteExtra()))
        if isinstance(persona,docente) and not isinstance(persona,docenteinvestigador):
            persona.mostrar()
            print('SUELDO : {}'.format(persona.getSueldo()+persona.getSueldo()*(persona.getAntiguedad()/100)+persona.getSueldo()*persona.getPorcentaje()))
        if isinstance(persona,investigador) and not isinstance(persona,docenteinvestigador):
            persona.mostrar()
            print('SUELDO : {}'.format(persona.getSueldo()+persona.getSueldo()*(persona.getAntiguedad()/100)))
        if isinstance(persona,PersonalApoyo):
            persona.mostrar()
            print('SUELDO : {}'.format(persona.getSueldo()+persona.getSueldo()*(persona.getAntiguedad()/100)+persona.getSueldo()*persona.getPorcentaje()))
