from interactions import OptionType, SlashCommandChoice, SlashCommandOption

from src.api_interaction.preview import preview
from src.core.metadata import metadata
from src.core.cards_db import cards
from src.core.formatting import format_name
from src.core.translator import locale as _


def player_card_slash_options(name_req=False, allow_image_only=False):
    """Returns the slash command options for player cards."""
    return [
        SlashCommandOption(
            name="name",
            description=_("name_description"),
            type=OptionType.STRING,
            required=name_req,
        ),
        SlashCommandOption(
            name="level",
            description=_("level_description"),
            type=OptionType.STRING,
            required=False,
        )
    ] + ([
        SlashCommandOption(
            name="image_only",
            description=_("imageOnly_description"),
            type=OptionType.BOOLEAN,
            required=False,
        ) 
    ] if allow_image_only else []) + [
        SlashCommandOption(
            name="faction",
            description=_("faction_description"),
            type=OptionType.STRING,
            required=False,
            choices=[
                SlashCommandChoice(name=_("guardian"), value="G"),
                SlashCommandChoice(name=_("seeker"), value="B"),
                SlashCommandChoice(name=_("rogue"), value="R"),
                SlashCommandChoice(name=_("mystic"), value="M"),
                SlashCommandChoice(name=_("survivor"), value="S"),
                SlashCommandChoice(name=_("multiclass"), value="Mult"),
                SlashCommandChoice(name=_("neutral"), value="N"),
            ],
        ),
        SlashCommandOption(
            name="extras",
            description=_("extras_description"),
            type=OptionType.STRING,
            required=False,
            choices=[
                SlashCommandChoice(name=_("permanent"), value="P"),
                SlashCommandChoice(name=_("exceptional"), value="E"),
                SlashCommandChoice(name=_("unique"), value="U"),
                SlashCommandChoice(name=_("signature"), value="C"),
            ],
        ),
        SlashCommandOption(
            name="subtitle",
            description=_("sub_description"),
            type=OptionType.STRING,
            required=False,
        ),
        SlashCommandOption(
            name="cycle",
            description=_("pack_description"),
            choices=[
                SlashCommandChoice(name=cycle_name, value=f"{cycle_position:02}")
                for cycle_name, cycle_position in metadata.get_cycles()
            ],
            type=OptionType.STRING,
            required=False,
        ),
        SlashCommandOption(
            name="traits",
            description=_("traits_description"),
            type=OptionType.STRING,
            required=False,
        ),
        SlashCommandOption(
            name="taboo_set",
            description=_("taboo_description"),
            choices=[
                SlashCommandChoice(name=taboo_set_name, value=taboo_set_id)
                for taboo_set_name, taboo_set_id in metadata.get_taboo_sets()
            ],
            type=OptionType.NUMBER,
            required=False,
        )
    ]


def deck_slash_options():
    """Returns the slash command options for decks"""
    return [
        SlashCommandOption(
            name="code",
            description=_("deck_code_desc"),
            type=OptionType.NUMBER,
            required=True,
        ),
        SlashCommandOption(
            name="deck_type",
            description=_("deck_type_desc"),
            type=OptionType.STRING,
            required=False,
            choices=[
                SlashCommandChoice(name=_("public_deck"), value="decklist"),
                SlashCommandChoice(name=_("private_deck"), value="deck"),
            ],
        ),
    ]


def general_card_slash_options(allow_taboo_set=False):
    """Returns the slash command options for general cards."""
    
    return [
        SlashCommandOption(
            name="name",
            description=_("name_description"),
            type=OptionType.STRING,
            required=True,
        ),
        SlashCommandOption(
            name="card_type",
            description=_("card_type_desc"),
            type=OptionType.STRING,
            required=False,
            choices=[
                SlashCommandChoice(name=_("scenario"), value="S"),
                SlashCommandChoice(name=_("act"), value="A"),
                SlashCommandChoice(name=_("agenda"), value="P"),
                SlashCommandChoice(name=_("treachery"), value="T"),
                SlashCommandChoice(name=_("enemy"), value="E"),
                SlashCommandChoice(name=_("location"), value="L"),
                SlashCommandChoice(name=_("player_cards"), value="J"),
            ],
        ),
        SlashCommandOption(
            name="image_only",
            description=_("imageOnly_description"),
            type=OptionType.BOOLEAN,
            required=False,
        ),
        SlashCommandOption(
            name="subtitle",
            description=_("sub_description"),
            type=OptionType.STRING,
            required=False,
        ),
        SlashCommandOption(
            name="cycle",
            description=_("pack_description"),
            choices=[
                SlashCommandChoice(name=cycle_name, value=f"{cycle_position:02}")
                for cycle_name, cycle_position in metadata.get_cycles()
            ],
            type=OptionType.STRING,
            required=False,
        ),
        SlashCommandOption(
            name="traits",
            description=_("traits_description"),
            type=OptionType.STRING,
            required=False,
        ),
    ] + [
        SlashCommandOption(
            name="taboo_set",
            description=_("taboo_description"),
            choices=[
                SlashCommandChoice(name=taboo_set_name, value=taboo_set_id)
                for taboo_set_name, taboo_set_id in metadata.get_taboo_sets()
            ],
            type=OptionType.NUMBER,
            required=False,
        )
    ] if allow_taboo_set else []


def tarot_slash_options():
    """Returns the slash command options for Tarot cards."""
    return [
        SlashCommandOption(
            name="name",
            description=_("name_description"),
            type=OptionType.STRING,
            required=False,
        )
    ]


def timing_slash_options():
    """Returns the slash command options for Game's Framework."""
    return [
        SlashCommandOption(
            name="timing",
            description=_("timings_type_desc"),
            type=OptionType.STRING,
            required=True,
            choices=[
                SlashCommandChoice(name=_("mythos_phase"), value="M"),
                SlashCommandChoice(name=_("investigation_phase"), value="I"),
                SlashCommandChoice(name=_("enemy_phase"), value="E"),
                SlashCommandChoice(name=_("upkeep_phase"), value="U"),
                SlashCommandChoice(name=_("skill_test"), value="S"),
            ],
        )
    ]


def customizable_card_slash_options():
    """Return the slash command options for costumizable upgrade cards"""
    customizable_cards = cards.get_customizable_cards(include_taboo_versions=False)
    return [
        SlashCommandOption(
            name="name",
            description=_("name_description"),
            type=OptionType.STRING,
            required=True,
            choices=[
                SlashCommandChoice(name=f"{format_name(c)}", value=c["code"])
                for c in customizable_cards
            ],
        ),
        SlashCommandOption(
            name="taboo_set",
            description=_("taboo_description"),
            choices=[
                SlashCommandChoice(name=taboo_set_name, value=taboo_set_id)
                for taboo_set_name, taboo_set_id in metadata.get_taboo_sets()
            ],
            type=OptionType.NUMBER,
            required=False,
        ),
    ]
