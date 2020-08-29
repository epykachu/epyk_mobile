from dataclasses import dataclass
from epyk_mobile.interfaces.android import TextView, ImageView


@dataclass
class Button(TextView):
    pass


@dataclass
class ImageButton(ImageView):
    pass
