import logging
from interactions import Embed

async def handle_command_error(ctx, exc: Exception, bot_owner):
    logging.error(f"Encountered an error running a command: {type(exc).__name__} | {exc}", exc_info=exc)
    embed = Embed(title="Oops!", description=f"The Cultist drew an Auto-fail, try again later or report to {bot_owner}", color=0xc43535)
    await ctx.send(embeds=embed, ephemeral=True)