import logging
import sys

from src.core.logger import init_logger
init_logger()

from config import TOKEN

from dotenv import load_dotenv
from interactions import (
    Client,
    Intents,
    SlashContext,
    check,
    listen,
    slash_command,
)
from sorcery import dict_of

from src.core.translator import locale as _
from src.response.response import (
    look_for_card_back,
    look_for_customizable_card,
    look_for_deck,
    look_for_framework,
    look_for_list_of_cards,
    look_for_mythos_card,
    look_for_player_card,
    look_for_random_player_card,
    look_for_tarot,
    look_for_upgrades,
    look_for_whom,
)
from src.response.slash_options import (
    customizable_card_slash_options,
    deck_slash_options,
    general_card_slash_options,
    player_card_slash_options,
    tarot_slash_options,
    timing_slash_options,
)
from src.core.stats import (
    init_db,
    increment_command
)
from src.core.errors import handle_command_error

init_db()
bot = Client(token=TOKEN, intents=Intents.DEFAULT)

@listen()
async def on_ready():
    logging.info("Bot is ready.")
    logging.info(f"{bot.owner} is the owner of the bot")


@slash_command(
    name="ah",
    description=_("ah_description"),
    options=player_card_slash_options(name_req=True, allow_image_only=True),  # type: ignore
)
async def player_card(
    ctx: SlashContext,
    name,
    level="",
    image_only=False,
    faction="",
    extras="",
    subtitle="",
    cycle="",
    traits="",
):
    """Handles the /ah slash command, this command returns' player cards."""
    try:
        query = dict_of(name, level, faction, extras, subtitle, cycle, traits)
        increment_command(ctx.guild_id, ctx.author_id, "ah", query=query)
        embed, hidden = look_for_player_card(query, str(ctx.guild_id), image_only=image_only)
        await ctx.send(embeds=embed, ephemeral=hidden)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahdeck",
    description=_("ahDeck_description"),
    options=deck_slash_options(),  # type: ignore
)
async def deck(ctx: SlashContext, code, deck_type=""):
    """Handles the /ahDeck command, it returns a deck from ArkhamDB."""
    try:
        await ctx.defer()
        increment_command(ctx.guild_id, ctx.author_id, "ahdeck", code=code, deck_type=deck_type)
        embed, _ = look_for_deck(code, deck_type, str(ctx.guild_id))
        await ctx.send(embeds=embed)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahup",
    description=_("ahUp_description"),
    options=deck_slash_options(),  # type: ignore
)
async def upgrade(ctx: SlashContext, code, deck_type=""):
    """Handles the /ahUp command, it returns the upgrades of a deck."""
    try:
        await ctx.defer()
        increment_command(ctx.guild_id, ctx.author_id, "ahup", code=code, deck_type=deck_type)
        embed, _ = look_for_upgrades(code, deck_type, str(ctx.guild_id))
        await ctx.send(embeds=embed)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahe",
    description=_("ahe_description"),
    options=general_card_slash_options(),  # type: ignore
)
async def encounter(
    ctx: SlashContext, name="", card_type="", image_only=False, subtitle="", cycle="", traits=""
):
    """Handle the /ahe command, it returns encounter cards."""
    try:
        query = dict_of(name, card_type, subtitle, cycle, traits)
        increment_command(ctx.guild_id, ctx.author_id, "ahe", query=query)
        embed, hidden = look_for_mythos_card(query, str(ctx.guild_id), image_only=image_only)
        await ctx.send(embeds=embed, ephemeral=hidden)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahb",
    description=_("ahb_description"),
    options=general_card_slash_options(),  # type: ignore
)
async def back(
    ctx: SlashContext, name="", card_type="", image_only=False, subtitle="", cycle="", traits=""
):
    """Handles the /ahb command, it returns card backs."""
    try:
        query = dict_of(name, card_type, subtitle, cycle, traits)
        increment_command(ctx.guild_id, ctx.author_id, "ahb", query=query)
        embed, hidden = look_for_card_back(query, str(ctx.guild_id), image_only=image_only)
        await ctx.send(embeds=embed, ephemeral=hidden)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahtarot",
    description=_("ahTarot_description"),
    options=tarot_slash_options(),  # type: ignore
)
async def tarot(ctx: SlashContext, name=""):
    """Handles the /ahTarot command, it returns tarot cards."""
    try:
        increment_command(ctx.guild_id, ctx.author_id, "ahtarot", name=name)
        embed, hidden = look_for_tarot(name, str(ctx.guild_id))
        await ctx.send(embeds=embed, ephemeral=hidden)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahtiming",
    description=_("ahTiming_description"),
    options=timing_slash_options(),  # type: ignore
)
async def game_timing(ctx: SlashContext, timing):
    """Handles the /ahTiming command, it returns game timings."""
    try:
        increment_command(ctx.guild_id, ctx.author_id, "ahtiming", timing=timing)
        embed, _ = look_for_framework(timing, str(ctx.guild_id))
        await ctx.send(embeds=embed)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahlist",
    description=_("ahList_description"),
    options=player_card_slash_options(),  # type: ignore
)
async def list_cards(
    ctx: SlashContext,
    name="",
    level="",
    faction="",
    extras="",
    subtitle="",
    cycle="",
    traits="",
):
    """Handles the /ahList command, it lists playercards."""
    try:
        query = dict_of(name, level, faction, extras, subtitle, cycle, traits)
        increment_command(ctx.guild_id, ctx.author_id, "ahlist", query=query)
        embed, hidden = look_for_list_of_cards(query, str(ctx.guild_id))
        await ctx.send(embeds=embed, ephemeral=hidden)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahrandom",
    description=_("ahRandom_description"),
    options=player_card_slash_options(allow_image_only=True),  # type: ignore
)
async def random(
    ctx: SlashContext,
    name="",
    level="",
    image_only=False,
    faction="",
    extras="",
    subtitle="",
    cycle="",
    traits="",
):
    """Handles the /ahRandom command, it returns a random card."""
    try:
        query = dict_of(name, level, faction, extras, subtitle, cycle, traits)
        increment_command(ctx.guild_id, ctx.author_id, "ahrandom", query=query)
        embed, hidden = look_for_random_player_card(query, str(ctx.guild_id), image_only=image_only)
        await ctx.send(embeds=embed, ephemeral=hidden)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahwho",
    description=_("ahWho_description"),
    options=player_card_slash_options(name_req=True),  # type: ignore
)
async def ah_who(
    ctx: SlashContext,
    name,
    level="",
    faction="",
    extras="",
    subtitle="",
    cycle="",
    traits="",
):
    """Handles the /ah slash command, this command returns' player cards."""
    try:
        query = dict_of(name, level, faction, extras, subtitle, cycle, traits)
        increment_command(ctx.guild_id, ctx.author_id, "ahwho", query=query)
        embed, hidden = look_for_whom(query, str(ctx.guild_id))
        await ctx.send(embeds=embed, ephemeral=hidden)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

@slash_command(
    name="ahcustomizable",
    description=_("ahCustomizable_description"),
    options=customizable_card_slash_options(),  # type: ignore
)
async def costumizable_card(ctx: SlashContext, name=""):
    """Handles the /ahahCustomizable command. Returns the upgrade sheet of a card."""
    try:
        query = {"name": name}
        increment_command(ctx.guild_id, ctx.author_id, "ahcustomizable", query=query)
        embed, hidden = look_for_customizable_card(query, str(ctx.guild_id))
        await ctx.send(embeds=embed, ephemeral=hidden)
    except Exception as exc:
        await handle_command_error(ctx, exc, bot.owner)

bot.start()
