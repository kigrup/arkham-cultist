from interactions import Embed
import logging

from src.core.formatting import (
    format_faction,
    format_name,
    format_subtext,
    format_card_text,
    format_set,
    format_illus_pack,
    create_embed,
)
from src.core.utils import text_if
from src.api_interaction.errata import errata
from src.core.arkhambuild import LocalizedAttribute as attr


def format_inv_card_b(c: dict, guild_id="None", back=True) -> Embed:
    """Format an investigator card's back side."""
    faction = format_faction(c, guild_id)
    name = format_name(c)
    subname = format_subtext(c)
    deck_req = text_if("> %s", format_card_text(c, attr.BACK_TEXT.get(c), guild_id))
    flavour = f"_{format_card_text(c, attr.BACK_FLAVOR.get(c), guild_id)}_"
    errata_text = errata.format_errata_text(c["code"], back=True, guild_id=guild_id)

    m_title = f"{faction} {name} {subname}"
    m_description = f"{deck_req}\n\n{flavour}\n\n{errata_text}"
    m_footnote = format_illus_pack(c)
    embed = create_embed(m_title, m_description, c, m_footnote, back=back)
    return embed


def format_location_card_b(c: dict, guild_id="None", back=True) -> Embed:
    """Format a location card's back side."""
    name = format_name(c)
    back_text = text_if("> %s", format_card_text(c, attr.BACK_TEXT.get(c), guild_id))
    flavour = f"_{format_card_text(c, attr.BACK_FLAVOR.get(c), guild_id)}_"

    m_title = name
    m_description = f"{back_text}\n\n{flavour}"
    m_footnote = format_illus_pack(c)
    embed = create_embed(m_title, m_description, c, m_footnote, back=back)
    return embed


def format_general_card_b(c: dict, guild_id="None", back=True) -> Embed:
    """Format a general card's back side."""
    name = format_name(c)
    subname = format_subtext(c)
    back_text = text_if("> %s", format_card_text(c, attr.BACK_TEXT.get(c), guild_id))
    pack = format_set(c)
    flavour = f"_{format_card_text(c, attr.BACK_FLAVOR.get(c), guild_id)}_"

    m_title = f"{name} {subname}"
    m_description = f"{flavour}\n\n{back_text}"
    m_footnote = pack
    embed = create_embed(m_title, m_description, c, m_footnote, back=back)
    return embed
