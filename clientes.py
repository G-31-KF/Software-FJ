from entidades import Entidad
from excepciones import ClienteError


class Cliente(Entidad):

    def __init__(self, nombre, documento):

        self.__nombre = nombre
        self.__documento = documento

        self.validar()

    def validar(self):

        if len(self.__nombre) < 3:
            raise ClienteError("Nombre demasiado corto")

        if not self.__documento.isdigit():
            raise ClienteError("Documento inválido")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    def mostrar(self):

        print(f"Cliente: {self.__nombre} Documento:{self.__documento}")