"""
Строитель — это порождающий паттерн проектирования, который позволяет создавать сложные объекты
пошагово. Строитель даёт возможность использовать один и тот же код строительства для получения
разных представлений объектов.

📦 Когда использовать Builder?
✅ Разделение ответственности — верно!
✅ Валидация в строителе — верно!
➕ Читабельность: .select("name").from_table("users") понятнее, чем
    Query(["name"], "users", None, None, None, None)
➕ Гибкость: Можно вызывать методы в любом порядке (кроме build())
➕ Переиспользование: Один строитель → много объектов

Много параметров конструктора (больше 4-5)
Некоторые параметры опциональны, но их много
Процесс создания состоит из шагов (сначала одно, потом другое)
Нужны разные представления одного объекта (классический бургер, веган-бургер)
"""

"""
Паттерн Builder (Строитель)
Пример: Конструктор бургеров
"""

from typing import Optional
from dataclasses import dataclass, field


# === ПРОДУКТ (то, что строим) ===
@dataclass
class Burger:
    """Сложный объект, который мы создаём пошагово"""
    bun_type: str
    patty_type: str
    patty_count: int = 1
    cheese: bool = False
    vegetables: list[str] = field(default_factory=list)
    sauces: list[str] = field(default_factory=list)
    extras: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        result = [f"🍔 Бургер на булочке '{self.bun_type}'"]
        result.append(f"   Котлета: {self.patty_count}x {self.patty_type}")
        if self.cheese:
            result.append("   🧀 Сыр")
        if self.vegetables:
            result.append(f"   🥬 Овощи: {', '.join(self.vegetables)}")
        if self.sauces:
            result.append(f"   🥫 Соусы: {', '.join(self.sauces)}")
        if self.extras:
            result.append(f"   ✨ Дополнительно: {', '.join(self.extras)}")
        return "\n".join(result)


# === СТРОИТЕЛЬ (Builder) ===
class BurgerBuilder:
    """
    Строитель позволяет пошагово конфигурировать объект.
    Методы возвращают self для chain-вызовов (fluent interface).
    """

    def __init__(self):
        self.reset()

    def reset(self) -> 'BurgerBuilder':
        """Сброс к начальному состоянию"""
        self._bun_type: Optional[str] = None
        self._patty_type: Optional[str] = None
        self._patty_count: int = 1
        self._cheese: bool = False
        self._vegetables: list[str] = []
        self._sauces: list[str] = []
        self._extras: list[str] = []
        return self

    def set_bun(self, bun_type: str) -> 'BurgerBuilder':
        """Выбор типа булочки"""
        self._bun_type = bun_type
        return self

    def set_patty(self, patty_type: str, count: int = 1) -> 'BurgerBuilder':
        """Выбор котлеты"""
        self._patty_type = patty_type
        self._patty_count = count
        return self

    def add_cheese(self) -> 'BurgerBuilder':
        """Добавить сыр"""
        self._cheese = True
        return self

    def add_vegetable(self, vegetable: str) -> 'BurgerBuilder':
        """Добавить овощ"""
        self._vegetables.append(vegetable)
        return self

    def add_sauce(self, sauce: str) -> 'BurgerBuilder':
        """Добавить соус"""
        self._sauces.append(sauce)
        return self

    def add_extra(self, extra: str) -> 'BurgerBuilder':
        """Добавить дополнительный ингредиент"""
        self._extras.append(extra)
        return self

    def build(self) -> Burger:
        """
        Финальный метод: создаём объект и валидируем.
        После build() строитель сбрасывается для повторного использования.
        """
        # Валидация
        if not self._bun_type:
            raise ValueError("Необходимо выбрать тип булочки!")
        if not self._patty_type:
            raise ValueError("Необходимо выбрать котлету!")

        # Создание объекта
        burger = Burger(
            bun_type=self._bun_type,
            patty_type=self._patty_type,
            patty_count=self._patty_count,
            cheese=self._cheese,
            vegetables=self._vegetables.copy(),
            sauces=self._sauces.copy(),
            extras=self._extras.copy()
        )

        # Сброс для повторного использования
        self.reset()

        return burger


# === ДИРЕКТОР (опционально) ===
class BurgerDirector:
    """
    Директор знает популярные рецепты и может создавать их одной командой.
    Это необязательный компонент паттерна Builder.
    """

    def __init__(self, builder: BurgerBuilder):
        self._builder = builder

    def make_classic(self) -> Burger:
        """Классический бургер"""
        return (self._builder
                .set_bun("кунжутная")
                .set_patty("говядина")
                .add_cheese()
                .add_vegetable("салат")
                .add_vegetable("помидор")
                .add_vegetable("лук")
                .add_sauce("кетчуп")
                .add_sauce("горчица")
                .build())

    def make_deluxe(self) -> Burger:
        """Бургер делюкс"""
        return (self._builder
                .set_bun("бриошь")
                .set_patty("мраморная говядина", count=2)
                .add_cheese()
                .add_vegetable("руккола")
                .add_vegetable("карамелизированный лук")
                .add_vegetable("маринованные огурцы")
                .add_sauce("трюфельный майонез")
                .add_extra("бекон")
                .add_extra("жареное яйцо")
                .build())

    def make_vegan(self) -> Burger:
        """Веган-бургер"""
        return (self._builder
                .set_bun("цельнозерновая")
                .set_patty("нут")
                .add_vegetable("салат")
                .add_vegetable("авокадо")
                .add_vegetable("помидор")
                .add_sauce("веган-майонез")
                .build())


# === ДЕМОНСТРАЦИЯ ===
if __name__ == "__main__":
    print("=" * 50)
    print("ПАТТЕРН BUILDER: ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ")
    print("=" * 50)

    # 1. Создание кастомного бургера (прямое использование Builder)
    print("\n1️⃣ Кастомный бургер (через Builder):\n")
    builder = BurgerBuilder()

    custom_burger = (builder
                     .set_bun("с маком")
                     .set_patty("курица")
                     .add_cheese()
                     .add_vegetable("огурцы")
                     .add_sauce("барбекю")
                     .build())

    print(custom_burger)

    # 2. Использование Director для стандартных рецептов
    print("\n" + "=" * 50)
    print("\n2️⃣ Стандартные рецепты (через Director):\n")

    director = BurgerDirector(builder)

    print("Классический бургер:")
    print(director.make_classic())

    print("\n" + "-" * 50)
    print("\nБургер Делюкс:")
    print(director.make_deluxe())

    print("\n" + "-" * 50)
    print("\nВеган-бургер:")
    print(director.make_vegan())

    # 3. Повторное использование builder
    print("\n" + "=" * 50)
    print("\n3️⃣ Создание нескольких бургеров подряд:\n")

    burger1 = (builder
               .set_bun("обычная")
               .set_patty("свинина")
               .add_sauce("кетчуп")
               .build())

    burger2 = (builder
               .set_bun("кунжутная")
               .set_patty("говядина", count=2)
               .add_cheese()
               .build())

    print("Бургер 1:")
    print(burger1)
    print("\nБургер 2:")
    print(burger2)

    print("\n" + "=" * 50)
