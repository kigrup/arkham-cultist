# Arkham Cultist

Discord bot forked from _Cotorrra_. Fetches Arkham Horror LCG cards, decks and images from [arkham.build](https://arkham.build) and [arkhamdb](https://arkhamdb.com).

## How to run

First you'll need to set up a .env file with the following properties:

- DISCORD_TOKEN : Your Discord Application Bot Token (not the OAuth Client Secret)
- ARKHAMDB: The link to arkhamDB where it should get the cards from. (i.e. https://es.arkhamdb.com or https://arkhamdb.com)
- BOT_LANGUAGE: The language of the Discord Interactions (it should be one that has a file in /data)

### Docker

Docker files come ready if you want to deploy it containerized. Simply running **rebuild.sh** should work.

### Manually run python

1. Install its requirements:
   `pip install -r requirements.txt`
2. Run:
   `python bot.py`
