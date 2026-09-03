from src.core.utils import is_lvl

def use_pc_keywords(cards: list, query: dict):
    """
    Filtra cartas de jugador según los caracteres del string dado
    :param query:
    :param cards: Lista de cartas
    :param key_list: Argumentos dados
    :return:
    """
    filtered_cards = cards.copy()

    if "extras" in query and query["extras"]:
        char = query["extras"].lower()
        if char == "u":
            filtered_cards = [
                c
                for c in filtered_cards
                if (c["is_unique"] if "is_unique" in c else False)
            ]
        if char == "p":
            filtered_cards = [c for c in filtered_cards if "permanent" in c]
        if char == "c":
            filtered_cards = [
                c for c in filtered_cards if "deck only." in c["real_text"]
            ]
        if char == "e":
            filtered_cards = [c for c in filtered_cards if c["exceptional"]]

    if "level" in query and query["level"] != '':
        filtered_cards = [c for c in filtered_cards if is_lvl(c, query["level"])]

    if "faction" in query and query["faction"]:
        char = query["faction"].lower()
        if char == "b":
            filtered_cards = [
                c for c in filtered_cards if c["faction_code"] == "seeker"
            ]
        if char == "g":
            filtered_cards = [
                c for c in filtered_cards if c["faction_code"] == "guardian"
            ]
        if char == "r":
            filtered_cards = [c for c in filtered_cards if c["faction_code"] == "rogue"]
        if char == "s":
            filtered_cards = [
                c for c in filtered_cards if c["faction_code"] == "survivor"
            ]
        if char == "m":
            filtered_cards = [
                c for c in filtered_cards if c["faction_code"] == "mystic"
            ]
        if char == "n":
            filtered_cards = [
                c for c in filtered_cards if c["faction_code"] == "neutral"
            ]
        if char == "mult":
            filtered_cards = [c for c in filtered_cards if "faction2_code" in c]

    if "traits" in query and query["traits"]:
        traits = query["traits"].split(",")
        traits = [t.strip() for t in traits]
        filtered_cards = [c for c in filtered_cards if "real_traits" in c]

        for trait in traits:
            # This is a workaround to avoid the last dot in the traits
            filtered_cards = [
                c for c in filtered_cards if trait in c["real_traits"][:-1].split(". ")
            ]

    return filtered_cards
