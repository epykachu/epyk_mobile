from dataclasses import dataclass

from epyk_mobile.core.constants import (TintModeEnum,
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
                                    VisibilityEnum
                                )

class ToolsLayout(object):
    pass

class AppLayout(object):
    pass

@dataclass
class AndroidViewObject(object):
    id: str
    accessibilityHeading: bool
    accessibilityLiveRegion: int
    accessibilityPaneTitle: str
    accessibilityTraversalAfter: int
    accessibilityTraversalBefore: int
    alpha: float
    autofillHints: str
    autofilledHighlight: str
    background: int
    backgroundTint: str
    backgroundTintMode: TintModeEnum
    clickable: bool
    contentDescription: str
    contextClickable: bool
    defaultFocusHighlightEnabled: bool
    drawingCacheQuality: int
    duplicateParentState: float
    elevation: float
    fadeScrollbars: bool
    fadingEdgeLength: str
    filterTouchesWhenObscured: bool
    fitsSystemWindows: bool
    focusable: int
    focusableInTouchMode: bool
    focusedByDefault: bool
    forceHasOverlappingRendering: bool
    foreground: str
    foregroundGravity: GravityEnum
    foregroundTint: str
    foregroundTintMode: TintModeEnum
    hapticFeedbackEnabled: bool
    importantForAccessibility: int
    importantForAutofill: ImportantEnum
    importantForContentCapture: ImportantEnum
    isScrollContainer: bool
    keepScreenOn: bool
    keyboardNavigationCluster: bool
    layerType: LayerEnum
    layoutDirection: LayoutDirectionEnum
    longClickable: bool
    minHeight: str
    minWidth: str
    nextClusterForward: str
    nextFocusDown: str
    nextFocusForward: str
    nextFocusLeft: str
    nextFocusRight: str
    nextFocusUp: str
    onClick: str
    outlineAmbientShadowColor: str
    outlineSpotShadowColor: str
    padding: str
    paddingBottom: str
    paddingEnd: str
    paddingHorizontal: str
    paddingLeft: str
    paddingRight: str
    paddingStart: str
    paddingTop: str
    paddingVertical: str
    requiresFadingEdge: FadingEnum
    rotation: float
    rotationX: float
    rotationY: float
    saveEnabled: bool
    scaleX: float
    scaleY: float
    screenReaderFocusable: bool
    scrollIndicators: ScrollEnum
    scrollX: str
    scrollY: str
    scrollbarAlwaysDrawHorizontalTrack: bool
    scrollbarAlwaysDrawVerticalTrack: bool
    scrollbarDefaultDelayBeforeFade: int
    scrollbarFadeDuration: int
    scrollbarSize: str
    scrollbarStyle: StyleEnum
    scrollbarThumbHorizontal: str
    scrollbarThumbVertical: str
    scrollbarTrackHorizontal: str
    scrollbarTrackVertical: str
    scrollbars: ScrollbarsEnum
    soundEffectsEnabled: bool
    stateListAnimator: str
    tag: str
    textAlignment: AlignEnum
    textDirection: TextDirectionEnum
    theme: str
    tooltipText: str
    transformPivotX: str
    transformPivotY: str
    transitionName: str
    translationX: str
    translationY: str
    translationZ: str
    visibility: VisibilityEnum

