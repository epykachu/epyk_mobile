from dataclasses import dataclass
from epyk_mobile.interfaces.layouts import AbsoluteLayout
from epyk_mobile.interfaces.android import ViewGroup


@dataclass
class WebView(ViewGroup, AbsoluteLayout):
    pass
