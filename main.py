TOKEN = '755388953:AAGfFvv8Wu994FKJXZepZKyidTJvgkPuPgE'

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, ConversationHandler, 
						Filters, MessageHandler, RegexHandler)
import logging
from datetime import datetime
import os

global path
CATEGORY, SERVICE, LOCATION, GO, MESSAGE = range(5)

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Привет! С этим ботом вы можете записать ваш отчет\nНажмите /new, чтобы записать новый отчет')

def help(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='/new - записать новый отчет\n')

def new(bot, update):
	reply_keyboard = [['Республика Казахстан', 'г. Астана'], ['г. Алматы', 'Акмолинская область'], 
					['Актюбинская область', 'Алматинская область'], ['Атырауская область', 'Западно-Казахстанская область'],
					['Жамбылская область', 'Карагандинская область'], ['Костанайская область', 'Кызылординская область'],
					['Мангистауская область', 'Южно-Казахстанская область'], ['Павлодарская область', 'Северо-Казахстанская область'],
					['Восточно-Казахстанская область', 'г. Шымкент']]
	response= ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
	update.message.reply_text(
        'Пожалуйста, выберите локацию\n'
        'Нажмите /cancel, чтобы завершить операцию', reply_markup=response)
	
	return SERVICE

def location(bot, update):
	reply_keyboard = [['Республика Казахстан', 'г. Астана'], ['г. Алматы', 'Акмолинская область'], 
					['Актюбинская область', 'Алматинская область'], ['Атырауская область', 'Западно-Казахстанская область'],
					['Жамбылская область', 'Карагандинская область'], ['Костанайская область', 'Кызылординская область'],
					['Мангистауская область', 'Южно-Казахстанская область'], ['Павлодарская область', 'Северо-Казахстанская область'],
					['Восточно-Казахстанская область', 'г. Шымкент']]
	response= ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
	update.message.reply_text(
        'Пожалуйста, выберите локацию\n'
        'Нажмите /cancel, чтобы завершить операцию', reply_markup=response)
	return SERVICE

def service(bot, update):
	reply_keyboard = [['Документирование'], ['Регистрация Физических лиц и граждан'], 
					['Регистрация Физических и юридических лиц'], ['Семья и дети'],
					['Права на имущество и интеллектуальную собственность'], 
					['Здоровье, медицина и здравоохранение'], ['Труд и социальная защита населения'],
					['Образование и наука'], ['Бизнес и предпринимательство'], ['Туризм'],
					['Транспорт и коммуникации'], ['Сельское хозяйство'],
					['Охрана окружающей среды и животного мира, природные ресурсы'],
					['Промышленность, индустрия и технологии'], ['Нефтегазовая сфера'],
					['Налоговое администрирование, бухгалтерский учет и финансовая отчетность, аудиторская деятельность'],
					['Государственное регулирование, контроль и надзор финансового рынка и финансовых организаций'],
					['Таможенное дело'], ['Безопасность, оборона и правосудие'], ['Защита конкуренции'],
					['Религия'], ['Земельные отношения, геодезия и картография'], ['Культура, информация и связь'],
					['Чрезвычайные ситуации'], ['Физическая культура и спорт'], ['Архитектурно-градостроительная деятельность'],
					['Жилищно-коммунальное хозяйство'], ['Внешняя политика и иностранные дела'], 
					['Регулирование естественных монополий'], ['Государственная служба'], ['Другие']]
	response= ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
	update.message.reply_text(
        'Пожалуйста, выберите государственную службу, к которой относится ваш отчет\n'
        'Нажмите /cancel, чтобы завершить операцию', reply_markup=response)
	
	return CATEGORY

def category(bot, update):
	reply_keyboard = [['Безопасность', 'Бизнес'], ['Государственное управление', 'ЖКХ'],
					['Здравоохранение', 'Земельные отношения'], ['Инфраструктура', 'Коррупция'],
					['Трудовые отношения', 'Судебно-правовая система'], ['Межэтнические и религиозные отношения', 'Образование'],
					['Общественный транспорт', 'Транспорт и автомобильные дороги'], ['Экология', 'Другое']]
	response= ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
	update.message.reply_text(
		'Пожалуйста, выберите категорию\n'
        'Нажмите /cancel, чтобы завершить операцию', reply_markup=response)

	return GO

def go(bot, update):
	update.message.reply_text('Пожалуйста, напишите текст вашего отчета',
                              reply_markup=ReplyKeyboardRemove())
	return MESSAGE

def echo(bot, update):
    update.message.reply_text(update.message.text)

def get_username(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=update.message.from_user.username)

def time(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=str(update.message.date))

def create_folder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print('panic!')

def file(bot, update):
	f = open('./test/hello.txt', 'w')
	f.write('hello world')
	f.close()
	bot.send_message(chat_id=update.message.chat_id, text='File created')

def folder(bot, update):
	create_folder('./test')
	bot.send_message(chat_id=update.message.chat_id, text='Folder created')

def cancel(bot, update):
    update.message.reply_text('Операция отменена',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	conv_handler = ConversationHandler(
        entry_points=[CommandHandler('new', new)],

        states={
            LOCATION: [
                MessageHandler(Filters.text, location),
                CommandHandler('cancel', cancel)
                ],
            SERVICE: [
            	MessageHandler(Filters.text, service),
                CommandHandler('cancel', cancel)
            ],
            CATEGORY: [
                MessageHandler(Filters.text, category),
                CommandHandler('cancel', cancel)
            ],
            GO: [
                MessageHandler(Filters.text, go),
                CommandHandler('new', cancel),
                CommandHandler('cancel', cancel)
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

	dp.add_handler(conv_handler)
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('help', help))
	dp.add_handler(CommandHandler('new', new))
	dp.add_handler(CommandHandler('folder', folder))
	dp.add_handler(CommandHandler('file', file))
	dp.add_handler(MessageHandler(Filters.text, echo))
	dp.add_handler(CommandHandler('username', get_username))
	dp.add_handler(CommandHandler('time', time))
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	print('Working...')
	main()
