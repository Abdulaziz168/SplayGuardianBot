import re
from config import ADMINS, SETTINGS
import json
from datetime import datetime

def is_spam(text):
    return bool(re.search(r"(http[s]?://|t\.me/|@\w+|\.com|\.uz)", text.lower()))

def log_violation(user, text):
    if SETTINGS.get("log_enabled", False):
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] {user}: {text}\n")

def update_stats(user_id):
    stats = {}
    try:
        with open("stats.json", "r") as f:
            stats = json.load(f)
    except:
        pass
    stats[str(user_id)] = stats.get(str(user_id), 0) + 1
    with open("stats.json", "w") as f:
        json.dump(stats, f)

async def handle_message(update, context):
    text = update.message.text
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_id = user.id

    update_stats(user_id)

    if is_spam(text) and user_id not in ADMINS and SETTINGS.get("link_filter", True):
        await update.message.delete()
        log_violation(user.username or user.full_name, text)
        await context.bot.send_message(chat_id, f"⚠️ {user.mention_html()} reklamaga ruxsat yo‘q!", parse_mode="HTML")
