# Arkham Cultist

Discord bot forked from _Cotorrra_. Fetches Arkham Horror LCG cards, decks and images from [arkham.build](https://arkham.build) and [arkhamdb](https://arkhamdb.com).

## How to run

First you'll need to set up a .env file with the following properties:

- DISCORD_TOKEN : Your Discord Application Bot Token (not the OAuth Client Secret)
- BOT_LANGUAGE: The language of the Discord Interactions (it should be one that has a file in /data)

### Docker

Docker files come ready if you want to deploy it containerized. Simply running **rebuild.sh** should work.

### Manually run python

1. Install its requirements:
   `pip install -r requirements.txt`
2. Run:
   `python bot.py`

## Custom emojis

This bot shows cards as Discord embeds, which support custom server emojis in the text. The `config.py` file comes preconfigured with these emojis used as icons. If the bot is used in a DM via an App user installation, the default icons will work. If the bot tries to use these emojis in any other server where the user who uploaded the icons is not in, the emojis will just show as text. You can upload your custom emojis to your own private server (free tier will fit all the icons) and replace the current ones in the config.py file. On a Discord message with custom emojis right-click > "Copy Text" gets you the correct syntax with its whole unique id.
