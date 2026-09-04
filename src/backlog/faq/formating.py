from src.core.formatting import (
    format_name,
    format_xp,
    format_subtext,
    format_faction,
    format_illus_pack,
    create_embed,
    format_card_text,
    format_text,
)
from src.core.translator import locale as _
from src.backlog.faq.faq import faq_info
from src.core.arkhambuild import LocalizedAttribute as attr


def format_faq(c, guild_id="None"):
    """Formats the FAQ information of a card."""
    name = format_name(c)
    subtext = format_subtext(c)
    faction = format_faction(c, guild_id)
    level = format_xp(c)
    text = f"> {format_card_text(c, guild_id=guild_id)}"
    faq = format_faq_text(c["code"], back=False, guild_id)

    title = f"{faction} {name}{subtext} {level if level else ''}"
    description = f"{text}\n{faq}"
    m_footnote = format_illus_pack(c)
    return create_embed(title, description, c, m_footnote)


def format_faq_text(card_id, back=False, guild_id="None"):
    """Formats the FAQ text of a card."""
    text = f"**{_('faq_title')}**: \n"
    if faq_info.has_faq(card_id):
        card = faq_info.get_faq(card_id)
        if back and ("text_back" in card):
            text += f">>> {format_text(card['text_back'], guild_id)} \n"
        elif "text" in card:
            text += f">>> {format_text(card['text'], guild_id)} \n"
        return text
    else:
        return _("faq_not_found")
