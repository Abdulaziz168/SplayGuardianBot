from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ChatPermissions
from telegram.ext import ContextTypes
from config import SETTINGS
import json
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("SplayGuardianBot ishga tushdi!")

async def ban_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user_to_ban = update.message.reply_to_message.from_user
        await context.bot.ban_chat_member(update.effective_chat.id, user_to_ban.id)
        await update.message.reply_text(f"{user_to_ban.mention_html()} bloklandi.", parse_mode="HTML")

async def mute_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user_to_mute = update.message.reply_to_message.from_user
        permissions = ChatPermissions(can_send_messages=False)
        await context.bot.restrict_chat_member(update.effective_chat.id, user_to_mute.id, permissions=permissions)
        await update.message.reply_text(f"{user_to_mute.mention_html()} o‘chirildi.", parse_mode="HTML")

async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Statistika", callback_data='stats')],
        [InlineKeyboardButton("Filtr sozlamalari", callback_data='settings')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Admin Panel:", reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "stats":
        stats_text = "Statistika:\n"
        if os.path.exists("stats.json"):
            with open("stats.json", "r") as f:
                stats = json.load(f)
                for uid, count in stats.items():
                    stats_text += f"👤 {uid}: {count} ta xabar\n"
        else:
            stats_text += "Statistika mavjud emas."
        await query.edit_message_text(stats_text)

    elif query.data == "settings":
        settings_text = "Aktiv filtrlar:\n"
        for key, value in SETTINGS.items():
            status = "✅" if value else "❌"
            settings_text += f"{status} {key}\n"
        await query.edit_message_text(settings_text)
