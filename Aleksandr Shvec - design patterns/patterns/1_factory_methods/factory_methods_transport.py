"""
Фабричный метод — это порождающий паттерн проектирования, который определяет общий интерфейс для
создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.

✅ Единая ответственность: Код создания объектов вынесен в отдельное место
✅ Открыт для расширения, закрыт для модификации: Можем добавлять новые типы, не трогая базовый класс
✅ Слабая связанность: Клиентский код не зависит от конкретных классов
"""

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def deliver(self) -> None:
        pass


class Truck(Transport):
    def deliver(self):
        print(f"Delivering truck... -> {self.__class__.__name__} {self.name}")


class Plane(Transport):
    def deliver(self):
        print(f"Delivering air... -> {self.__class__.__name__} {self.name}")


class LogisticsCompany(ABC):
    @abstractmethod
    def create_transport(self, name: str) -> Transport:
        pass


class RoadLogistics(LogisticsCompany):
    def create_transport(self, name: str) -> Transport:
        return Truck(name)


class AirLogistics(LogisticsCompany):
    def create_transport(self, name: str) -> Transport:
        return Plane(name)


if __name__ == "__main__":
    company_truck = RoadLogistics()
    truck = company_truck.create_transport(name="Iveco")
    truck.deliver()

    company_air = AirLogistics()
    air = company_air.create_transport(name="Boing")
    air.deliver()
