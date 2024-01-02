from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, value) -> None:
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, value) -> None:
        for observer in self._observers:
            observer.update(self, value)


class Observer(ABC):
    def __init__(self):
        self.name = None

    @abstractmethod
    def update(self, subject: Subject, value) -> None:
        pass


class STRObserver(Observer):
    def __init__(self, str_list):
        super().__init__()
        self.str_list = str_list

    def update(self, subject: Subject, value) -> None:
        for x in self.str_list:
            x.ability_mod_var.set(value=value)


class DEXObserver(Observer):
    def __init__(self, dex_list):
        super().__init__()
        self.dex_list = dex_list

    def update(self, subject: Subject, value) -> None:
        for x in self.dex_list:
            x.ability_mod_var.set(value=value)

class CONObserver(Observer):
    def __init__(self, con_list):
        super().__init__()
        self.con_list = con_list

    def update(self, subject: Subject, value) -> None:
        for x in self.con_list:
            x.ability_mod_var.set(value=value)


class INTObserver(Observer):
    def __init__(self, int_list):
        super().__init__()
        self.int_list = int_list

    def update(self, subject: Subject, value) -> None:
        for x in self.int_list:
            x.ability_mod_var.set(value=value)


class WISObserver(Observer):
    def __init__(self, wis_list):
        super().__init__()
        self.wis_list = wis_list

    def update(self, subject: Subject, value) -> None:
        for x in self.wis_list:
            x.ability_mod_var.set(value=value)


class CHAObserver(Observer):
    def __init__(self, cha_list):
        super().__init__()
        self.cha_list = cha_list

    def update(self, subject: Subject, value) -> None:
        for x in self.cha_list:
            x.ability_mod_var.set(value=value)
