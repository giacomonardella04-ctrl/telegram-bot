import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Configurazione del logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Token del bot fornito da BotFather
TOKEN = "9247010842:AAHF5PsVTYrWYpzrvUIjmq4rC6-H-s4J2yY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Ciao! Sono Media Gate.\n\n"
        "Aggiungimi come amministratore a un supergruppo: ogni nuovo membro "
        "dovrà inviare 10 foto o video entro 1 ora, altrimenti verrà bannato.\n"
        "Dopo la verifica serviranno altri 10 media ogni 24 ore.\n"
        "Alla scadenza chi non ha raggiunto la quota riceve un'ammonizione con altre 2 ore di tempo, poi viene bannato.\n\n"
        "Nel gruppo puoi usare /me, /stato e /help."
    )
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Media Gate — comandi\n\n"
        "/stato — statistiche del gruppo\n"
        "/me — la tua quota e il tempo rimasto\n"
        "/id — mostra l'ID della chat corrente\n"
        "/pending — membri con quota aperta (admin)\n"
        "/verifica <id|@username> — verifica manuale (admin)\n"
        "/perdona <id|@username> — rimuove il ban e verifica (admin)\n"
        "/unbanall — rimuove il ban di tutti (proprietario)\n"
        "/tempo <ore> — ore per la verifica iniziale (admin)\n"
        "/help — questo messaggio\n\n"
        "Alla scadenza della quota chi non ha inviato i media riceve un'ammonizione con 2 ore di proroga, poi viene bannato.\n"
        "Per i comandi admin puoi anche rispondere al messaggio dell'utente."
    )
    await update.message.reply_text(text)

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"ID di questa chat: {chat_id}")

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("id", id_command))

    print("Il bot è stato avviato...")
    application.run_polling()

if __name__ == '__main__':
    main()
