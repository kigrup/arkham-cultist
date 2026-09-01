import json
from config import BOT_LANGUAGE


class Preview:
    """Class that handles the preview data from the data/preview.json file."""

    def __init__(self):
        with open(f"data/{BOT_LANGUAGE}/preview.json", encoding="UTF-8") as f:
            self.preview = json.load(f)

    def get_preview_data(self):
        """Returns the preview data from the JSON file.

        Returns:
            dict: The preview data.
        """
        return self.preview["cards"]


preview = Preview()
