from dataclasses import dataclass
from typing import Any


from epyk_mobile.core.constants import (
    ImportantEnum,
    LayerEnum,
    LayoutDirectionEnum,
    FadingEnum,
    ScrollEnum,
    StyleEnum,
    ScrollbarsEnum,
    AlignEnum,
    TextDirectionEnum,
    VisibilityEnum,
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
    ScaleTypeEnum,
    DescendantFocusabilityEnum,
    LayoutModeEnum,
    PersistentDrawingCache,
)


class ToolsLayout:
    pass


class AppLayout:
    pass


@dataclass
class ViewObject:
    id: str
    layout_width: str
    layout_height: str


@dataclass
class ViewDefault:
    accessibilityHeading: bool = None
    accessibilityLiveRegion: int = None
    accessibilityPaneTitle: str = None
    accessibilityTraversalAfter: int = None
    accessibilityTraversalBefore: int = None
    alpha: float = None
    autofillHints: str = None
    autofilledHighlight: str = None
    background: int = None
    backgroundTint: str = None
    backgroundTintMode: TintModeEnum = None
    clickable: bool = None
    contentDescription: str = None
    contextClickable: bool = None
    defaultFocusHighlightEnabled: bool = None
    drawingCacheQuality: int = None
    duplicateParentState: float = None
    elevation: float = None
    fadeScrollbars: bool = None
    fadingEdgeLength: str = None
    filterTouchesWhenObscured: bool = None
    fitsSystemWindows: bool = None
    focusable: int = None
    focusableInTouchMode: bool = None
    focusedByDefault: bool = None
    forceHasOverlappingRendering: bool = None
    foreground: str = None
    foregroundGravity: GravityEnum = None
    foregroundTint: str = None
    foregroundTintMode: TintModeEnum = None
    hapticFeedbackEnabled: bool = None
    importantForAccessibility: int = None
    importantForAutofill: ImportantEnum = None
    importantForContentCapture: ImportantEnum = None
    isScrollContainer: bool = None
    keepScreenOn: bool = None
    keyboardNavigationCluster: bool = None
    layerType: LayerEnum = None
    layoutDirection: LayoutDirectionEnum = None
    longClickable: bool = None
    minHeight: str = None
    minWidth: str = None
    nextClusterForward: str = None
    nextFocusDown: str = None
    nextFocusForward: str = None
    nextFocusLeft: str = None
    nextFocusRight: str = None
    nextFocusUp: str = None
    onClick: str = None
    outlineAmbientShadowColor: str = None
    outlineSpotShadowColor: str = None
    padding: str = None
    paddingBottom: str = None
    paddingEnd: str = None
    paddingHorizontal: str = None
    paddingLeft: str = None
    paddingRight: str = None
    paddingStart: str = None
    paddingTop: str = None
    paddingVertical: str = None
    requiresFadingEdge: FadingEnum = None
    rotation: float = None
    rotationX: float = None
    rotationY: float = None
    saveEnabled: bool = None
    scaleX: float = None
    scaleY: float = None
    screenReaderFocusable: bool = None
    scrollIndicators: ScrollEnum = None
    scrollX: str = None
    scrollY: str = None
    scrollbarAlwaysDrawHorizontalTrack: bool = None
    scrollbarAlwaysDrawVerticalTrack: bool = None
    scrollbarDefaultDelayBeforeFade: int = None
    scrollbarFadeDuration: int = None
    scrollbarSize: str = None
    scrollbarStyle: StyleEnum = None
    scrollbarThumbHorizontal: str = None
    scrollbarThumbVertical: str = None
    scrollbarTrackHorizontal: str = None
    scrollbarTrackVertical: str = None
    scrollbars: ScrollbarsEnum = None
    soundEffectsEnabled: bool = None
    stateListAnimator: str = None
    tag: str = None
    textAlignment: AlignEnum = None
    textDirection: TextDirectionEnum = None
    theme: str = None
    tooltipText: str = None
    transformPivotX: str = None
    transformPivotY: str = None
    transitionName: str = None
    translationX: str = None
    translationY: str = None
    translationZ: str = None
    visibility: VisibilityEnum = None


@dataclass
class ViewGroup(ViewDefault, ViewObject):
    addStatesFromChildren: bool = None
    alwaysDrawnWithCache: bool = None
    animateLayoutChanges: bool = None
    animationCache: bool = None
    clipChildren: bool = None
    clipToPadding: bool = None
    descendantFocusability: DescendantFocusabilityEnum = None
    layoutAnimation: str = None
    layoutMode: LayoutModeEnum = None
    persistentDrawingCache: PersistentDrawingCache = None
    splitMotionEvents: bool = None


@dataclass
class ImageView(ViewDefault, ViewObject):
    adjustViewBounds: bool = None
    baseline: str = None
    baselineAlignBottom: bool = None
    cropToPadding: bool = None
    maxHeight: str = None
    maxWidth: str = None
    scaleType: ScaleTypeEnum = None
    src: str = None
    tint: str = None
    tintMode: TintModeEnum = None


@dataclass
class TextViewObject(ViewDefault, ViewObject):
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
