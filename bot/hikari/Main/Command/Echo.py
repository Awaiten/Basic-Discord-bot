import hikari
import lightbulb

bot = lightbulb.BotApp(
    os.environ["Token"],
    default_enabled_guilds=int(os.environ["Default_Guild_ID"]),
    intents=hikari.Intents.ALL,
)


@bot.command()
@lightbulb.option("say", "...")
@lightbulb.command("...", "...")
@lightbulb.implements(...) #This wil most likey be lightbulb.Slashcommand or lightbulb.Prefixcommand
async def embed_command(ctx: lightbulb.Context) -> None:
  embed = hikari.Embed(title=(ctx.options.Say), colour="#...")
  await ctx.respond(embed=embed) #a simple embed command :)
  
