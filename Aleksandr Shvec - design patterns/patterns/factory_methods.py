"""
Фабричный метод — это порождающий паттерн проектирования, который определяет общий интерфейс для
создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.
"""

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def deliver(self) -> str:
        pass


class Truck(Transport):
    def __init__(self, name: str):
        super().__init__(name)

    def deliver(self):
        print(f"Delivering truck... -> {self.__class__.__name__} {self.name}")


class Air(Transport):
    def __init__(self, name):
        super().__init__(name)

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
        return Air(name)


if __name__ == "__main__":
    company_truck = RoadLogistics()
    truck = company_truck.create_transport(name="Iveco")
    truck.deliver()

    company_air = AirLogistics()
    air = company_air.create_transport(name="Boing")
    air.deliver()
