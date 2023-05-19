import pandas as pd
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6238496236:AAFWzWyATpKFDJHeDtUXO_rztC6YJaCZNpg'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

file_path = "table.xlsx"

data = pd.read_excel(file_path)


@dp.message_handler(commands=['help'])
async  def help(message: types.Message):
   await message.answer("Чтобы узнать успеваемость вашего ребенка просто введите его имя")


@dp.message_handler()
async def endform(message: types.Message):
    student_name = message.text

    student_data = data[data['Имя'] == student_name]

    if student_data.empty:
        await message.reply("Данные для указанного школьника не найдены.")
    else:
        await message.answer(f"Успеваемость школьника {student_name}:\n {student_data}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
