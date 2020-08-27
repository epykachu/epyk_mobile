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
    end = 800005
    fill = 77
    fill_horizontal = 7
    fill_vertical = 70
    left = 3
    right = 5
    start = 800003
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


class AutoLinkEnum(enum.Enum):
    all = "f"
    email = 2
    map = 8
    none = 0
    phone = 4
    web = 1


class AutoSizeTextEnum(enum.Enum):
    none = 0
    uniform = 1


class BreakStrategyEnum(enum.Enum):
    balanced = 2
    high_quality = 1
    simple = 0


class BufferTypeEnum(enum.Enum):
    editable = 2
    normal = 0
    simple = 1


class CapitalizeEnum(enum.Enum):
    characters = 3
    none = 0
    sentences = 1
    words = 2


class EllipsizeEnum(enum.Enum):
    end = 3
    marquee = 4
    middle = 2
    none = 0
    start = 1


class HyphenationEnum(enum.Enum):
    full = 2
    none = 0
    normal = 1


class ImeOptionsEnum(enum.Enum):
    actionDone = 6
    actionGo = 2
    actionNext = 5
    actionNone = 1
    actionPrevious = 7
    actionSearch = 3
    actionSend = 4
    actionUnspecified = 0
    flagForceAscii = 80000000
    flagNavigateNext = 8000000
    flagNavigatePrevious = 4000000
    flagNoAccessoryAction = 20000000
    flagNoEnterAction = 40000000
    flagNoExtractUi = 10000000
    flagNoFullscreen = 2000000
    flagNoPersonalizedLearning = 1000000
    normal = 0


class InputTypeEnum(enum.Enum):
    date = 14
    datetime = 4
    none = 0
    number = 2
    numberDecimal = 2002
    numberPassword = 12
    numberSigned = 1002
    phone = 3
    text = 1
    textAutoComplete = 10001
    textAutoCorrect = 8001
    textCapCharacters = 1001
    textCapSentences = 4001
    textCapWords = 2001
    textEmailAddress = 21
    textEmailSubject = 31
    textFilter = "b1"
    textImeMultiLine = 40001
    textLongMessage = 51
    textMultiLine = 20001
    textNoSuggestions = 80001
    textPassword = 81
    textPersonName = 61
    textPhonetic = "c1"
    textPostalAddress = 71
    textShortMessage = 41
    textUri = 11
    textVisiblePassword = 91
    textWebEditText = "a1"
    textWebEmailAddress = "d1"
    textWebPassword = "e1"
    time = 24


class JustificationModeEnum(enum.Enum):
    none = 0
    inter_word = 1


class NumericEnum(enum.Enum):
    decimal = 5
    integer = 1
    signed = 3


class TextStyleEnum(enum.Enum):
    bold = 1
    italic = 2
    normal = 0


class TypefaceEnum(enum.Enum):
    monospace = 3
    sans = 1
    normal = 0
    serif = 2
