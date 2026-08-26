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

# Advanced: If you want to change the emojis from the bot
# [tag] -> <emoji:code>
# you can get this code with /:emoji: in Discord.
TEXT_FORMAT = {
    "[free]": "<:free_trigger:1542282589358923777>",
    "[fast]": "<:free_trigger:1542282589358923777>",
    "[elder_sign]": "<:elder_sign_token:1542282529632030771>",
    "[wild]": "<:wild:1542282587983183902>",
    "[willpower]": "<:willpower:1542282568639058030>",
    "[combat]": "<:combat:1542282700390531182>",
    "[intellect]": "<:intellect:1542282584816492695>",
    "[agility]": "<:agility:1542282570262384753>",
    "[action]": "<:action:1542282590671732816>",
    "[reaction]": "<:reaction:1542282591841816646>",
    "[bless]": "<:bless_token:1542282534501486662>",
    "[curse]": "<:curse_token:1542282532727296030>",
    "[skull]": "<:skull_token:1542282547533447309>",
    "[cultist]": "<:cultist_token:1542282540637753404>",
    "[tablet]": "<:tablet_token:1542282696300961972>",
    "[elder_thing]": "<:elder_thing_token:1542282539241185481>",
    "[auto_fail]": "<:autofail_token:1542282537894813776>",
    "[frost]": "<:frost_token:1542282536808353902>",
    "[mystic]": "<:mystic:1542282594966577262>",
    "[seeker]": "<:seeker:1542282702580088914>",
    "[guardian]": "<:guardian:1542282605989331095>",
    "[rogue]": "<:rogue:1542282596489232424>",
    "[survivor]": "<:survivor:1542282593175736362>",
    "[neutral]": "<:neutral:1542282550117007420>",
    "[mythos]": "<:cultist:1542282552440660119>",
    "[health]": "<:health:1542282528323276911>",
    "[sanity]": "<:sanity:1542282526553542706>",
    "[per_investigator]": "<:per_invest:1542282566420135966>",
    "[doom]": "<:doom:1542282698754891786>",
    "[taboo]": "<:taboo:1542282555695440012>",
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
