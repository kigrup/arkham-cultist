import json
import logging
import requests

from config import ARKHAM_DB, ARKHAM_BUILD_API


def find_deck(code: float, deck_mode) -> dict:
    """Searchs a deck by code in the ArkhamDB API."""
    print(f"find_deck({code}, {deck_mode})")
    print(f"type(code) is float: {type(code) is float}")
    try:
        code = int(code)
        link = f"{ARKHAM_BUILD_API}/v1/public/share/{code}{"?type=decklist" if deck_mode == "decklist" else ""}"
        req = requests.get(link, timeout=8)
        if req.status_code != 200 and deck_mode:
            print(req.status_code)
            return {}
        elif req.status_code != 200:
            link = f"{ARKHAM_BUILD_API}/v1/public/share/{code}?type=decklist"
            req = requests.get(link, timeout=8)
            if req.status_code != 200:
                print(req.status_code)
                return {}

        logging.info(f"Gotten Request: {req.json()}")
        return req.json()
    except json.decoder.JSONDecodeError:
        logging.error("JSONDecodeError")
        return {}


def find_former_deck(code: str, deck_mode):
    """Looks for a deck by its code, and returns its former deck in the upgrade list."""
    curr_deck = find_deck(code, deck_mode)
    if curr_deck:
        former_code = str(curr_deck["previous_deck"])
        former_deck = find_deck(former_code, deck_mode)
        if former_deck:
            return former_deck
        else:
            return False
    return False
