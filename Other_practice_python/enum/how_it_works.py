from enum import Enum
from datetime import date

# class Weekday(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7
#
#     @classmethod
#     def from_date(cls, day):
#         """Return day of the week, where Monday == 1 ... Sunday == 7."""
#         return cls(day.isoweekday())


# print(type(Weekday.MONDAY))  # <enum 'Weekday'>
# print(Weekday.SUNDAY)  # Weekday.SUNDAY
# print(Weekday(7).name)  # SUNDAY
# print(Weekday["SATURDAY"])  # Weekday.SATURDAY
# print(Weekday(3))  # Weekday.WEDNESDAY
# print(isinstance(Weekday.FRIDAY, Weekday))  # True
# ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
# print([obj.name for obj in Weekday])
# print([obj.value for obj in Weekday])  # [1, 2, 3, 4, 5, 6, 7]
# print(Weekday.from_date(date.today()).name.title())  # Thursday
#############################################################################################

from enum import Flag


class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64


# Flag также позволяет нам объединить несколько членов в одну переменную
weekend = Weekday.SATURDAY | Weekday.SUNDAY
# print(weekend)  # Weekday.SATURDAY|SUNDAY
# Вы даже можете перебирать Flag переменную:
print([day for day in weekend])  #[<Weekday.SATURDAY: 32>, <Weekday.SUNDAY: 64>]


