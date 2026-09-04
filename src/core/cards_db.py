import requests

from config import ARKHAM_BUILD_API, API_LANGUAGE
from src.core.translator import locale as _
from src.core.utils import get_code
from src.core.arkhambuild import LocalizedAttribute as attr


class CardsDB:
    """
    This class contains the cards from arkham.build, with its Errata and Taboo data.
    """

    def __init__(self):
        self.ah_all_cards = requests.get(
            f"{ARKHAM_BUILD_API}/cache/cards/{API_LANGUAGE}", timeout=10
        ).json()["data"]["all_card"]

        self.taboo_set_versions = {}
        for c in self.ah_all_cards:
            if "taboo_set_id" in c:
                if c["code"] not in self.taboo_set_versions:
                    self.taboo_set_versions[c["code"]] = {}
                self.taboo_set_versions[c["code"]][c["taboo_set_id"]] = c


        self.ah_player = [
            c
            for c in self.ah_all_cards
            if ("encounter_code" not in c
             and "duplicate_of_code" not in c # Remove duplicates
             and "taboo_set_id" not in c # Remove taboo versions
             and not ("faction_code" in c and c["faction_code"] == "mythos")) 
            or ("real_text" in c and "Reward." in c["real_text"]) # Include reward cards
        ]

        self.ah_encounter = [c for c in self.ah_all_cards if "encounter_code" in c]
        self.ah_investigators = [
            c
            for c in self.ah_player
            if c["type_code"] == "investigator"
            and "deck_requirements" in c  # No Bonded/Hank
            and "alternate_of_code" not in c # No Parallels
        ]
        parallel_inv = [
            c
            for c in self.ah_player
            if "alternate_of_code" in c
        ]
        for inv in parallel_inv:
            inv["name"] = f"{inv['real_name']} ({_('parallel')})"
        self.ah_investigators += parallel_inv
        self.ah_customizable = [c for c in self.ah_player if "real_customization_text" in c] 

    def get_all_cards(self):
        """Returns all the cards from the game"""
        return self.ah_all_cards

    def get_p_cards(self):
        """Returns all the player cards from the game"""
        return self.ah_player

    def get_e_cards(self):
        """Returns all the encounter cards from the game"""
        return self.ah_encounter

    def get_investigators(self):
        """Returns all the investigators from the game"""
        return self.ah_investigators

    def get_customizable_cards(self, include_taboo_versions=True):
        """Returns all the customizable cards from the game"""
        return self.ah_customizable if not include_taboo_versions else [c for c in self.ah_customizable if "taboo_set_id" not in c]

    def get_taboo_compliant_version(self, card, taboo_set_id):
        """Returns the version of a card compliant with a specific taboo set id"""
        if card["code"] in self.taboo_set_versions and taboo_set_id in self.taboo_set_versions[card["code"]]:
            return self.taboo_set_versions[card["code"]][taboo_set_id]
        return card


cards = CardsDB()
