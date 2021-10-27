...

özel_prefix = {}
varsayılan_prefix = ['!'] #siz değiştirebilirsiniz

async def belirle_prefix(bot, message):
    guild = message.guild
    #sadece prefixin sunucuda değişmesini sağlar bu kısım
    if guild:
        return özel_prefix.get(guild.id, varsayılan_prefix)
    else:
        return varsayılan_prefix

bot = commands.Bot(command_prefix = belirle_prefix, ...)
bot.run()

@commands.command()
@commands.guild_only()
async def setprefix(self, ctx, *, prefix=""):

    özel_prefix[ctx.guild.id] = prefix.split() or varsayılan_prefix
    await ctx.send("Varsayılan Prefix Değiştirildi!")
