from Persona import *
import numpy as np
import random as rn

lista_personas = np.array([])
ciclo = True

def agregarPersona(lista_personas):
    p = Persona()
    c = False
    while c == False:
        c = p.setNIF(input("ingrese NIF. Ej. 99999999-AAA:"))
    c = False
    while c == False:
        c = p.setNombre(input("Ingrese Nombre:"))
    c = False
    while c == False:
        try:
            c = p.setEdad(int(input("Ingrese edad:")))
        except BaseException as error:
            print(f"Error:{error}")
    return np.append(lista_personas, p)


def buscarPersona(lista_personas):
    nif = input("Ingrese NIF Ej.99999999-AAA:")
    flag=False
    for persona in lista_personas:
        if nif == persona.NIF:
            flag = True
            print("Datos del Ciudadano")
            print(f"NIF   :{persona.NIF}")
            print(f"Nombre:{persona.Nombre}")
            print(f"Edad  :{persona.Edad}")
            if persona.Edad >=15:
                print("Es Ciudadano de la Union Europea")
            else:
                print("No es Ciudadano de la Union Europea")
            break
    if flag == False:
        print("No existe la persona")


def imprimirCertificado(lista_personas):
    nif = input("Ingrese NIF Ej.99999999-AAA:")
    flag = False
    for persona in lista_personas:
        if nif == persona.NIF:
            aleatorio = rn.randint(1,3)
            match aleatorio:
                case 1:
                    print("Certificado Nacimiento")
                case 2:
                    print("Certificado Conyugal")
                case 3:
                    print("Certificado Pertenencia UE")
            print(f"NIF   :{persona.NIF}")
            print(f"Nombre:{persona.Nombre}")
            print(f"Edad  :{persona.Edad}")
            flag=True
            break
    if flag == False:
        print("no existe persona")


def salir():
    return  False


while ciclo:
    print("Menu NIF España")
    print("1) Registrar Persona")
    print("2) Buscar Persona")
    print("3) Certificados")
    print("4) Salir")
    try:
        op = int(input("Seleccione (1-4):"))
        match op:
            case 1:
                print("Registrar Persona")
                lista_personas = agregarPersona(lista_personas)
            case 2:
                print("Buscar Persona")
                buscarPersona(lista_personas)
            case 3:
                print("Certificados")
                imprimirCertificado(lista_personas)
            case 4:
                print("Salir")
                ciclo = salir()
            case _:
                print("numero ingresado incorrecto")
    except BaseException as error:
        print(f"Error:{error}")
