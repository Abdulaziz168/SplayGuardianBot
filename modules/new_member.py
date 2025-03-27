from telegram import Update
from telegram.ext import ContextTypes

async def handle_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.chat_member.new_chat_members:
        try:
            await context.bot.delete_message(chat_id=update.chat_member.chat.id, message_id=update.chat_member.message_id)
        except:
            pass  # Agar xabarni o‘chirib bo‘lmasa, e'tiborsiz qoldiramiz
