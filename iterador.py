from abc import ABC, abstractmethod
from typing import List, Optional, Callable
from libro import Libro

class Iterator(ABC):    

    @abstractmethod
    def has_next(self) -> bool:
        #Retorna True si hay más elementos en la colección, False en caso contrario.
        pass

    @abstractmethod
    def next(self) -> Optional[Libro]:
        #Retorna el siguiente libro en la colección y avanza el cursor.
        pass

    @abstractmethod
    def current(self) -> Optional[Libro]:
        #Retorna el libro actual en la posición del cursor sin avanzar.
        pass

    @abstractmethod
    def reset(self) -> None:
        #Reinicia el cursor al inicio de la colección.
        pass

class BibliotecaIterator(Iterator):
    #Implementación concreta del Iterator para la clase Biblioteca.

    def __init__(self, libros: List[Libro], filtro: Callable[[Libro], bool] = lambda x: True):
        self._libros = [libro for libro in libros if filtro(libro)]
        self._posicion = 0

    def has_next(self) -> bool:
        #Retorna True si hay más libros que recorrer; False en caso contrario.
        return self._posicion < len(self._libros)

    def next(self) -> Optional[Libro]:
        #Retorna el siguiente libro y avanza el cursor. Si no hay más, retorna None.
        if self.has_next():
            libro = self._libros[self._posicion]
            self._posicion += 1
            return libro
        return None

    def current(self) -> Optional[Libro]:
        #Retorna el libro en la posición actual del cursor sin avanzar.
        if 0 <= self._posicion < len(self._libros):
            return self._libros[self._posicion]
        return None

    def reset(self) -> None:        
        self._posicion = 0 #Reinicia el cursor a la posición inicial.
