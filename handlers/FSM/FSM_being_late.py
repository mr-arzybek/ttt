# =======================================================================================================================
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards.buttons import cancel_markup, staff_markup, submit_markup, city_markup

from db.db_bish.ORM_Bish import bish_sql_being_late_insert
from db.db_osh.ORM_Osh import osh_sql_being_late_insert
from db.db_moscow_1.ORM_Moscow_1 import moscow_1_sql_being_late_insert
from db.db_moscow_2.ORM_Moscow_2 import moscow_2_sql_being_late_insert


# =======================================================================================================================

class fsm_control(StatesGroup):
    full_name = State()
    date = State()
    time = State()
    city = State()
    submit = State()


async def fsm_start(message: types.Message):
    await fsm_control.full_name.set()
    await message.answer('ФИО сотрудника?', reply_markup=cancel_markup)


async def load_full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text
    await fsm_control.next()
    await message.answer("Дата?\n"
                         "Образец: 12 августа")


async def load_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await fsm_control.next()
    await message.answer('Время прихода?\n'
                         'Образец: 9:34')


async def load_time(message: types.Message, state: FSMContext):
    # Вот здесь прописать логику, если челик опоздал, то отправить ему сообщение
    # Либо для всех установить одно время и, если он опоздал, то сказать что он опоздал
    async with state.proxy() as data:
        data['time'] = message.text
    await fsm_control.next()
    await message.answer('Город?\n'
                         'Если Москва, то указать какой филиал!\n'
                         'Выберите снизу по кнопкам, какой город!',
                         reply_markup=city_markup)


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        await message.answer(f'Данные: \n'
                             f'ФИО: {data["full_name"]}\n'
                             f'Дата: {data["date"]}\n'
                             f'Время прибытия: {data["time"]}\n'
                             f'Город: {data["city"]}')

    await fsm_control.next()
    await message.answer('Всё верно?', reply_markup=submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            if data['city'] == 'Бишкек':
                await bish_sql_being_late_insert(state)
                await message.answer('Готово!', reply_markup=staff_markup)
                await state.finish()

            elif data['city'] == 'ОШ':
                await osh_sql_being_late_insert(state)
                await message.answer('Готово!', reply_markup=staff_markup)
                await state.finish()

            elif data['city'] == 'Москва 1-филиал':
                await moscow_1_sql_being_late_insert(state)
                await message.answer('Готово!', reply_markup=staff_markup)
                await state.finish()

            elif data['city'] == 'Москва 2-филиал':
                await moscow_2_sql_being_late_insert(state)
                await message.answer('Готово!', reply_markup=staff_markup)
                await state.finish()

        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено', reply_markup=staff_markup)
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=staff_markup)


# =======================================================================================================================

def register_control(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['контроль_сотрудников'])
    dp.register_message_handler(load_full_name, state=fsm_control.full_name)
    dp.register_message_handler(load_data, state=fsm_control.date)
    dp.register_message_handler(load_time, state=fsm_control.time)
    dp.register_message_handler(load_city, state=fsm_control.city)

    dp.register_message_handler(load_submit, state=fsm_control.submit)