import requests
import logging

from datetime import datetime
from babel.dates import format_date
from config import ARKHAM_BUILD_API, API_LANGUAGE, BOT_LANGUAGE
from src.core.translator import locale as _

class Metadata:
    """
    This class contains the metadata from arkham.build which includes packs, cycles and encounters
    """

    def __init__(self):
        logging.info("Initializing Metadata...")
        self.metadata = requests.get(
            f"{ARKHAM_BUILD_API}/cache/metadata/{API_LANGUAGE}", timeout=10
        ).json()["data"]

        self.metadata["taboo_set"].sort(key=lambda s: s["id"], reverse=True)
        self.LATEST_TABOO_SET = self.metadata["taboo_set"][0]["id"]
        logging.info("Initialized Metadata")

    def get_pack_name(self, code: str):
        for p in self.metadata["pack"]:
            if p["code"] == code:
                return p["name" if "name" in p else "real_name"]
        return ""

    def get_cycles(self):
        return ((cycle["name" if "name" in cycle else "real_name"], cycle["position"]) for cycle in self.metadata["cycle"])
    
    def get_encounter_set_name(self, code: str):
        for es in self.metadata["card_encounter_set"]:
            if es["code"] == code:
                return es["name" if "name" in es else "real_name"]
        return ""

    def get_taboo_sets(self):
        yield _("taboo_set_none"), 0
        yield _("taboo_set_latest"), self.LATEST_TABOO_SET
        
        for taboo_set in self.metadata["taboo_set"]:
            name = taboo_set["name"]
            if "date" in taboo_set:
                date = datetime.fromisoformat(taboo_set["date"].replace("Z", "+00:00"))
                localized_date = format_date(date, format="MMMM yyyy", locale=BOT_LANGUAGE)
                name = f"{name} ({localized_date})"
            yield name, taboo_set["id"]

metadata = Metadata()