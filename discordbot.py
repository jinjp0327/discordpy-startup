import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzcwMjYzNjMyMjgxNjAwMDEw.X5bB6A.b1LuBg_pi56pryMhDoatPYAWR3U'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

	
client.run(TOKEN)	
