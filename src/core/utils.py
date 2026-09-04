def split_files(src: str):
    splits = src.split("/")
    rest = ""
    for a in splits[:-1]:
        rest += f"{a}/"
    return rest

def is_lvl(card: dict, lvl: str):
    """
    Runs a query against a card's level, if the card doesnt have a level it always returns false.
    :param card: card
    :param lvl: an integer of the level to check for, or a string with a greater than or less than sign to check for a range of levels.
    :return:
    """
    if "xp" in card:
        if (type(lvl) == str and lvl.isnumeric()) or type(lvl) == int:
            return card["xp"] == int(lvl)
        elif type(lvl) == str and len(lvl) == 2 and lvl[1].isnumeric():
            if lvl[0] == '<':
                return card["xp"] < int(lvl[1])
            elif lvl[0] == '>':
                return card["xp"] > int(lvl[1])
            return card["x"] in list(range())
        elif ',' in lvl:
            lvl = lvl.split(',')
            return card["xp"] in [int(q) for q in lvl]

    return False

def get_qty(deck, card_id):
    for c_id, qty in deck["slots"].items():
        if c_id == card_id:
            return qty
    return 0


def has_trait(card, trait):
    try:
        traits = card["real_traits"].lower().split()
        return f"{trait}." in traits

    except KeyError:
        return False


def text_if(template, text):
    if text:
        return template % text
    else:
        return ""


def get_code(card):
    card_id = card["code"]
    while card_id:
        try:
            return int(card_id)
        except ValueError:
            card_id = card_id[:-1]
    return 0

def calculate_xp(card, qty):
    if "xp" not in card:
        return 0
    return qty * (card["xp"] * (2 if "exceptional" in card and card["exceptional"] else 1) + (card["taboo_xp"] if "taboo_xp" in card else 0))