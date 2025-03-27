from telegram.ext import ApplicationBuilder
from modules.handlers import register_handlers
from config import BOT_TOKEN

# Asosiy ilovani yaratish
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handlarni ro‘yxatdan o‘tkazish
register_handlers(app)

print("SplayGuardianBot ishga tushdi...")

# Botni ishga tushirish
app.run_polling()
