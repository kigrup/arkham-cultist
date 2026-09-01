import json

from config import BOT_LANGUAGE


class Rules:
    """Class that handles the rules data from the data/rules.json file."""

    def __init__(self):
        with open(f"data/{BOT_LANGUAGE}/rules.json", encoding="UTF-8") as f:
            self.rules_info = json.load(f)

    def get_rules(self):
        """Returns the rules data from the JSON file."""
        return self.rules_info["rules"]


rules_info = Rules()
