from dataclasses import dataclass

from epyk_mobile.core.constants import (
    TintModeEnum,
    GravityEnum,
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
)


class ToolsLayout:
    pass


class AppLayout:
    pass


@dataclass
class AndroidViewObject:
    id: str
    layout_width: str
    layout_height: str


@dataclass
class AndroidViewDefault:
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
