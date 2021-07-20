#Врубаем библиотеки
import logging
from aiogram import Bot, Dispatcher, executor, types

#Сам бот
bot = Bot(token="XYI")
#Хэндлеры теперь через него. 
#Появились доп.варианты для работы
dp = Dispatcher(bot)
#Логшинг
logging.basicConfig(level=logging.INFO)


#3.1
@dp.message_handler(command="test1")
async def cmd_test(message: types.Message):
	await message.reply("test 1")

#3.2
async def cmd_test2(message: types.Message):
	await message.reply("test 2")

dp.register_message_handler(cmd_test2, commands="test2")



if __name__ = "__main__":
	executor.start_polling(dp, skip_updates=True)


