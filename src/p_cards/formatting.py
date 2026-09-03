import logging
from src.core.formatting import (
    format_customizable_note,
    format_name,
    format_subtext,
    format_faction,
    format_card_text,
    faction_order,
    format_victory,
    format_illus_pack,
    create_embed,
    format_flavour,
    format_type,
    format_traits,
    format_text,
    slot_order,
    format_customizable,
)
from src.core.utils import text_if
from src.api_interaction.errata import errata
from src.p_cards.utils import (
    format_slot,
    format_skill_icons,
    format_health_sanity,
    format_inv_skills,
    format_sub_text_short,
    format_costs,
)
from src.api_interaction.taboo import taboo
from src.core.translator import locale as _
from config import ARKHAM_BUILD
from src.core.arkhambuild import LocalizedAttribute as attr


def format_player_card(c, guild_id="None", back=False):
    name = format_name(c)
    level = taboo.format_xp(c)
    subtext = format_subtext(c)
    faction = format_faction(c, guild_id)
    card_type = format_type(c)
    slot = format_slot(c, guild_id)
    customizable = format_customizable_note(c)

    traits = text_if("%s\n", format_traits(c))
    icons = text_if("%s\n", format_skill_icons(c, guild_id))
    costs = format_costs(c)

    text = text_if("> %s\n", format_card_text(c, guild_id=guild_id))
    flavour = text_if("%s\n", format_flavour(c))
    health_sanity = text_if("%s\n", format_health_sanity(c, guild_id))
    taboo_text = taboo.format_taboo_text(c["code"], guild_id)
    errata_text = errata.format_errata_text(c["code"], guild_id=guild_id)
    victory = text_if("> %s\n", format_victory(c))

    m_title = f"{faction} {name}{subtext}{level}"
    m_description = (
        f"{card_type} {slot}\n"
        f"{traits}"
        f"{costs}"
        f"{icons}\n"
        f"{text}"
        f"{customizable}"
        f"{victory}"
        f"{health_sanity}\n"
        f"{flavour}"
        f"{errata_text}"
        f"{taboo_text}"
    )
    m_footnote = format_illus_pack(c)
    return create_embed(m_title, m_description, c, m_footnote, back=back)


def format_inv_card_f(c, guild_id="None"):
    faction = format_faction(c, guild_id)
    name = format_name(c)
    subname = format_subtext(c)
    skills = format_inv_skills(c, guild_id)
    health_sanity = text_if("%s\n", format_health_sanity(c, guild_id))
    ability = text_if("> %s", format_card_text(c, guild_id=guild_id))
    traits = format_traits(c)
    taboo_text = taboo.format_taboo_text(c["code"], guild_id)
    errata_text = errata.format_errata_text(c["code"], guild_id=guild_id)
    flavour = format_flavour(c)

    m_title = f"{faction} {name}{subname}"
    m_description = (
        f"{skills}\n"
        f"{traits}\n\n"
        f"{ability}\n"
        f"{health_sanity}\n"
        f"{flavour}"
        f"{errata_text}\n"
        f"{taboo_text}\n"
    )
    m_footnote = format_illus_pack(c)
    return create_embed(m_title, m_description, c, m_footnote)


def format_player_card_deck(c, qty=0, taboo_info="", guild_id="None"):
    name = c[attr.NAME.get(c)]
    level = taboo.format_xp(c, taboo_info)
    faction = format_faction(c, guild_id)
    quantity = f"x{str(qty)}" if qty > 1 else ""
    subname = format_sub_text_short(c)
    slot = format_slot(c, guild_id)
    priority_order = slot_order(c) + faction_order[c["faction_code"]]
    taboo_text = (
        format_text(" [taboo]", guild_id) if taboo.is_in_taboo(c["code"], taboo_info) else ""
    )
    text = f"{priority_order}{faction}{slot} {name}{subname} {level}{taboo_text} {quantity} [↗]({ARKHAM_BUILD}/card/{c["code"]})"
    return text


def format_customizable_upgrades(c, guild_id="None"):
    name = format_name(c)
    level = taboo.format_xp(c)
    subtext = format_subtext(c)
    faction = format_faction(c, guild_id)

    customizable = format_customizable(c)
    taboo_text = taboo.format_taboo_text(c["code"], guild_id)
    errata_text = errata.format_errata_text(c["code"], guild_id=guild_id)

    m_title = f"{faction} {name}{subtext}{level}"
    m_description = (
        f"{_('customization_title')}\n\n{customizable}\n{errata_text}{taboo_text}"
    )
    m_footnote = format_illus_pack(c)
    return create_embed(m_title, m_description, c, m_footnote)
