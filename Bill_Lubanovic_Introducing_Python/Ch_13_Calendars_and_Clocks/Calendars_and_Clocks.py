from datetime import date, timedelta, time, datetime

"""Модуль стандартной библиотеки datetime позволяет работать с датами и временем.
- date — для годов, месяцев и дней;
- time — для часов, минут, секунд и долей секунды;
- datetime — для даты и времени одновременно;
- timedelta — для интервалов даты и/или времени."""

halloween = date(2019, 10, 31)
# print(halloween)                  # 2019-10-31
"""метод today() для генерации сегодняшней даты"""
now = date.today()                  # 2022-09-26
"""timedelta используется для того, чтобы добавить некоторый временной интервал"""
one_day = timedelta(days=1)
tomorrow = now + one_day            # 2022-09-27
now + 25 * one_day                  # 2022-10-21
"""Объект date может иметь значение в диапазоне, начинающемся с date.min (year=1, month=1, day=1)
и заканчивающемся date.max (year=9999, month=12, day=31)."""
noon = time(12, 30, 0)              # 12:30:00
"""Порядок аргументов таков: от самой крупной единицы времени (часа) до самой мелкой 
(микросекунды). Если вы передадите не все аргументы, объект time предположит, что остальные 
имеют значение 0."""
# noon.hour, noon.minute, noon.microsecond            # 12 30 0
"""datetime также имеет метод isoformat()"""
some_day = datetime(2019, 1, 2, 3, 4, 5, 6)     # 2019-01-02 03:04:05.000006
"""datetime также имеет метод isoformat() Буква T, разделяет дату и время"""
some_day.isoformat()                            # 2019-01-02T03:04:05.000006
"""datetime имеет метод now(), с помощью которого можно получить текущие дату и время"""
datetime.now()                                  # 2022-09-26 14:22:28.731629
"""Объединить объекты date и time в объект datetime можно с помощью метода combine(). Объединить 
объекты date и time в объект datetime можно с помощью метода combine()"""
_now = date.today()
_time = time(13, 23, 4)
noon_today = datetime.combine(_now, _time)          # 2022-09-26 13:23:04
noon_today.date(), noon_today.time()                # 2022-09-26 13:23:04

"""В Python есть модуль datetime с объектом time, но есть и отдельный модуль time. Одним из 
способов представления абсолютного времени является подсчет количества секунд, прошедших с 
определенной начальной точки. В Unix считают количество секунд, прошедших с полуночи 
1 января 1970 года: это значение часто называют epoch.  Примерно в это время появилась система Unix
"""
import time

"""Функция time() модуля time возвращает текущее время как значение epoch"""
now = time.time()                             # 1664192242.504132
"""можете преобразовать значение epoch в строку с помощью функции ctime():"""
time.ctime(now)                               # Mon Sep 26 14:39:57 2022
"""Функция localtime() предоставляет время в вашем текущем часовом поясе,
 а функция gmtime() — в UTC"""
time.localtime()
# time.struct_time(tm_year=2022, tm_mon=9, tm_mday=26, tm_hour=14, tm_min=44, tm_sec=20,
# tm_wday=0, tm_yday=269, tm_isdst=0)
time.gmtime()
# time.struct_time(tm_year=2022, tm_mon=9, tm_mday=26, tm_hour=11, tm_min=45, tm_sec=16,
# tm_wday=0, tm_yday=269, tm_isdst=0)
"""структура struct_time также может играть роль именованного кортежа"""
second = time.localtime()[5]    # 54
"""Функция mktime() идет в другом направлении и преобразует объект struct_time в секунды epoch:"""
time.mktime(time.localtime())        # 1664194369.0
"""
Небольшой совет: везде, где возможно, используйте часовой пояс UTC. UTC — это абсолютное время,
            не зависящее от часовых поясов. Если у вас есть сервер, установите его время в UTC,
            не привязываясь к местному времени.
Еще один совет: никогда не используйте летнее время, если можно без этого обойтись."""

"""Читаем и записываем дату и время
Вы также можете преобразовывать дату и время с помощью функции strftime(). Она предоставляется 
как метод в объектах datetime, date и time и как функция в модуле time. Функция strftime() 
использует для вывода информации на экран спецификаторы формата
Спецификатор     Единица            Диапазон
                даты/времени
%Y                 Год                1900–…
%m                 Месяц              01–12
%B                 Название месяца    Январь…
%b                 Сокр. для месяца   Янв…
%d                 День месяца        01–31
%А                 Название дня       Воскресенье…
А                  Сокр/ для дня      Вск…
%Н                 Часы (24 часа)     00–23
%I                 Часы (12 часов)    01–12
%p                 AM или PM          AM, PM
%M                 Минуты             00–59
%S                 Секунды            00–59

"""
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
time.strftime(fmt)                      # It's Monday, September 26, 2022, local time 03:26:06PM
time.strftime(fmt, time.localtime())    # It's Monday, September 26, 2022, local time 03:27:46PM
"""Если мы попробуем сделать это с объектом date, функция отработает только для
даты. Время будет установлено в полночь"""
cur_time = date(2022, 10, 23)
cur_time.strftime(fmt)                  # It's Sunday, October 23, 2022, local time 12:00:00AM
"""Для объекта time будут преобразованы только части, касающиеся времени"""
# time(10, 35).strftime(fmt)            # "It's Monday, January 01, 1900, local time 10:35:00AM"
"""Используйте функцию strptime() с такой же строкой формата. Эта строка работает не так, как
регулярные выражения, — части строки, не касающиеся формата (без символа %), должны совпадать 
точно. год-месяц-день, например 2019-01-29."""
import time
fmt = "%Y-%m-%d"
# time.strptime("2019 01 29", fmt)
# ValueError: time data '2019 01 29' does not match format '%Y-%m-%d'
time.strptime("2019-01-29", fmt)  # time.struct_time(tm_year=2019, tm_mon=1, tm_mday=29, tm_hour=0,
# tm_min=0, tm_sec=0, tm_wday=1, tm_yday=29, tm_isdst=-1)
"""Даже если строка совпадает с заданным форматом, но одно из значений находится вне диапазона,
 будет сгенерировано исключение"""
"""Имена соответствуют вашей локали — региональному набору настроек операционной системы. 
Чтобы вывести на экран другие названия месяцев и дней, измените свою локаль с помощью функции
 setlocale(): ее первый аргумент — locale.LC_TIME для даты и времени, 
 а второй аргумент — это строка, содержащая сокращенное обозначение языка и страны."""
import locale
birth_day_ks = date(1988, 6, 27)
# for lang_country in ['en_en', 'ru_ru', 'fr_fr', 'lt_lt', 'lv_lv', 'ja_jp']:
#     locale.setlocale(locale.LC_TIME, lang_country)
#     print(birth_day_ks.strftime('%A, %B %d'))
"""получить все сразу аргументы lang_country"""
# print(locale.locale_alias.items())

# TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS
"""13.1. Запишите текущие дату и время как строку в текстовый файл today.txt."""
fmt = "%d-%m-%Y, local time %H:%M:%S"
today = time.strftime(fmt)
with open('today.txt', 'w') as file:
    file.write(today)           # 27-09-2022, local time 08:54:15 # --> in file today.txt
###################################################################################################
"""13.2. Прочтите текстовый файл today.txt и разместите данные в строке today_string."""
with open('today.txt', 'r') as file:
    today_string = file.read()  # 27-09-2022, local time 08:58:46
###################################################################################################
"""13.3. Проанализируйте дату из строки today_string."""
###################################################################################################
"""13.4. Создайте объект date с датой вашего рождения."""
date_bd = date(1985, 2, 13)
###################################################################################################
"""13.5. В какой день недели вы родились?"""
fmt = "Your Birth Day %d %B %Y. You were born on %A"
date_bd.strftime(fmt)    # Your Birth Day 13 February 1985. You were born on Wednesday
###################################################################################################
"""13.6. Когда вам будет (или уже было) 10 000 дней от роду?"""
delta = timedelta(days=10_000)
date_bd + delta      # 2012-07-01
###################################################################################################

