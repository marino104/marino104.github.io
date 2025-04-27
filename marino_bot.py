import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Inserisci il tuo token ottenuto da BotFather
TOKEN = "7378196063:AAFlELp_RYsPEPsbLasQBpweHZ_PbdurzgE"

# Dizionario dei film organizzati per genere
film_catalogo = {
    "azione": [
        {
            "titolo": "Mad Max: Fury Road",
            "anno": 2015,
            "descrizione": "Un'epica corsa attraverso un deserto post-apocalittico.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg"
        },
        {
            "titolo": "John Wick",
            "anno": 2014,
            "descrizione": "Un ex assassino torna in azione per vendetta.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg"
        }
    ],
    "commedia": [
        {
            "titolo": "The Grand Budapest Hotel",
            "anno": 2014,
            "descrizione": "Le avventure di un concierge in un lussuoso hotel europeo.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg"
        },
        {
            "titolo": "Superbad",
            "anno": 2007,
            "descrizione": "Due amici cercano di divertirsi prima del diploma.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/8/8b/Superbad_Poster.png"
        }
    ],
    "drammatico": [
        {
            "titolo": "The Shawshank Redemption",
            "anno": 1994,
            "descrizione": "La storia di un'amicizia nata in prigione.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg"
        },
        {
            "titolo": "Forrest Gump",
            "anno": 1994,
            "descrizione": "La straordinaria vita di un uomo semplice.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg"
        }
    ],
    "fantasy": [
        {
            "titolo": "Il Signore degli Anelli: La Compagnia dell'Anello",
            "anno": 2001,
            "descrizione": "Un gruppo parte per distruggere un potente anello.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29.jpg"
        },
        {
            "titolo": "Harry Potter e la Pietra Filosofale",
            "anno": 2001,
            "descrizione": "Un ragazzo scopre di essere un mago.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_Poster.jpg"
        }
    ],
    "animazione": [
        {
            "titolo": "Coco",
            "anno": 2017,
            "descrizione": "Un ragazzo viaggia nel mondo dei morti per scoprire le sue radici.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg"
        },
        {
            "titolo": "Inside Out",
            "anno": 2015,
            "descrizione": "Un viaggio nelle emozioni di una ragazza.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg"
        }
    ]
}

# Funzione per il comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messaggio = (
        "🎬 Ciao! Sono Marino, il tuo consigliere cinematografico.\n"
        "Puoi chiedermi un consiglio con i seguenti comandi:\n"
        "/consiglia - Un film casuale\n"
        "/azione - Film d'azione\n"
        "/commedia - Film commedia\n"
        "/drammatico - Film drammatici\n"
        "/fantasy - Film fantasy\n"
        "/animazione - Film d'animazione\n"
        "/film_del_giorno - Il film del giorno con poster\n"
    )
    await update.message.reply_text(messaggio)

# Funzione per consigliare un film casuale
async def consiglia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tutti_i_film = sum(film_catalogo.values(), [])
    film = random.choice(tutti_i_film)
    messaggio = f"🎞 {film['titolo']} ({film['anno']})\n{film['descrizione']}"
    await update.message.reply_photo(photo=film['poster'], caption=messaggio)

# Funzione per consigliare un film per genere
async def consiglia_per_genere(update: Update, context: ContextTypes.DEFAULT_TYPE):
    comando = update.message.text[1:]  # Rimuove la barra iniziale
    genere = comando.lower()
    if genere in film_catalogo:
        film = random.choice(film_catalogo[genere])
        messaggio = f"🎞 {film['titolo']} ({film['anno']})\n{film['descrizione']}"
        await update.message.reply_photo(photo=film['poster'], caption=messaggio)
    else:
        await update.message.reply_text("❌ Genere non riconosciuto.")

# Funzione per il film del giorno
async def film_del_giorno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tutti_i_film = sum(film_catalogo.values(), [])
    film = random.choice(tutti_i_film)
    messaggio = f"🎬 *Film del Giorno*\n🎞 {film['titolo']} ({film['anno']})\n{film['descrizione']}"
    await update.message.reply_photo(photo=film['poster'], caption=messaggio, parse_mode='Markdown')

# Funzione principale
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("consiglia", consiglia))
    app.add_handler(CommandHandler("azione", consiglia_per_genere))
    app.add_handler(CommandHandler("commedia", consiglia_per_genere))
    app.add_handler(CommandHandler("drammatico", consiglia_per_genere))
    app.add_handler(CommandHandler("fantasy", consiglia_per_genere))
    app.add_handler(CommandHandler("animazione", consiglia_per_genere))
    app.add_handler(CommandHandler("film_del_giorno", film_del_giorno))

    print("🤖 Marino Consiglia Film è attivo!")
    app.run_polling()

if __name__ == "__main__":
    main()
