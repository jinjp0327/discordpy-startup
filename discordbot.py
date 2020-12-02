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
    
@client.event
async def on_message(message):
    
    if message.author.bot:
        return
    
    if message.content == 'kurumin':
        await message.channel.send(':banana:')

    if message.content == 'yukey':
        await message.channel.send(':toilet:')

    if message.content == 'yuu':
        await message.channel.send(':poop:')

    if message.content == 'noki':
        await message.channel.send(':cupid: ')

    if message.content == 'jin':
        await message.channel.send(':sunglasses: ')

    if message.content == 'jincome':
        await message.channel.send('@566444794734444555早く来いよ')

    if message.content == 'nokicome':
        await message.channel.send('@579665819445887006早く来いよ')

    if message.content == 'yukeycome':
        await message.channel.send('@435358191971336204早く来いよ')

    if message.content == 'yuucome':
        await message.channel.send('@588781728257015821早く来いよ')

    if message.content == 'kurumincome':
        await message.channel.send('@701027198328504360早く来いよ')

    if message.content == '今日やる人いる？':
        await message.channel.send('一人でやっとけボッチ')

    if message.content == '誰かシージしませんか？':
        await message.channel.send('一人でやっとけボッチ')

    if message.content == '入ってもいいですか？':
        await message.channel.send('多分いいと思う')     
        
    if message.content == ':grinning: :left_facing_fist: ':
        await message.channel.send('死ね')    

    if message.content == ':banana:':
        await message.channel.send('変態！')  
        
    if message.content == 'はよこい':
        await message.channel.send('せかんでぇー')   

    if message.content == 'はやくー':
        await message.channel.send('せかんでぇー')  
        
    if message.content == '笑':
        await message.channel.send('なに笑ってんの？')

    if message.content == 'しね':
        await message.channel.send('どしたん？話きこか？^-^')

    if message.content == '死ね':
        await message.channel.send('どしたん？話きこか？^-^')

    if message.content == 'ふざけんなよ':
        await message.channel.send('どしたん？話きこか？^-^')   
        
    if message.content == 'ええ加減にしろ':
        await message.channel.send('どしたん？話きこか？^-^') 

    if message.content == 'かす':
        await message.channel.send('どしたん？話きこか？^-^') 

    if message.content == 'やめちまえシージ':
        await message.channel.send('どしたん？話きこか？^-^') 

    if message.content == 'おもんないねん':
        await message.channel.send('どしたん？話きこか？^-^') 

    if message.content == 'え':
        await message.channel.send('なんか文句あるんか？') 

    if message.content == 'e':
        await message.channel.send('なんか文句あるんか？') 

    if message.content == 'あ':
        await message.channel.send('なんか文句あるんか？')

    if message.content == 'a':
        await message.channel.send('なんか文句あるんか？')    


bot.run(token)
