class Persona:
    NIF=''
    Nombre=''
    Edad=0

    def __init__(self):
        self.NIF='99999999-AAA'
        self.Nombre='S/N'
        self.Edad=0

    def setNIF(self,NIF):
        if len(NIF) == 12:
            if NIF[0:8].isdigit() and NIF[9:12].isalpha() and NIF[8:9] == '-':
                self.NIF = NIF
                return True
            else:
                print("no tiene el formato correcto Ej. 99999999-AAA")
                return False
        else:
            print("largo incorrecto")
            return False

    def setNombre(self,Nombre):
        if len(Nombre) >= 8:
            self.Nombre = Nombre
            return True
        else:
            print("ingreso mal el nombre, minimo 8 caracteres")
            return False

    def setEdad(self,Edad):
        if Edad >=0:
            self.Edad = Edad
            return True
        else:
            print("edad debe ser mayor a 0")
            return False
