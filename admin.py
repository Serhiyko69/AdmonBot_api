import datetime
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from kbs import *
from connect import TOKEN, collection
from api import get_info
from aiogram.types import CallbackQuery

from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
storage = MemoryStorage()
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)

# ID вашої групи
GROUP_ID = -1001972496725


def generate_towns_keyboard(info):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    for item in info:
        town, region = item.split(' (')
        region = region.rstrip(')')
        region = f"{region}.обл"
        button_text = f"{town} ({region})"
        keyboard.add(button_text)
    return keyboard


def generate_dates_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    today = datetime.date.today()
    for i in range(7):
        date = today + datetime.timedelta(days=i)
        button_text = date.strftime('%Y-%m-%d')
        button = InlineKeyboardButton(button_text, callback_data=f"date:{date}")
        keyboard.add(button)
    return keyboard


@dp.message_handler(commands=['start'])
async def start_def(message: types.Message):
    await message.answer('Привіт, що хочеш зробити?', reply_markup=kb_client)


# Обробник натискання на кнопку "Активні зустрічі"
@dp.message_handler(text=['Переглянути активні зустрічі'])
async def active_meetings(message: types.Message):
    user_id = message.from_user.id

    # Отримати активні зустрічі користувача з бази даних
    active_meetings = collection.find({"user_id": user_id})

    if active_meetings:
        response = "Ваші активні зустрічі:\n"
        for meeting in active_meetings:
            response += f"Зустріч у місті {meeting['city']}, {meeting['region']} область, Дата: {meeting['datetime']}\n"
    else:
        response = "Наразі у вас немає активних зустрічей."

    await message.answer(response)


@dp.message_handler(text=['Створити зустріч'])
async def start_create_meeting(message: types.Message, state: FSMContext):
    await message.answer('Введи назву населеного пункту де буде зустріч:')
    await state.set_state('waiting_for_town')  # Встановлюємо стан для очікування назви населеного пункту


@dp.message_handler(state='waiting_for_town')
async def process_town_input(message: types.Message, state: FSMContext):
    selected_town = message.text

    async with state.proxy() as data:
        data['selected_town'] = selected_town

    info = get_info(selected_town)

    if info:
        await state.update_data(info=info)  # Зберігаємо інформацію про населені пункти
        await message.answer("Виберіть населений пункт:", reply_markup=generate_towns_keyboard(info))
        await state.set_state('waiting_for_selected_town')  # Встановлюємо стан для очікування вибору населеного пункту
    else:
        await message.answer("Назва населеного пункту некоректна. Введіть іншу назву:")


@dp.callback_query_handler(lambda c: c.data.startswith('date:'), state='waiting_for_date')
async def process_selected_date_input(callback_query: CallbackQuery, state: FSMContext):
    data = callback_query.data.split(':')
    selected_date = data[1]

    # Отримуємо вибраний населений пункт і дату зі стану FSMContext
    async with state.proxy() as data:
        selected_town = data.get('selected_town')

    # Тут ви можете використовувати обрані дані для створення зустрічі або іншої логіки
    # Наприклад, відправити повідомлення про створену зустріч

    await callback_query.message.answer(f"Ви вибрали місто: {selected_town}\nДата: {selected_date}")

    # Скидаємо стан до початкового стану
    await state.finish()


@dp.callback_query_handler(lambda c: c.data.startswith('town:'))
async def process_selected_town_input(callback_query: CallbackQuery):
    data = callback_query.data.split(':')
    selected_town = data[1]

    # Зберігаємо вибраний населений пункт у стані FSMContext
    async with FSMContext(callback_query.message.chat.id) as state:
        await state.update_data(selected_town=selected_town)

        # Встановлюємо стан для очікування вибору дати
        await state.set_state('waiting_for_date')

    # Відправляємо клавіатуру для вибору дати
    await bot.send_message(callback_query.message.chat.id, "Виберіть дату:", reply_markup=generate_dates_keyboard())


# Обробник для вибору населеного пункту
@dp.callback_query_handler(lambda c: c.data.startswith('town:'))
async def process_selected_town_input(callback_query: CallbackQuery):
    data = callback_query.data.split(':')
    selected_town = data[1]

    # Зберігаємо вибраний населений пункт у стані FSMContext
    async with FSMContext(callback_query.message.chat.id) as state:
        await state.update_data(selected_town=selected_town)

        # Встановлюємо стан для очікування вибору дати
        await state.set_state('waiting_for_date')

    # Відправляємо клавіатуру для вибору дати
    await bot.send_message(callback_query.message.chat.id, "Виберіть дату:", reply_markup=generate_dates_keyboard())


@dp.callback_query_handler(lambda c: c.data.startswith('date:'), state='waiting_for_date')
async def process_selected_date_input(callback_query: CallbackQuery, state: FSMContext):
    data = callback_query.data.split(':')
    selected_date = data[1]

    # Отримуємо вибраний населений пункт і дату зі стану FSMContext
    async with state.proxy() as data:
        selected_town = data.get('selected_town')

    # Тут ви можете використовувати обрані дані для створення зустрічі або іншої логіки
    # Наприклад, відправити повідомлення про створену зустріч

    await callback_query.message.answer(f"Ви вибрали місто: {selected_town}\nДата: {selected_date}")

    # Скидаємо стан до початкового стану
    await state.finish()


# Функція-запуск при старті
async def on_startup(_):
    print('Бот запущено')


# Запуск бота
if __name__ == "__main__":
    from aiogram import executor

    executor.start_polling(dp, on_startup=on_startup)