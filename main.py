import os
import telebot

# Get the environment variables set in Railway
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Set this in Railway Environment
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Set the target chat ID in Railway Environment

bot = telebot.TeleBot(TOKEN)

def send_signal(signal_text):
    bot.send_message(CHAT_ID, signal_text)

# Example: When this script runs, it sends a signal message
send_signal("📈 BUY Signal: RELIANCE above ₹2900")
