import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ----------------- BOT CONFIG -----------------
TOKEN = "8336764812:AAHHNa4XAaU72A_TtJORHsPaMaElTOpQlnQ"  # Replace with your token from @BotFather

# Map each cooking category to a local video file or a direct video URL.
VIDEO_CATEGORIES = {
    "P0RN": "videos/P0RN 1.mp4",
    "P0RN": "videos/P0RN 2.mp4",
    "P0RN": "videos/P0RN 3.mp4",
}

# ----------------- LOGGING -----------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ----------------- HANDLERS -----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /start command: sends a welcome message and shows category buttons.
    """
    keyboard = [
        [InlineKeyboardButton(category, callback_data=category)]
        for category in VIDEO_CATEGORIES.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🍳 Welcome to the Cooking Bot!\n"
        "Choose a category to get a recipe video:",
        reply_markup=reply_markup,
    )

async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles button clicks and sends the appropriate video.
    """
    query = update.callback_query
    await query.answer()
    category = query.data
    video_path = VIDEO_CATEGORIES[category]

    # To send from a URL, you can simply pass the URL string instead of opening a file.
    await query.message.reply_video(video=open(video_path, "rb"))

# ----------------- MAIN ENTRY -----------------
def main():
    # Build the application and register handlers.
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(send_video))

    print("✅ Hotvid bot is running… Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
