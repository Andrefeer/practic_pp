from abc import ABC, abstractmethod
from enum import Enum

class StareMentala(Enum):
    FERICIT   = "Fericit"
    STRESAT   = "Stresat"
    DISPERAT  = "Disperat"
    RELAXAT   = "Relaxat"
    MOTIVAT   = "Motivat"

class Student:
    def __init__(self, nume: str):
        self._nume  = nume
        self._stare = StareMentala.FERICIT
        self._istoric: list[str] = []

    @property
    def nume(self) -> str:
        return self._nume

    @property
    def stare(self) -> StareMentala:
        return self._stare

    def schimba_starea(self, stare_noua: StareMentala) -> None:
        veche = self._stare
        self._stare = stare_noua
        self._istoric.append(
            f"{veche.value} → {stare_noua.value}"
        )

    def afiseaza_istoric(self) -> None:
        print(f"Istoricul lui {self._nume}:")
        for i, ev in enumerate(self._istoric, 1):
            print(f"  {i}. {ev}")

class Comanda(ABC):
    @abstractmethod
    def executa(self) -> None: ...

    @abstractmethod
    def anuleaza(self) -> None: ...

class ComandaSchimbaStare(Comanda):
    def __init__(self, student: Student, stare_noua: StareMentala):
        self._student    = student
        self._stare_noua = stare_noua
        self._stare_veche: StareMentala | None = None

    def executa(self) -> None:
        self._stare_veche = self._student.stare
        self._student.schimba_starea(self._stare_noua)
        print(f"✔ {self._student.nume}: {self._stare_noua.value}")

    def anuleaza(self) -> None:
        if self._stare_veche is not None:
            self._student.schimba_starea(self._stare_veche)
            print(f"↩ Anulat → {self._stare_veche.value}")

class Colega:
    def __init__(self):
        self._stiva_comenzi: list[Comanda] = []

    def da_comanda(self, comanda: Comanda) -> None:
        comanda.executa()
        self._stiva_comenzi.append(comanda)

    def anuleaza_ultima(self) -> None:
        if self._stiva_comenzi:
            self._stiva_comenzi.pop().anuleaza()
        else:
            print("Nicio comandă de anulat.")

if __name__ == "__main__":
    andrei  = Student("Andrei")
    colega  = Colega()

    colega.da_comanda(ComandaSchimbaStare(andrei, StareMentala.STRESAT))
    colega.da_comanda(ComandaSchimbaStare(andrei, StareMentala.DISPERAT))
    colega.da_comanda(ComandaSchimbaStare(andrei, StareMentala.MOTIVAT))
    colega.anuleaza_ultima()

    andrei.afiseaza_istoric()