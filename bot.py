from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import datetime

# Inserisci il tuo token di BotFather qui
TOKEN = "7378196063:AAFlELp_RYsPEPsbLasQBpweHZ_PbdurzgE"

# Dizionario di film per genere
film_by_genre = {
    "azione": [
        ("Mad Max: Fury Road (2015)", "https://upload.wikimedia.org/wikipedia/en/2/23/Mad_Max_Fury_Road.jpg"),
        ("John Wick (2014)", "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg"),
    ],
    "commedia": [
        ("Una notte da leoni (2009)", "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg"),
        ("Forrest Gump (1994)", "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg"),
    ],
    "fantasy": [
        ("Il Signore degli Anelli: La Compagnia dell'Anello (2001)", "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29.jpg"),
        ("Harry Potter e la Pietra Filosofale (2001)", "https://upload.wikimedia.org/wikipedia/en/6/6b/HP1poster.jpg"),
    ]
}

# Lista globale di film per il consiglio casuale
all_films = []
for films in film_by_genre.values():
    all_films.extend(films)

# Funzione /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Ciao! Sono Marino Consiglia Film.\n"
        "Usa i comandi:\n"
        "/consiglia ➔ Ricevi un film a caso\n"
        "/azione ➔ Film d'azione\n"
        "/commedia ➔ Film commedia\n"
        "/fantasy ➔ Film fantasy\n"
        "/filmoggi ➔ Ti consiglio il film del giorno!"
    )

# Funzione per /consiglia
async def consiglia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    film, poster = random.choice(all_films)
    await update.message.reply_photo(photo=poster, caption=f"🎞 Consiglio casuale:\n{film}")

# Funzione per /azione
async def azione(update: Update, context: ContextTypes.DEFAULT_TYPE):
    film, poster = random.choice(film_by_genre["azione"])
    await update.message.reply_photo(photo=poster, caption=f"🔥 Film d'azione:\n{film}")

# Funzione per /commedia
async def commedia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    film, poster = random.choice(film_by_genre["commedia"])
    await update.message.reply_photo(photo=poster, caption=f"😂 Film commedia:\n{film}")

# Funzione per /fantasy
async def fantasy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    film, poster = random.choice(film_by_genre["fantasy"])
    await update.message.reply_photo(photo=poster, caption=f"🧙‍♂️ Film fantasy:\n{film}")

# Funzione per /filmoggi
async def film_oggi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.date.today()
    index = today.toordinal() % len(all_films)
    film, poster = all_films[index]
    await update.message.reply_photo(photo=poster, caption=f"📅 Film del giorno ({today.strftime('%d/%m/%Y')}):\n{film}")

# Funzione principale
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("consiglia", consiglia))
    app.add_handler(CommandHandler("azione", azione))
    app.add_handler(CommandHandler("commedia", commedia))
    app.add_handler(CommandHandler("fantasy", fantasy))
    app.add_handler(CommandHandler("filmoggi", film_oggi))

    app.run_polling()

if __name__ == "__main__":
    main()

