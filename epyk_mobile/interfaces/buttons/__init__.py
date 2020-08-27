from dataclasses import dataclass
from epyk_mobile.interfaces.android import TextViewObject, ImageView


@dataclass
class Button(TextViewObject):
    pass

@dataclass
class ImageButton(ImageView):
    pass