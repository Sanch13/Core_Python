"""
Задание:
У тебя есть два класса для работы с температурой:

EuropeanThermometer — возвращает температуру в Цельсиях методом get_celsius()
AmericanThermometer — возвращает температуру в Фаренгейтах методом read_fahrenheit()

Создай:

Общий интерфейс Thermometer с методом get_temperature() (возвращает в Цельсиях)
Адаптеры для обоих термометров
Функцию display_temperature(thermometer), которая работает с любым термометром

Формула: C = (F - 32) * 5/9
Пиши код — потом обсудим! Если будут вопросы — спрашивай.
"""
from abc import ABC, abstractmethod


class Thermometer(ABC):
	@abstractmethod
	def get_temperature(self) -> float:
		pass


class EuropeanThermometer(Thermometer):
	def __init__(self, celsius: float):
		self._celsius = celsius

	def get_temperature(self) -> float:
		return self._celsius


class AmericanThermometer:
	def __init__(self, fahrenheit: float):
		self._fahrenheit = fahrenheit

	def read_fahrenheit(self) -> float:
		return self._fahrenheit


class KelvinThermometer:
	def __init__(self, kelvin: float):
		self._kelvin = kelvin

	def measure_kelvin(self) -> float:
		return self._kelvin


class KelvinThermometerAdapter(Thermometer):
	def __init__(self, kelvin_thermometer: KelvinThermometer):
		self._kelvin_thermometer = kelvin_thermometer

	def get_temperature(self) -> float:
		kelvin_tempo = self._kelvin_thermometer.measure_kelvin()
		if kelvin_tempo < 0:
			raise ValueError(f"Invalid Kelvin temperature: {kelvin_tempo}K (must be >= 0)")
		celsius = kelvin_tempo - 273.15
		return celsius


class AmericanThermometerAdapter(Thermometer):
	def __init__(self, american_thermometer: AmericanThermometer):
		self._thermometer = american_thermometer

	def get_temperature(self) -> float:
		fahrenheit = self._thermometer.read_fahrenheit()
		celsius = (fahrenheit - 32) * 5 / 9
		return celsius


def display_temperature(thermometer: Thermometer):
	temp = thermometer.get_temperature()
	print(f"Температура: {temp:.1f}°C")


if __name__ == '__main__':
	thermometer_eu = EuropeanThermometer(celsius=23.3)
	thermometer_na_f = AmericanThermometer(fahrenheit=77.0)
	kelvin_thermometer = KelvinThermometer(kelvin=100.0)

	thermometer_na_adapter = AmericanThermometerAdapter(american_thermometer=thermometer_na_f)
	kelvin_thermometer_adapter = KelvinThermometerAdapter(kelvin_thermometer=kelvin_thermometer)

	display_temperature(thermometer=thermometer_eu)
	display_temperature(thermometer=thermometer_na_adapter)
	display_temperature(thermometer=kelvin_thermometer_adapter)
