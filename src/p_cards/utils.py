from config import SLOT_CUSTOM_EMOJIS
from src.core.formatting import format_text, format_number, color_picker
from src.core.search import find_by_id
from src.core.translator import locale as _


def format_slot(c, guild_id="None"):
    text = ""
    if "real_slot" in c or "slot" in c:
        slot_key = "real_slot" if "real_slot" in c else "slot"
        slots = c[slot_key].split(". ")
        for slot in slots:
            text += SLOT_CUSTOM_EMOJIS[guild_id if guild_id in SLOT_CUSTOM_EMOJIS else "None"][slot]

    return text


def format_inv_skills(c, guild_id="None"):
    will = f"{c['skill_willpower']} [willpower]" if "skill_willpower" in c else ""
    intel = f"{c['skill_intellect']} [intellect]" if "skill_intellect" in c else ""
    com = f"{c['skill_combat']} [combat]" if "skill_combat" in c else ""
    agi = f"{c['skill_agility']} [agility]" if "skill_agility" in c else ""
    return format_text(f"{will} {intel} {com} {agi}", guild_id)


def format_skill_icons(c, guild_id="None"):
    will = f"{c['skill_willpower'] * '[willpower]'}" if "skill_willpower" in c else ""
    intel = f"{c['skill_intellect'] * '[intellect]'}" if "skill_intellect" in c else ""
    com = f"{c['skill_combat'] * '[combat]'}" if "skill_combat" in c else ""
    agi = f"{c['skill_agility'] * '[agility]'}" if "skill_agility" in c else ""
    wild = f"{c['skill_wild'] * '[wild]'}" if "skill_wild" in c else ""
    return format_text(f"{will}{intel}{com}{agi}{wild}", guild_id)


def format_health_sanity(c, guild_id="None"):
    return format_text(
        "%s%s"
        % (
            "[health] %s " % format_number(c["health"]) if "health" in c else "",
            "[sanity] %s" % format_number(c["sanity"]) if "sanity" in c else "",
        ), guild_id
    )


def get_color_by_investigator(deck, cards):
    inv_id = deck["investigator_code"]
    inv_card = find_by_id(inv_id, cards)
    return color_picker(inv_card)


def format_sub_text_short(c):
    if "real_text" in c:
        if "subname" in c:
            if (
                "Researched." in c["real_text"]
                or "Directive" in c["real_name"]
                or "Discipline" in c["real_name"]
            ):
                return f": _{c['subname']}_"
        if "Advanced." in c["real_text"]:
            return " _(Adv)_"
    return ""


def format_costs(c):
    if "cost" in c:
        return f"{_('cost')}: %s \n" % format_number(c["cost"])
    else:
        return ""
