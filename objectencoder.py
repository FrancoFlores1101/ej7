import json
from ClaseDocente import docente
from ClaseInvestigador import investigador
from ClasePersonalDeApoyo import PersonalApoyo
from ClaseDocenteInvestigador import docenteinvestigador
from coleccion import ColeccionPersonal


class ObjectEncoder:
    def decodificar(self, d):
        retorno=None
        if '__class__' not in d:
            retorno=d
        else:
            class_name=d["__class__"]
            class_=eval(class_name)
            if class_name=="ColeccionPersonal":
                personas=d["personas"]
                coleccion=class_()
                for i in range(len(personas)):
                    dpersona=personas[i]
                    class_name=dpersona["__class__"]
                    class_=eval(class_name)
                    atributos=dpersona["__atributos__"]
                    unaPersona=class_(**atributos)
                    coleccion.agregarPersonal(unaPersona)
                retorno = coleccion
        return  retorno




    def leerJSON(self):
        archivo=open('personal.json',encoding='UTF-8')
        diccionario=json.load(archivo)
        archivo.close
        return diccionario
    def guardarJSON(self,diccionario):
        archivo=open('personal.json',"w",encoding='UTF-8')
        json.dump(diccionario,archivo,indent=4)
        archivo.close()

