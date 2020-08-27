import enum


class TintModeEnum(enum.Enum):
    add = 10
    multiply = "e"
    screen = "f"
    src_atop = 9
    src_in = 5
    src_over = 3


class GravityEnum(enum.Enum):
    bottom = 50
    center = 11
    center_horizontal = 1
    center_vertical = 10
    clip_horizontal = 8
    clip_vertical = 80
    fill = 77
    fill_horizontal = 7
    fill_vertical = 70
    left = 3
    right = 5
    top = 30


class ImportantEnum(enum.Enum):
    auto = 0
    no = 2
    noExcludeDescendants = 8
    yes = 1
    yesExcludeDescendants = 4


class LayerEnum(enum.Enum):
    hardware = 2
    none = 0
    software = 1


class LayoutDirectionEnum(enum.Enum):
    inherit = 2
    locale = 3
    ltr = 0
    rtl = 1


class FadingEnum(enum.Enum):
    horizontal = 1000
    none = 0
    vertical = 2000


class ScrollEnum(enum.Enum):
    bottom = 2
    end = 20
    left = 4
    none = 0
    right = 8
    start = 10
    top = 1


class StyleEnum(enum.Enum):
    insideInset = 1000000
    insideOverly = 0
    outsideInset = 3000000
    outsideOverlay = 2000000


class ScrollbarsEnum(enum.Enum):
    horizontal = 100
    none = 0
    vertical = 200


class AlignEnum(enum.Enum):
    center = 4
    gravity = 1
    inherit = 0
    textEnd = 3
    textStart = 2
    viewEnd = 6
    viewStart = 5


class TextDirectionEnum(enum.Enum):
    anyRtl = 2
    firstStrong = 1
    firstStrongLtr = 6
    firstStrongRtl = 7
    inherit = 0
    locale = 5
    ltr = 3
    rtl = 4

class VisibilityEnum(enum.Enum):
    gone = 2
    invisibility = 1
    visible = 0