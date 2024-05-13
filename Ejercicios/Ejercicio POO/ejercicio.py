class persona:
    def __init__(self,nombre,edad,dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
        self.m=[]
        
               
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,n):
        self.nombre=n

    def getEdad(self):
        return  self.edad
    
    def setEdad(e):
        if e>0:
            edad=e

    def getDNI(self):
        return self.dni
    
    def setDNI(dn):
        dni=dn

    def mostrar_datos(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("DNI: ",self.dni)
        if self.mayorEdad:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

    def mostar_datos_1(self):
        print("Nombre: ",self.getNombre())
        print("Edad: ",self.getEdad)
        print("DNI: ",self.getDNI)
        print("Es mayor de edad: ",self.mayorEdad)

    def mayorEdad(self):
        if (self.edad>=18):
            return True
        else:
            return False
    
    def init_m(self):
        list=[]
        for i in range(4):
            list.append(0)
        self.m=list


p = persona ("Juan",25,"3456789")
p.mostrar_datos()
"""
print("segunda ")
p1=("Juan",25,"3456789")
p1.setNombre("Maria")
p1.setEdad("25")
p1.setDNI("30696288")
p1.mostar_datos_1
"""


    
    
"""
Hacer metodos:
contructr vacio
los set y get para todos y validar datos
mostradatos de la persno
devolver logico si es mayor de edad
"""