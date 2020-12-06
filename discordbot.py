from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

await bot.change_presence(activity=discord.Game(name="yukey いじめ"))


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
async def mac(ctx):
    await ctx.send(':hamburger:')

@bot.command()
async def kuramasu(ctx):
    await ctx.send('<@&742741011163250759>')

@bot.command()
async def ateam(ctx):
    await ctx.send('<@&754414375850344528>')

@bot.command()
async def bteam(ctx):
    await ctx.send('<@&754414423267082240>')

@bot.command()
async def boss(ctx):
    await ctx.send('<@&742740658694914088>')

@bot.command()
async def anarisuto(ctx):
    await ctx.send('<@&784767086752169984>')

 
@bot.command(name='server')
async def fetchServerInfo(context):
	guild = context.guild
	
	await context.send(f'server Name: {guild.name}')
	await context.send(f'server Size: {len(guild.members)}')
	await context.send(f'Server Name: {guild.owner.display_name}') 
	


    
bot.run(token)
