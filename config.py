import logging
import os

from dotenv import load_dotenv

log_format = "[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s"

# The Bot secret TOKEN
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Base link to arkhamdb. It varies from language to language
ARKHAM_DB = os.getenv("ARKHAMDB")
logging.info(f"ArkhamDB url: {ARKHAM_DB}")

ARKHAM_BUILD = "https://arkham.build"
ARKHAM_BUILD_API = "https://api.arkham.build"

# You can choose to es/en: Check Sr-Cotorre Data to check all languages that are available!
LANG = os.getenv("BOT_LANGUAGE")
logging.info(f"Language: {LANG}")

# You can change where the data comes from
DATA_API = os.getenv("DATA_API")
logging.info(f"Cotorre Data: {DATA_API}")

SLOT_CUSTOM_EMOJIS = {
    "Accessory": "<:slot_accessory:1542451465371516928>",
    "Ally": "<:slot_ally:1542451482031431720>",
    "Arcane": "<:slot_arcane:1542451498661970010>",
    "Arcane x2": "<:slot_2arcane:1542451431615762492>",
    "Body": "<:slot_body:1542453694107357206>",
    "Hand": "<:slot_hand:1542453716580569128>",
    "Hand x2": "<:slot_2hand:1542451448707813418>",
    "Tarot": "<:slot_tarot:1542453765058072617>",
}

TEXT_FORMAT = {
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
    "[mythos]": "<:cultist:1542200315825356911>",
    "[health]": "<:health:1542454318773305415>",
    "[sanity]": "<:sanity:1542454338147057675>",
    "[per_investigator]": "<:per_invest:1542454703949094973>",
    "[doom]": "<:doom:1542454035574034492>",
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
    "[[": "***",
    "]]": "***",
    "<cite>": "\n— ",
    "</cite>": "",
}
