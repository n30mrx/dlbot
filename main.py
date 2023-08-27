import telebot, os, re
bot = telebot.TeleBot("TOKEN")

# download function
def downvid(message):
    ytregx = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
    if re.match(ytregx,message.text):
        a = bot.send_message(message.chat.id,"Downloading")
        print(a)
        os.system(f"yt-dlp {message.text} --format 'mp4[height<=480]' --output video{message.from_user.id}{message.id}.mp4>logs/log{message.from_user.id}.log")
        # bot.send_message(message.chat.id,"Sending video")
        bot.edit_message_text("Sending video", message.chat.id,a.id)
        try:
            bot.send_video(message.chat.id,video=open(f'video{message.from_user.id}{message.id}.mp4', 'rb'), supports_streaming=True)
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id,f"An error occured\nVideo might be too large\nError info: {e}")
    else:
        bot.send_message(message.chat.id,"Please send a vaild youtube link")

@bot.message_handler(commands=["start"])
def startmsg(message):
    bot.send_message(message.chat.id,"Hi! sned me a youtube link to download the video")

@bot.message_handler()
def downmsg(message):
    downvid(message=message)


bot.infinity_polling()