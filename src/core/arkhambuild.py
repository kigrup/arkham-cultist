from enum import Enum

class LocalizedAttribute(Enum):
    NAME = "name"
    BACK_NAME = "back_name"
    SUBNAME = "subname"
    BACK_SUBNAME = "back_subname"
    TEXT = "text"
    BACK_TEXT = "back_text"
    FLAVOR = "flavor"
    BACK_FLAVOR = "back_flavor"
    TRAITS = "traits"
    BACK_TRAITS = "back_traits"
    CUSTOMIZATION_TEXT = "customization_text"
    CUSTOMIZATION_CHANGE = "customization_change"

    def get(self, obj):
        return self.value if self.value in obj else f"real_{self.value}"
