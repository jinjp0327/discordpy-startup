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
    await ctx.send('<@566444794734444555>早く来いよ ') 
    
    
@bot.command()
async def yukeycome(ctx):
    await ctx.send('<@435358191971336204>早く来いよ ')     
            
    
@bot.command()
async def yuucome(ctx):
    await ctx.send('<@588781728257015821>早く来いよ ')     
    
    
@bot.command()
async def nokicome(ctx):
    await ctx.send('<@579665819445887006>早く来いよ ')    
    
@bot.command()
async def gyucome(ctx):
    await ctx.send('<@605025536867303434>早く来いよ ') 
    
@bot.command()
async def gyucome(ctx):
    await ctx.send(':hamburger:') 
        
    
    

    
    
bot.run(token)
