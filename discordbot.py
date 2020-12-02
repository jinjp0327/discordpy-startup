from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def jin(ctx):
    await ctx.send(':sunglasses: ') 
    
    
@bot.command()
async def yukey(ctx):
    await ctx.send(':toilet: ') 
    
    
@bot.command()
async def yuu(ctx):
    await ctx.send(':poop: ') 
    
    
@bot.command()
async def noki(ctx):
    await ctx.send(':cupid: ')   
    
    
@bot.command()
async def gyu(ctx):
    await ctx.send(':fingers_crossed:  ')     
    

@bot.command()
async def jincome(ctx):
    await ctx.send('@566444794734444555早く来いよ ') 
    
    
@bot.command()
async def yukeycome(ctx):
    await ctx.send('@579665819445887006早く来いよ ')     
            
    
@bot.command()
async def yuucome(ctx):
    await ctx.send('@588781728257015821早く来いよ ')     
    
    
@bot.command()
async def nokicome(ctx):
    await ctx.send('@579665819445887006早く来いよ ')    
    
@bot.command()
async def gyucome(ctx):
    await ctx.send('@605025536867303434早く来いよ ') 
    
    
if not discord.opus.is_loaded():
    discord.opus.load_opus("heroku-buildpack-libopus")

@bot.command(aliases=["connect","summon"]) #connectやsummonでも呼び出せる
async def join(ctx):
    """Botをボイスチャンネルに入室させます。"""
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

    channel = voice_state.channel

    await channel.connect()
    print("connected to:",channel.name)


@bot.command(aliases=["disconnect","bye"])
async def leave(ctx):
    """Botをボイスチャンネルから切断します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    await voice_client.disconnect()
    await ctx.send("ボイスチャンネルから切断しました。")


@bot.command()
async def play(ctx):
    """指定された音声ファイルを流します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    if not ctx.message.attachments:
        await ctx.send("ファイルが添付されていません。")
        return

    await ctx.message.attachments[0].save("tmp.mp3")

    ffmpeg_audio_source = discord.FFmpegPCMAudio("tmp.mp3")
    voice_client.play(ffmpeg_audio_source)

    await ctx.send("再生しました。")    
    
   
    
    
    
    
    
    
bot.run(token)
