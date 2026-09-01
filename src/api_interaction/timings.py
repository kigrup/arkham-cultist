import json

from config import BOT_LANGUAGE
from src.core.formatting import format_text, create_embed


class Timings:
    """Class that handles the timing data from the data/timings.json file."""

    def __init__(self):
        with open(f"data/{BOT_LANGUAGE}/timings.json", encoding="UTF-8") as f:
            self.timings = json.load(f)

    def get_timings_data(self):
        """Returns the timings data from the JSON file."""
        return self.timings

    def find_formatted_timing(self, query, guild_id="None"):
        """Formats the timing information into an embed."""
        timing = self.timings["framework"][query]
        name, text = next(iter(timing.items()))
        title = f"**{name}**"
        description = ">>> "
        for line in text:
            description += f"{format_text(line, guild_id)}\n"
        embed = create_embed(title=title, description=description)
        return embed


timings = Timings()
