from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Створити зустріч')
button2 = KeyboardButton('Переглянути активні зустрічі')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button1], [button2]])
#############################################################################
cities = {
'Львівська':[
'Львів',
'Золочів',
'Броди',
'Стрий',
'Буськ',
'Яворів',
'Городок',
'Самбір'],

'Київська': [
'Київ',
'Ірпінь',
'Біла Церква',
'Бровари',
'Обухів',
'Бородянка',
'Фастів',
'Бориспіль'],

'Харківська': [
'Харків',
'Ізюм'],

'Одеська': [
'Одеса',
'Ізмаїл']
}

cities_per_row = 2

# Створюємо клавіатуру для вибору області
location_k = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)

for region in cities.keys():
    region_button = KeyboardButton(region)
    location_k.insert(region_button)

# Створюємо клавіатуру для вибору міст після вибору області
city_k = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, row_width=cities_per_row)
#############################################################################
kb_region = ReplyKeyboardMarkup()

b3 = KeyboardButton({'Львівська': ['Львів', 'Дрогобич']})
b4 = KeyboardButton('Київська')
b5 = KeyboardButton('Харківська')
b6 = KeyboardButton('Одеська')

kb_region.add(b3).add(b4).add(b5).add(b6)
#############################################################################

kb_Lviv = ReplyKeyboardMarkup(resize_keyboard=True)

Lviv1 = KeyboardButton('Львів')
Lviv2 = KeyboardButton('Золочів')
Lviv3 = KeyboardButton('Броди')
Lviv4 = KeyboardButton('Стрий')
Lviv5 = KeyboardButton('Буськ')
Lviv6 = KeyboardButton('Яворів')
Lviv7 = KeyboardButton('Городок')
Lviv8 = KeyboardButton('Самбір')

kb_Lviv.add(Lviv1).add(Lviv2).add(Lviv3).add(Lviv4).add(Lviv5).add(Lviv6).add(Lviv7).add(Lviv8)
#############################################################################

kb_Kyiv = ReplyKeyboardMarkup(resize_keyboard=True)

Kyiv1 = KeyboardButton('Київ')
Kyiv2 = KeyboardButton('Ірпінь')
Kyiv3 = KeyboardButton('Біла Церква')
Kyiv4 = KeyboardButton('Бровари')
Kyiv5 = KeyboardButton('Обухів')
Kyiv6 = KeyboardButton('Бородянка')
Kyiv7 = KeyboardButton('Фастів')
Kyiv8 = KeyboardButton('Бориспіль')

kb_Kyiv.add(Kyiv1).add(Kyiv2).add(Kyiv3).add(Kyiv4).add(Kyiv5).add(Kyiv6).add(Kyiv7).add(Kyiv8)
#############################################################################

keyboard = InlineKeyboardMarkup()
button = InlineKeyboardButton(text="Вказати дату і час", callback_data="set_datetime")
keyboard.insert(button)

kb_cancel = kb_Kyiv = ReplyKeyboardMarkup(resize_keyboard=True)
cancel = KeyboardButton('Відмінити')
kb_cancel.add(cancel)



# Кількість кнопок в рядку для років
years_per_row = 4

year_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, row_width=years_per_row)

# Створюємо кнопки для клавіатури років
year_buttons = [KeyboardButton(str(year)) for year in range(2023, 2043)]  # Змініть діапазон на потрібний

# Розбиваємо кнопки на рядки
for row in range(0, len(year_buttons), years_per_row):
    year_keyboard.row(*year_buttons[row:row + years_per_row])


# Створення клавіатури для вибору місяця

buttons_per_row = 4

month_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, row_width=buttons_per_row)

# Створюємо кнопки для клавіатури
buttons = [KeyboardButton(str(i)) for i in range(1, 13)]

# Розбиваємо кнопки на рядки
for row in range(0, len(buttons), buttons_per_row):
    month_keyboard.row(*buttons[row:row + buttons_per_row])


# Створення клавіатури для вибору дня
days_per_row = 6

day_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, row_width=days_per_row)

# Створюємо кнопки для клавіатури днів
day_buttons = [KeyboardButton(str(day)) for day in range(1, 32)]

# Розбиваємо кнопки на рядки
for row in range(0, len(day_buttons), days_per_row):
    day_keyboard.row(*day_buttons[row:row + days_per_row])

# Створення клавіатури для вибору години
# Кількість кнопок в рядку для годин
hours_per_row = 4

hour_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, row_width=hours_per_row)

# Створюємо кнопки для клавіатури годин
hour_buttons = [KeyboardButton(str(hour)) for hour in range(0, 24)]

# Розбиваємо кнопки на рядки
for row in range(0, len(hour_buttons), hours_per_row):
    hour_keyboard.row(*hour_buttons[row:row + hours_per_row])
# Кількість кнопок в рядку для хвилин
minutes_per_row = 4

minute_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, row_width=minutes_per_row)

# Створюємо кнопки для клавіатури хвилин
minute_buttons = [KeyboardButton(str(minute)) for minute in range(0, 60, 5)]  # Змініть крок на потрібний

# Розбиваємо кнопки на рядки
for row in range(0, len(minute_buttons), minutes_per_row):
    minute_keyboard.row(*minute_buttons[row:row + minutes_per_row])

