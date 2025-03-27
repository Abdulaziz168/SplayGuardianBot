from telegram.ext import CommandHandler, MessageHandler, filters, CallbackQueryHandler, ChatMemberHandler
from .message_filter import handle_message
from .admin_commands import start, ban_user, mute_user, panel, button_callback
from .new_member import handle_new_member
from .media_filter import handle_media

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ban", ban_user))
    app.add_handler(CommandHandler("mute", mute_user))
    app.add_handler(CommandHandler("panel", panel))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(ChatMemberHandler(handle_new_member, ChatMemberHandler.CHAT_MEMBER))

    # ✅ Media filtrlar — to‘g‘rilangan
    app.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO | filters.ATTACHMENT, handle_media))

    # ✅ Matnli xabarlar uchun
    app.add_handler(MessageHandler(filters.TEXT, handle_message))