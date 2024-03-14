from abc import ABC, abstractmethod

from src.librerialectorarchivo.implclases.lector import Lector, LectorArchivo


class Filtro(Lector, ABC):
    def __init__(self, lector_base: Lector):
        self.lector_base: Lector = lector_base

    def leer(self):
        c = self.lector_base.leer()
        return self.filtrar(c)

    def cerrar(self):
        self.lector_base.cerrar()

    @abstractmethod
    def filtrar(self, c):
        pass


class FiltroMayAMin(Filtro):
    def __init__(self, lector):
        super().__init__(lector)

    def filtrar(self, c):
        if c.isupper():
            c = c.lower()
        return c


class FiltroEspacioAGuion(Filtro):
    def __init__(self, lector):
        super().__init__(lector)

    def filtrar(self, c):
        if c == ' ':
            c = '_'
        return c


class FiltroParentesisACorchetes(Filtro):
    def __init__(self, lector):
        super().__init__(lector)

    def filtrar(self, c):
        if c == '(':
            c = '['
        if c == ')':
            c = ']'
        return c


class CreadorLector:
    def __init__(self, file_path):
        self.lector = LectorArchivo(file_path)

    def crear_lector(self) -> Lector:
        return self.lector

    def con_filtro_may_a_min(self):
        self.lector = FiltroMayAMin(self.lector)
        return self

    def con_filtro_espacio_a_guion(self):
        self.lector = FiltroEspacioAGuion(self.lector)
        return self

    def con_filtro_parentesis_a_corchetes(self):
        self.lector = FiltroParentesisACorchetes(self.lector)
        return self

    def con_filtro_personalizado(self, filtro):
        self.lector = filtro(self.lector)
        return self