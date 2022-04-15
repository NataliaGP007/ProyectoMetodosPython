"""
Desarrollar un algoritmo que pida el nombre del usuario, el día, mes y año actual y el día, mes y año de nacimiento del
usuario. En  base a esos datos el algoritmo indica el signo zodiacal, la edad en horas y el número de la suerte del
usuario.

Autor: Natalia Gutiérrez Pineda.
"""

# Clase publica
class Numerologia:

    __anioNacimiento = int(0)
    __mesNacimiento = int(0)
    __diaNacimiento = int(0)
    __anioActual = int(0)
    __mesActual = int(0)
    __diaActual = int(0)
    __edad = int(0)
    __edadHoras = int(0)
    __signoZodiacal = str(" ")
    __numeroSuerte = int(0)

    # Metodo Constructor
    def __init__(self, anioNacimiento, mesNacimiento, diaNacimiento, anioActual, mesActual, diaActual):
        self.__anioNacimiento = anioNacimiento
        self.__mesNacimiento = mesNacimiento
        self.__diaNacimiento = diaNacimiento
        self.__anioActual = anioActual
        self.__mesActual = mesActual
        self.__diaActual = diaActual
        self.calcularEdad()
        self.identificarSignoZodiacal()
        self.calcularNumeroSuerte()

    # Getters
    def get_edad(self):
        return self.__edad

    def get_signoZodiacal(self):
        return self.__signoZodiacal

    def get_numeroSuerte(self):
        return self.__numeroSuerte

    # Metodos de instancia
    def calcularEdad(self):
        # Este metodo calculará la edad en horas del usuario.
        self.__edad = self.__anioActual - self.__anioNacimiento
        if (self.__mesActual < self.__mesNacimiento) or (
                self.__mesActual == self.__mesNacimiento and self.__diaActual < self.__diaNacimiento):
            self.__edad = self.__edad - 1
        self.__edad = self.__edad * 8760

    def identificarSignoZodiacal(self):
        # Este metodo identificará el signo zodiacal del usuario.
        if (self.__mesNacimiento == 12 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 1 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Capricornio'
        if (self.__mesNacimiento == 1 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 2 and self.__diaNacimiento <= 19):
            self.__signoZodiacal = 'Acuario'
        if (self.__mesNacimiento == 2 and self.__diaNacimiento >= 20) or (self.__mesNacimiento == 3 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Piscis'
        if (self.__mesNacimiento == 3 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 4 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Aries'
        if (self.__mesNacimiento == 4 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 5 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Tauro'
        if (self.__mesNacimiento == 5 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 6 and self.__diaNacimiento <= 21):
            self.__signoZodiacal = 'Géminis'
        if (self.__mesNacimiento == 6 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 7 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Cáncer'
        if (self.__mesNacimiento == 7 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 8 and self.__diaNacimiento <= 23):
            self.__signoZodiacal = 'Leo'
        if (self.__mesNacimiento == 8 and self.__diaNacimiento >= 24) or (self.__mesNacimiento == 9 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Virgo'
        if (self.__mesNacimiento == 9 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 10 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Libra'
        if (self.__mesNacimiento == 10 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 11 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Escorpio'
        if (self.__mesNacimiento == 11 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 12 and self.__diaNacimiento <= 21):
            self.__signoZodiacal = 'Sagitario'

    def calcularNumeroSuerte (self):
        # Este metodo calculará el numero de la suerte del usuario.
        while self.__anioNacimiento > 0:
            self. __numeroSuerte = self. __numeroSuerte + self.__anioNacimiento % 10
            self.__anioNacimiento = self.__anioNacimiento // 10

        while self.__numeroSuerte > 9:
            self.__numeroSuerte = self.__numeroSuerte - 9

    def __del__(self):
        print("Instancia destruida")

from abc import ABC

class abc(ABC):

    # Metodos de clase
    @classmethod
    def calcularEdadMC(cls, anioNacimiento, mesNacimiento, diaNacimiento, anioActual, mesActual, diaActual):
        # Este metodo calculará la edad en horas del usuario.
        edad = anioActual - anioNacimiento
        if (mesActual < mesNacimiento) or (
            mesActual == mesNacimiento and diaActual < diaNacimiento):
            edad = edad - 1

        return edad * 8760

    @classmethod
    def identificarSignoZodiacalMC(cls, mesNacimiento, diaNacimiento):
        # Este metodo identificará el signo zodiacal del usuario.
        signoZodiacal = " "
        if (mesNacimiento == 12 and diaNacimiento >= 22) or (mesNacimiento == 1 and diaNacimiento <= 20):
            signoZodiacal = 'Capricornio'
        if (mesNacimiento == 1 and diaNacimiento >= 22) or (mesNacimiento == 2 and diaNacimiento <= 19):
            signoZodiacal = 'Acuario'
        if (mesNacimiento == 2 and diaNacimiento >= 20) or (mesNacimiento == 3 and diaNacimiento <= 20):
            signoZodiacal = 'Piscis'
        if (mesNacimiento == 3 and diaNacimiento >= 21) or (mesNacimiento == 4 and diaNacimiento <= 20):
            signoZodiacal = 'Aries'
        if (mesNacimiento == 4 and diaNacimiento >= 21) or (mesNacimiento == 5 and diaNacimiento <= 20):
            signoZodiacal = 'Tauro'
        if (mesNacimiento == 5 and diaNacimiento >= 21) or (mesNacimiento == 6 and diaNacimiento <= 21):
            signoZodiacal = 'Géminis'
        if (mesNacimiento == 6 and diaNacimiento >= 22) or (mesNacimiento == 7 and diaNacimiento <= 22):
            signoZodiacal = 'Cáncer'
        if (mesNacimiento == 7 and diaNacimiento >= 23) or (mesNacimiento == 8 and diaNacimiento <= 23):
            signoZodiacal = 'Leo'
        if (mesNacimiento == 8 and diaNacimiento >= 24) or (mesNacimiento == 9 and diaNacimiento <= 22):
            signoZodiacal = 'Virgo'
        if (mesNacimiento == 9 and diaNacimiento >= 23) or (mesNacimiento == 10 and diaNacimiento <= 22):
            signoZodiacal = 'Libra'
        if (mesNacimiento == 10 and diaNacimiento >= 23) or (mesNacimiento == 11 and diaNacimiento <= 22):
            signoZodiacal = 'Escorpio'
        if (mesNacimiento == 11 and diaNacimiento >= 23) or (mesNacimiento == 12 and diaNacimiento <= 21):
            signoZodiacal = 'Sagitario'

        return signoZodiacal

    @classmethod
    def calcularNumeroSuerteMC(cls, anioNacimiento):
        # Este metodo calculará el numero de la suerte del usuario.
        numeroSuerte = 0
        while anioNacimiento > 0:
            numeroSuerte = numeroSuerte + anioNacimiento % 10
            anioNacimiento = anioNacimiento // 10

        while numeroSuerte > 9:
            numeroSuerte = numeroSuerte - 9

        return numeroSuerte

class Sobrecarga:

    __anioNacimiento = int(0)
    __mesNacimiento = int(0)
    __diaNacimiento = int(0)
    __anioActual = int(0)
    __mesActual = int(0)
    __diaActual = int(0)
    __edad = int(0)
    __edadHoras = int(0)
    __signoZodiacal = str(" ")
    __numeroSuerte = int(0)

    # Metodos de instancia
    def calcularEdad(self, anioNacimiento, mesNacimiento, diaNacimiento, anioActual, mesActual, diaActual):
        # Este metodo calculará la edad en horas del usuario.
        self.__anioNacimiento = anioNacimiento
        self.__mesNacimiento = mesNacimiento
        self.__diaNacimiento = diaNacimiento
        self.__anioActual = anioActual
        self.__mesActual = mesActual
        self.__diaActual = diaActual
        self.__edad = self.__anioActual - self.__anioNacimiento
        if (self.__mesActual < self.__mesNacimiento) or (
                self.__mesActual == self.__mesNacimiento and self.__diaActual < diaNacimiento):
            self.__edad = self.__edad - 1

        return self.__edad * 8760

    def identificarSignoZodiacal(self):
        # Este metodo identificará el signo zodiacal del usuario.
        if (self.__mesNacimiento == 12 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 1 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Capricornio'
        if (self.__mesNacimiento == 1 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 2 and self.__diaNacimiento <= 19):
            self.__signoZodiacal = 'Acuario'
        if (self.__mesNacimiento == 2 and self.__diaNacimiento >= 20) or (self.__mesNacimiento == 3 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Piscis'
        if (self.__mesNacimiento == 3 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 4 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Aries'
        if (self.__mesNacimiento == 4 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 5 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Tauro'
        if (self.__mesNacimiento == 5 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 6 and self.__diaNacimiento <= 21):
            self.__signoZodiacal = 'Géminis'
        if (self.__mesNacimiento == 6 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 7 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Cáncer'
        if (self.__mesNacimiento == 7 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 8 and self.__diaNacimiento <= 23):
            self.__signoZodiacal = 'Leo'
        if (self.__mesNacimiento == 8 and self.__diaNacimiento >= 24) or (self.__mesNacimiento == 9 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Virgo'
        if (self.__mesNacimiento == 9 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 10 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Libra'
        if (self.__mesNacimiento == 10 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 11 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Escorpio'
        if (self.__mesNacimiento == 11 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 12 and self.__diaNacimiento <= 21):
            self.__signoZodiacal = 'Sagitario'

        return self.__signoZodiacal

    def calcularNumeroSuerte(self):
        # Este metodo calculará el numero de la suerte del usuario.
        while self.__anioNacimiento > 0:
            self.__numeroSuerte = self.__numeroSuerte + self.__anioNacimiento % 10
            self.__anioNacimiento = self.__anioNacimiento // 10

        while self.__numeroSuerte > 9:
            self.__numeroSuerte = self.__numeroSuerte - 9

        return self.__numeroSuerte

    # Metodo con sobrecarga
    def numerologia(self, anioNacimiento=None, mesNacimiento=None, diaNacimiento=None, anioActual=None, mesActual=None, diaActual=None):
        if anioNacimiento is not None and mesNacimiento is not None and diaNacimiento is not None and anioActual is None and mesActual is None and diaActual is None:
            self.__anioNacimiento = anioNacimiento
            self.__mesNacimiento = mesNacimiento
            self.__diaNacimiento = diaNacimiento
            print(self.identificarSignoZodiacal())
            print(self.calcularNumeroSuerte())
            self.__numeroSuerte = 0
        elif anioNacimiento is not None and mesNacimiento is not None and diaNacimiento is not None and anioActual is not None and mesActual is not None and diaActual is not None:
            self.__anioNacimiento = anioNacimiento
            self.__mesNacimiento = mesNacimiento
            self.__diaNacimiento = diaNacimiento
            self.__anioActual = anioActual
            self.__mesActual = mesActual
            self.__diaActual = diaActual
            print(self.identificarSignoZodiacal())
            print(self.calcularNumeroSuerte())
            print(self.calcularEdad(2003, 7, 27, 2022, 4, 10))

    def __del__(self):
        print("Instancia destruida")

# Clase main
class Main:

    if __name__ == "__main__":
        # Instancia
        metodos = Numerologia(2003, 7, 27, 2022, 4, 10)
        # Llamado de los getters
        print(metodos.get_edad())
        print(metodos.get_signoZodiacal())
        print(metodos.get_numeroSuerte())
        # Llamado del destructor
        del metodos
        # Llamado de metodos de clase
        print(abc.calcularEdadMC(2003, 7, 27, 2022, 4, 10))
        print(abc.identificarSignoZodiacalMC(7, 27))
        print(abc.calcularNumeroSuerteMC(2003))
        # Instancia
        metodos2 = Sobrecarga()
        # Llamado del metodo con sobrecarga
        metodos2.numerologia(2000, 7, 27)
        metodos2.numerologia(2000, 7, 27, 2022, 4, 10)
        # Llamado del destructor
        del metodos2
