import requests
import logging

from config import ARKHAM_BUILD_API, API_LANGUAGE

class Metadata:
    """
    This class contains the metadata from arkham.build which includes packs, cycles and encounters
    """

    def __init__(self):
        logging.info("Initializing Metadata...")
        self.metadata = requests.get(
            f"{ARKHAM_BUILD_API}/cache/metadata/{API_LANGUAGE}", timeout=10
        ).json()["data"]
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

metadata = Metadata()