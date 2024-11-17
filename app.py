import csv

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import csv

BOT_TOKEN = "7922133300:AAHsSus2lBB9BqnxShd4X1OUSeSDG1lgBO4"

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def user_info_save(user_id, first_name, last_name):
    with open('users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(['User ID', 'First Name', 'Last Name'])
        writer.writerow([user_id, first_name, last_name])

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_info_save(user_id=message.from_user.id, first_name=message.from_user.first_name,
                   last_name=message.from_user.last_name)
    await message.answer(text='Hola!')


@dp.message_handler(commands=["how"])
async def handler(message: types.Message):
    await message.answer(text=f'Como Estas? {message.from_user.first_name}')


if __name__ == '__main__':
    executor.start_polling(dp)

