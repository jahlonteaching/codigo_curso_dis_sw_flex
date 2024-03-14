from src.librerialectorarchivo.implclases.filtros import Filtro, CreadorLector
from src.librerialectorarchivo.implclases.lector import Lector


class FiltroInterrogacionAExclamacion(Filtro):
    def __init__(self, lector_base):
        super().__init__(lector_base)

    def filtrar(self, c):
        if c == '¿':
            c = '¡'
        if c == '?':
            c = '!'
        return c


if __name__ == '__main__':
    creador = CreadorLector("test.txt")
    lector: Lector = (creador.con_filtro_parentesis_a_corchetes()
                      .con_filtro_espacio_a_guion()
                      .con_filtro_personalizado(FiltroInterrogacionAExclamacion)
                      .crear_lector())

    with lector as lec:
        ch = lec.leer()
        while ch != '':
            print(ch, end='')
            ch = lec.leer()