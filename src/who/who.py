from src.core.cards_db import cards
from src.core.formatting import create_embed, format_text, format_xp
from src.core.translator import locale as _
from src.who.utils import match_investigator_deck_options, filter_by_classes
from config import ARKHAM_BUILD
from src.core.arkhambuild import LocalizedAttribute as attr


def resolve_search_who(array, guild_id="None"):
    """Resolves the who command for a card."""
    if len(array) > 0:
        card = array[0]
        who_can_take = []
        who_cannot_take = []
        investigators = (inv for inv in cards.get_investigators() if inv["id"] != '90087' and inv["id"] != '03006' and "-" not in inv["id"])
        if "xp" in card:
            for inv in investigators:
                result = match_investigator_deck_options(inv, card)
                if result:
                    who_can_take.append(inv)
                else:
                    who_cannot_take.append(inv)

            if 0 <= len(who_cannot_take) <= 10:
                embed = format_who(card, who_cannot_take, positive=False, guild_id=guild_id)
            else:
                embed = format_who(card, who_can_take, guild_id=guild_id)

            return embed
    return None


def format_who(card, array, positive=True, guild_id="None"):
    """Formats the who command for a card."""
    neg_text = "" if positive else "_neg"
    title = f"{_(f'ahWho_title{neg_text}')}: {card[attr.NAME.get(card)]}{format_xp(card)}"
    description = ""

    if len(array) == 0 and not positive:
        title = f"{_('ahWho_title')}: {card[attr.NAME.get(card)]}{format_xp(card)}"
        description = f"{_('ahWho_everyone')}"
        return create_embed(title=title, description=description, c=card)

    if card["xp"] == 0 and card["faction_code"] != "neutral":
        description += f"{format_text(_('ahWho_versatile_text')), guild_id}\n"

    if not positive:
        description += f"{_('ahWho_neg_text')}"

    embed = create_embed(title=title, description=description, c=card)

    classes = filter_by_classes(array)

    for faction, investigators in classes.items():
        if investigators:
            names = [f"{c[attr.NAME.get(c)]}[↗]({ARKHAM_BUILD}/card/{c["code"]})" for c in investigators]
            description = ", ".join(names)
            title = f"{format_text('[' + faction + ']', guild_id)}{_(faction)} ({len(investigators)}):"
            embed.add_field(name=title, value=description)

    return embed
