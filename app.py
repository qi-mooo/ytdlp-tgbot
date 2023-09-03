import asyncio
import yt_dlp
import os
from aiogram import Bot, Dispatcher, types

# 设置你的 Telegram bot token
BOT_TOKEN = os.getenv('BOT_TOKEN')
SAVE_DIR = "/Downloads"

# 初始化 bot 和 dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("你好！发送一个URL给我，我会帮你下载它。")

@dp.message_handler()
async def download_video(message: types.Message):
    url = message.text
    options = {
        'format': 'best',
        'outtmpl': f'{SAVE_DIR}/%(title)s.%(ext)s',  # 使用视频标题作为文件名
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    await message.reply("视频下载完成！")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
