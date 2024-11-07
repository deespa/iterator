from abc import ABC, abstractmethod
from typing import List, Optional, Callable
from libro import Libro

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Optional[Libro]:
        pass

    @abstractmethod
    def current(self) -> Optional[Libro]:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

class BibliotecaIterator(Iterator):
    def __init__(self, libros: List[Libro], filtro: Callable[[Libro], bool] = lambda x: True):
        self._libros = [libro for libro in libros if filtro(libro)]
        self._posicion = 0

    def has_next(self) -> bool:
        return self._posicion < len(self._libros)

    def next(self) -> Optional[Libro]:
        try:
            libro = self._libros[self._posicion]
            self._posicion += 1
            return libro
        except IndexError:
            return None

    def current(self) -> Optional[Libro]:
        try:
            return self._libros[self._posicion]
        except IndexError:
            return None

    def reset(self) -> None:
        self._posicion = 0

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

    @abstractmethod
    def create_filtered_iterator(self, filtro: Callable[[Libro], bool]) -> Iterator:
        pass

class Biblioteca(Aggregate):
    def __init__(self):
        self._libros: List[Libro] = []

    def agregar_libro(self, libro: Libro) -> None:
        if not isinstance(libro, Libro):
            raise ValueError("Solo se pueden agregar instancias de la clase Libro")
        self._libros.append(libro)

    def create_iterator(self) -> Iterator:
        return BibliotecaIterator(self._libros)

    def create_filtered_iterator(self, filtro: Callable[[Libro], bool]) -> Iterator:
        return BibliotecaIterator(self._libros, filtro)

    def iterar(self) -> Iterator:        
        return self.create_iterator()

    def iterar_por_genero(self, genero: str) -> Iterator:       
        return self.create_filtered_iterator(lambda libro: libro.genero == genero)