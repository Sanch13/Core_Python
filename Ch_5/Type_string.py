from Ch_2_Data_Types.Python_types import replace_sep_in_sting
import string

replace_sep_in_sting("""
""")

"""В Python вы можете объединить строки или строковые переменные с помощью
оператора +. Строки (не переменные) можно объединять, просто расположив их одну за
другой: "My word! " "A gentleman caller!"""

print("My word! " "A gentleman caller!")

"""Кроме отсутствия аргумента (когда подразумевается, что нужно найти пробелы)
или отдельного символа, возможна и ситуация, когда функция strip() удалит все
символы из последовательности"""
blurt = "What the...!!?"
print(blurt.strip('.?!'))
# string.whitespace 	#  \t\n\r\x0b\x0c
# string.punctuation  # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
ex = '   #$ What in tarnation .. {}[]*('
print(ex.strip(string.punctuation + string.whitespace))

