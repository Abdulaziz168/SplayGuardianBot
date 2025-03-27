async def handle_media(update, context):
    user = update.message.from_user
    await update.message.delete()
    await update.message.reply_text(
        f"⚠️ {user.mention_html()} rasm, video yoki fayl yuborish taqiqlangan!",
        parse_mode="HTML"
    )
