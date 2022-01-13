from importlib.metadata import entry_points
from telegram import Update
from telegram.ext import (Updater, 
                            CommandHandler,                             
                            ConversationHandler,
                            CallbackQueryHandler,    
                            Filters, 
                            MessageHandler,
                            PicklePersistence, dispatcher)
from bot.src.registration import Registration
import dotenv
import os
import logging


dotenv.load_dotenv()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


registration = Registration()
def main():
    updater = Updater(token=os.getenv("BOT_TOKEN"))
    dispatcher = updater.dispatcher
    
    main_conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', registration.start)
        ],
        
        states = {
            
        },
        fallbacks=[
            CommandHandler('start', menu.display)],
        per_chat=False,
        name="main_conversation"
    )
    

    updater.dispatcher.add_handler(main_conversation)

    updater.start_polling()
    updater.idle()