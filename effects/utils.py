from openrgb.utils import RGBColor

def apply_brightness(color: RGBColor, brightness: float) -> RGBColor:
    return RGBColor(
        round(color.red * brightness),
        round(color.green * brightness),
        round(color.blue * brightness),
    )