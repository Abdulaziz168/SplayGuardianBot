async def handle_media(update, context):
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_id = user.id

    # Adminlar ro'yxatini guruhdan avtomatik olish
    chat_administrators = await context.bot.get_chat_administrators(chat_id)
    admin_ids = [admin.user.id for admin in chat_administrators]

    # Faqat oddiy user bo‘lsa — o‘chir
    if user_id not in admin_ids:
        await update.message.delete()
        await update.message.reply_text(
            f"⚠️ {user.mention_html()} rasm, video yoki fayl yuborish taqiqlangan!",
            parse_mode="HTML"
        )
