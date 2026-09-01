import requests

from config import ARKHAM_BUILD_API, API_LANGUAGE
from src.core.translator import locale as _
from src.core.utils import get_code


class CardsDB:
    """
    This class contains the cards from ArkhamDB, with its Errata, Taboo and Tarot data.
    """

    def __init__(self):
        self.ah_all_cards = requests.get(
            f"{ARKHAM_BUILD_API}/cache/cards/{API_LANGUAGE}", timeout=10
        ).json()["data"]["all_card"]

        self.ah_player = [
            c
            for c in self.ah_all_cards
            if "encounter_code" not in c or ("real_text" in c and "Reward." in c["real_text"])
        ]

        self.ah_player = [
            c
            for c in self.ah_player
            if "duplicate_of_code" not in c and not c["faction_code"] == "mythos" # Remove duplicates and mythos cards
        ]
        self.ah_encounter = [c for c in self.ah_all_cards if "encounter_code" in c]
        self.ah_investigators = [
            c
            for c in self.ah_player
            if c["type_code"] == "investigator"
            and "duplicate_of_code" not in c  # NO Duplicates
            and "deck_requirements" in c  # No Bonded/Hank
            and (
                1000 < get_code(c) < 70000  # No Parallels/Books
            )
        ]
        parallel_inv = [
            c
            for c in self.ah_player
            if "alternate_of_code" in c
            and "duplicate_of_code" not in c  # NO Duplicates
        ]
        for inv in parallel_inv:
            inv["name"] = f"{inv['real_name']} ({_('parallel')})"
        self.ah_investigators += parallel_inv
        self.ah_customizable = [c for c in self.ah_player if "customization_text" in c and "-" not in c["id"]]

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

    def get_customizable_cards(self):
        """Returns all the customizable cards from the game"""
        return self.ah_customizable


cards = CardsDB()
