from src.core.formatting import format_number, format_text
from src.core.translator import locale as _


def format_enemy_stats(c, guild_id="None"):
    per_inv = c["health_per_investigator"] if "health_per_investigator" in c else False
    health = "[health] %s%s" % (
        format_number(c["health"]) if "health" in c else "-",
        "[per_investigator]" if per_inv else "",
    )
    combat = "[combat] %s" % (
        format_number(c["enemy_fight"]) if "enemy_fight" in c else "-"
    )
    agility = "[agility] %s" % (
        format_number(c["enemy_evade"]) if "enemy_evade" in c else "-"
    )

    return format_text(f"{combat} / {health} / {agility}", guild_id)


def format_clues(c, guild_id="None"):
    if "clues" in c:
        clues = str(c["clues"])
        if "clues_fixed" in c or c["clues"] == 0:
            return format_text(f"[clues] {clues}", guild_id)
        else:
            return format_text(f"[clues] {clues} [per_investigator]", guild_id)
    else:
        return format_text("[clues] -", guild_id)


def format_location_data(c, guild_id="None"):
    shroud_value = str(c["shroud"]) if "shroud" in c else "-"
    shroud = f"{_('shroud')}: {shroud_value}"
    clues = format_clues(c, guild_id)
    return f"{shroud} | {clues}"


def format_attack(c, verbose=True, guild_id="None"):
    damage = ""
    if "enemy_damage" in c:
        damage = format_text("[health]" * c["enemy_damage"], guild_id)
    horror = ""
    if "enemy_horror" in c:
        horror = format_text("[sanity]" * c["enemy_horror"], guild_id)

    if not damage and not horror:
        return ""
    elif verbose:
        return f"{_('attack')}: {damage}{horror}\n"
    else:
        return f"{damage}{horror}\n"


def extract_token_info(tokens, guild_id="None"):
    lines = tokens.split("\n")
    symbols = ["", "", "", ""]  # Skull / Cultist / Tablet / Elder
    for line in lines:
        if "[skull]" in line:
            symbols[0] = f"[skull]: {line.split(': ')[1][:2]}"
        if "[cultist]" in line:
            symbols[1] = f"[cultist]: {line.split(': ')[1][:2]}"
        if "[tablet]" in line:
            symbols[2] = f"[tablet]: {line.split(': ')[1][:2]}"
        if "[elder_thing]" in line:
            symbols[3] = f"[elder_thing]: {line.split(': ')[1][:2]}"

    text = "["
    for s in symbols:
        if s:
            text += s
    text += "]"
    return format_text(text, guild_id)
