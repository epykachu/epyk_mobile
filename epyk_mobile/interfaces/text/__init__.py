from dataclasses import dataclass
from typing import Any
from epyk_mobile.interfaces.android import AndroidViewObject, AndroidViewDefault
from epyk_mobile.core.constants import (
    AutoLinkEnum,
    AutoSizeTextEnum,
    BreakStrategyEnum,
    CapitalizeEnum,
    BufferTypeEnum,
    TintModeEnum,
    EllipsizeEnum,
    GravityEnum,
    HyphenationEnum,
    ImeOptionsEnum,
    InputTypeEnum,
    JustificationModeEnum,
    NumericEnum,
    TextStyleEnum,
    TypefaceEnum,
)


@dataclass
class TextiViewObject(AndroidViewDefault, AndroidViewObject):
    """
    Python interface for the TextView Android object

    Related Pages:
    -------------

        https://developer.android.com/reference/android/widget/TextView#attr_android:allowUndo

    """

    allowUndo: bool = None
    autoLink: AutoLinkEnum = None
    autoSizeMaxTextSize: str = None
    autoSizeMinTextSize: str = None
    autoSizePresetSizes: Any = None
    autoSizeStepGranularity: str = None
    autoSizeTextType: AutoSizeTextEnum = None
    autoText: bool = None
    breakStrategy: BreakStrategyEnum = None
    bufferType: BufferTypeEnum = None
    capitalize: CapitalizeEnum = None
    cursorVisible: bool = None
    digits: str = None
    drawableBottom: str = None
    drawableEnd: str = None
    drawableLeft: str = None
    drawablePadding: float = None
    drawableRight: str = None
    drawableStart: str = None
    drawableTint: str = None
    drawableTintMode: TintModeEnum = None
    drawableTop: str = None
    editable: bool = None
    editorExtras: str = None
    elegantTextHeight: bool = None
    ellipsize: EllipsizeEnum = None
    ems: int = None
    enabled: bool = None
    fallbackLineSpacing: bool = None
    firstBaselineToTopHeight: int = None
    fontFamily: str = None
    fontFeatureSettings: str = None
    fontVariationSettings: str = None
    freezesText: bool = None
    gravity: GravityEnum = None
    height: str = None
    hint: str = None
    hyphenationFrequency: HyphenationEnum = None
    imeActionId: int = None
    imeActionLabel: str = None
    imeOptions: ImeOptionsEnum = None
    includeFontPadding: bool = None
    inputMethod: str = None
    inputType: InputTypeEnum = None
    justificationMode: JustificationModeEnum = None
    lastBaselineToBottomHeight: str = None
    letterSpacing: float = None
    lineHeight: str = None
    lineSpacingExtra: str = None
    lineSpacingMultiplier: float = None
    lines: int = None
    linksClickable: bool = None
    marqueeRepeatLimit: Any = None
    maxEms: int = None
    maxHeight: str = None
    maxLength: int = None
    maxLines: int = None
    maxWidth: str = None
    minEms: int = None
    minHeight: str = None
    minLines: int = None
    minWidth: str = None
    numeric: NumericEnum = None
    password: bool = None
    phoneNumber: bool = None
    privateImeOptions: str = None
    scrollHorizontally: bool = None
    selectAllOnFocus: bool = None
    shadowColor: str = None
    shadowDx: float = None
    shadowDy: float = None
    shadowRadius: float = None
    singleLine: bool = None
    text: str = None
    textAllCaps: bool = None
    textAppearance: str = None
    textColor: str = None
    textColorHighlight: str = None
    textColorHint: str = None
    textColorLink: str = None
    textCursorDrawable: str = None
    textFontWeight: int = None
    textIsSelectable: bool = None
    textScaleX: float = None
    textSelectHandle: str = None
    textSelectHandleLeft: str = None
    textSelectHandleRight: str = None
    textSize: str = None
    textStyle: TextStyleEnum = None
    typeface: TypefaceEnum = None
    width: str = None
