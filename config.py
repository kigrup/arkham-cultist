import logging
import os
import json

from dotenv import load_dotenv

log_format = "[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s"

# The Bot secret TOKEN
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN", "")
if (TOKEN == ""):
    logging.error("No DISCORD_TOKEN provided in .env")

ARKHAM_BUILD = "https://arkham.build"
ARKHAM_BUILD_API = "https://api.arkham.build/v1"
ARKHAM_BUILD_CDN = "https://cdn.arkham.build/optimized"

LANG = os.getenv("BOT_LANGUAGE", "en")
logging.info(f"BOT_LANGUAGE:{LANG}")

SLOT_CUSTOM_EMOJIS = {
    "None": {
        "Accessory": "<:slot_accessory:1542451465371516928>",
        "Ally": "<:slot_ally:1542451482031431720>",
        "Arcane": "<:slot_arcane:1542451498661970010>",
        "Arcane x2": "<:slot_2arcane:1542451431615762492>",
        "Body": "<:slot_body:1542453694107357206>",
        "Hand": "<:slot_hand:1542453716580569128>",
        "Hand x2": "<:slot_2hand:1542451448707813418>",
        "Tarot": "<:slot_tarot:1542453765058072617>",
    }
}

TEXT_FORMAT = {
    "None": {
        "[[": "***",
        "]]": "***",
        "[free]": "<:free_ah:1542183227333283880>",
        "[fast]": "<:free_ah:1542183227333283880>",
        "[elder_sign]": "<:elder_sign_token:1542454050661081138>",
        "[wild]": "<:wild:1542454175911383122>",
        "[willpower]": "<:skill_willpower:1542453879197667468>",
        "[combat]": "<:skill_combat:1542453836617093140>",
        "[intellect]": "<:skill_intellect:1542453860012925019>",
        "[agility]": "<:skill_agility:1542453823208034334>",
        "[action]": "<:action:1542183247092523109>",
        "[reaction]": "<:reaction:1542180792401133671>",
        "[bless]": "<:bless_token:1542233777563246663>",
        "[curse]": "<:curse_token:1542233761129824397>",
        "[skull]": "<:skull_token:1542455406532497408>",
        "[cultist]": "<:cultist_token:1542454021217058877>",
        "[tablet]": "<:tablet_token:1542455294271946752>",
        "[elder_thing]": "<:elder_thing_token:1542454083460538448>",
        "[auto_fail]": "<:autofail:1542453960349065246>",
        "[frost]": "<:frost_token:1542454100292280421>",
        "[mystic]": "<:mystic:1542179151870558208>",
        "[seeker]": "<:seeker:1542179183868911678>",
        "[guardian]": "<:guardian:1542179118668316692>",
        "[rogue]": "<:rogue:1542179168219832401>",
        "[survivor]": "<:survivor:1542179222691258408>",
        "[neutral]": "<:neutral:1542273761909415986>",
        "[mythos]": "<:mythos:1542851332094824518>",
        "[health]": "<:health:1542454318773305415>",
        "[sanity]": "<:sanity:1542454338147057675>",
        "[per_investigator]": "<:per_invest:1542454703949094973>",
        "[doom]": "<:doom:1542454035574034492>",
        "[clues]": "<:clue_token:1542453989436817478>",
        "[taboo]": "<:taboo:1542200378773348482>",
        "_____": "＿＿＿",
        "<br/>": "\n",
        "</b>": "**",
        "<b>": "**",
        "<em>": "_",
        "</em>": "_",
        "<i>": "_",
        "</i>": "_",
        "<u>": "__",
        "</u>": "__",
        "<cite>": "\n— ",
        "</cite>": "",
    }
}

def initialize_emojis():
    logging.info(f"Starting initialize_emojis")
    CUSTOM_EMOJIS = json.loads(os.getenv("CUSTOM_EMOJIS", "{}"))

    # first override default/DM emojis if "None" guild is present in .env
    # this allows changing default icons without modifying the config.py file
    if "None" in CUSTOM_EMOJIS:
        for tag in CUSTOM_EMOJIS["None"]:
            if tag in SLOT_CUSTOM_EMOJIS:
                SLOT_CUSTOM_EMOJIS[tag] = CUSTOM_EMOJIS["None"][tag]
            elif tag in TEXT_FORMAT:
                TEXT_FORMAT[tag] = CUSTOM_EMOJIS["None"][tag]

    # create all the empty guild_id dictionary in the the emoji dictionaries
    for guild_id in CUSTOM_EMOJIS:
        if guild_id != "None":
            SLOT_CUSTOM_EMOJIS[guild_id] = {}
            TEXT_FORMAT[guild_id] = {}

    # initialize the default icons for every guild dictionary
    for guild_id in CUSTOM_EMOJIS:
        if guild_id != "None":
            for tag in SLOT_CUSTOM_EMOJIS["None"]:
                SLOT_CUSTOM_EMOJIS[guild_id][tag] = SLOT_CUSTOM_EMOJIS["None"][tag]
            for tag in TEXT_FORMAT["None"]:
                TEXT_FORMAT[guild_id][tag] = TEXT_FORMAT["None"][tag]

    # override the guild specific emojis with the ones provided in the .env
    for guild_id in CUSTOM_EMOJIS:
        if guild_id != "None":
            for tag in CUSTOM_EMOJIS[guild_id]:
                if tag in SLOT_CUSTOM_EMOJIS[guild_id]:
                    SLOT_CUSTOM_EMOJIS[guild_id][tag] = CUSTOM_EMOJIS[guild_id][tag]
                elif tag in TEXT_FORMAT[guild_id]:
                    TEXT_FORMAT[guild_id][tag] = CUSTOM_EMOJIS[guild_id][tag]

try:
    initialize_emojis()
except Exception as exc:
    logging.error(f"Error initializing custom emojis in config.py!")
    logging.error(type(exc))
    logging.error(exc.args)
    logging.error(exc)