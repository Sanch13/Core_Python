from Ch_2_Data_Types.Python_types import replace_sep_in_sting


replace_sep_in_sting("""
""")

"""
Булевы операторы имеют более низкий приоритет по сравнению с фрагментами 
кода, которые они сравнивают. Это значит, что результаты фрагментов сначала вычисляются, 
а затем сравниваются. Cамый простой способ избежать путаницы — использовать 
круглые скобки: (5 < x) and (x < 10).
К False приравниваются следующие значения:
"""
print(bool(False), bool(None), bool(0), bool(0.0))              # False False False False
print(bool(''), bool([]), bool(()),  bool({}),  bool(set()))    # False False False False False
"""Все остальные значения приравниваются к True."""

"""В Python 3 8 появился оператор-морж, который выглядит следующим образом:
имя := выражение"""

total_limit = 100
pieces = 49
if (diff := total_limit - pieces) >= 0:
    print(f'{diff} - enough')
else:
    print(f'{diff} - not enough')


secret = 9
guess = 10
if guess < 7:
    print('too low')
elif guess > 7:
    print('too high')
else:
    print("just right")

