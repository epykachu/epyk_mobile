from dataclasses import dataclass
from typing import Any
import xml.etree.ElementTree as ET
import json

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

@dataclass
class AppLayout:
    barrierAllowsGoneWidgets: bool = None
    barrierDirection: str = None
    chainUseRtl: bool = None
    constraintSet: str = None
    constraint_referenced_ids: str = None
    content: str = None
    emptyVisibility: str = None
    layout_constrainedHeight: bool = None
    layout_constrainedWidth: bool = None
    layout_constraintBaseline_creator: int = None
    layout_constraintBaseline_toBaselineOf: str = None
    layout_constraintBottom_creator: int = None
    layout_constraintBottom_toBottomOf: str = None
    layout_constraintBottom_toTopOf: str = None
    layout_constraintCircle: str = None
    layout_constraintCircleAngle: int = None
    layout_constraintCircleRadius: str = None
    layout_constraintDimensionRatio: str = None
    layout_constraintEnd_toEndOf: str = None
    layout_constraintEnd_toStartOf: str = None
    layout_constraintGuide_begin: str = None
    layout_constraintGuide_end: str = None
    layout_constraintGuide_percent: float = None
    layout_constraintHeight_default: str = None
    layout_constraintHeight_max: str = None
    layout_constraintHeight_min: str = None
    layout_constraintHeight_percent: float = None
    layout_constraintHorizontal_bias: float = None
    layout_constraintHorizontal_chainStyle: str = None
    layout_constraintHorizontal_weight: float = None
    layout_constraintLeft_creator: int = None
    layout_constraintLeft_toLeftOf: str = None
    layout_constraintLeft_toRightOf: str = None
    layout_constraintRight_creator: int = None
    layout_constraintRight_toLeftOf: str = None
    layout_constraintRight_toRightOf: str = None
    layout_constraintStart_toEndOf: str = None
    layout_constraintStart_toStartOf: str = None
    layout_constraintTop_creator: int = None
    layout_constraintTop_toBottomOf: str = None
    layout_constraintTop_toTopOf: str = None
    layout_constraintVertical_bias: float = None
    layout_constraintVertical_chainStyle: str = None
    layout_constraintVertical_weight: float = None
    layout_constraintWidth_default: str = None
    layout_constraintWidth_max: str = None
    layout_constraintWidth_min: str = None
    layout_constraintWidth_percent: float = None
    layout_editor_absoluteX: str = None
    layout_editor_absoluteY: str = None
    layout_goneMarginBottom: str = None
    layout_goneMarginEnd: str = None
    layout_goneMarginLeft: str = None
    layout_goneMarginRight: str = None
    layout_goneMarginStart: str = None
    layout_goneMarginTop: str = None
    layout_optimizationLevel: str = None


class ToolsLayout(AppLayout):
    pass


@dataclass
class View:
    id: str
    layout_width: str
    layout_height: str

    def __post_init__(self):
        self.id = f"@+id/{self.id}"
        self.__node = ET.Element(self.__class__.__name__)
        self.__app_layout = AppLayout()
        self.__tool_layout = ToolsLayout()
        self.__child_nodes = []

    def __add__(self, node):
        node.inReport = False
        self.__child_nodes.append(node)

    @property
    def app(self):
        return self.__app_layout

    @property
    def tools(self):
        return self.__tool_layout

    def __forge(self):
        for attr_name, attr_val in self.__dict__.items():
            if attr_val is not None and not attr_name.startswith("_"):
                if type(attr_val) == bool:
                    self.__node.set(f"android:{attr_name}", json.dumps(attr_val))
                else:
                    self.__node.set(f"android:{attr_name}", attr_val)
        for attr_name, attr_val in self.app.__dict__.items():
            if attr_val is not None and not attr_name.startswith("_"):
                if type(attr_val) == bool:
                    self.__node.set(f"app:{attr_name}", json.dumps(attr_val))
                else:
                    self.__node.set(f"app:{attr_name}", attr_val)
        for child_node in self.__child_nodes:
            self.__node.append(child_node.forge())
        return self.__node

    def __str__(self):
        return ET.tostring(self.__forge(), encoding="unicode")


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
class ViewGroup(ViewDefault, View):
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
class ImageView(ViewDefault, View):
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
class TextView(ViewDefault, View):
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
