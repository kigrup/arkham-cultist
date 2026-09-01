# Arkham Cultist

Discord bot forked from _Cotorrra_. Fetches Arkham Horror LCG cards, decks and images from [arkham.build](https://arkham.build).

## How to run

First you'll need to set up a .env file with the following properties:

- DISCORD_TOKEN : **Required**. Your Discord Application Bot Token (not the OAuth Client Secret).
- API_LANGUAGE: **Optional**. The language of the arkham.build API, so all the cards and metadata retrieved. Will default to `en` if empty or invalid value is provided.
   - Valid values: `en`, `es`, `pl`, `de`, `fr`, `ko`, `ru`, `it`, `zh`.
- BOT_LANGUAGE: **Optional**.  The language of the bot labels and descriptions. Will default to `en` if empty or invalid value is provided.
   - Valid values: `en`, `es`. (If you need the bot translated to any other language please open an issue)
- CUSTOM_EMOJIS: **Optional**. JSON with custom emojis override per server. Any emoji not provided for any server will use the default ones (which only work in DMs).
   - Example syntax: `{"225349059689447425": {"Hand x2": ":open_hands:", "[action]": ":arrow_right:"}}`

### Docker

Docker files come ready if you want to deploy it containerized. Simply running `rebuild.sh` should work.

### Or manually run python

1. Install its requirements:
   `pip install -r requirements.txt`
2. Run:
   `python bot.py`

## Custom emojis

This bot shows cards as Discord embeds, which support custom server emojis in the text. The `config.py` file comes preconfigured with these emojis used as icons. If the bot is used in a DM via an App user installation, the default icons will work. If the bot tries to use these emojis in any other server where the user who uploaded the icons is not in, the emojis will just show as text. You can upload your custom emojis to your own private server (free tier will fit all the icons) and override the current ones in the .env file. On a Discord message with custom emojis right-click > "Copy Text" gets you the correct syntax with its whole unique id.
