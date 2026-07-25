from openrgb.utils import RGBColor

TEMPERATURE_POINTS = [
    (30, RGBColor(0,0,255)),
    (45, RGBColor(0,255,255)),
    (60, RGBColor(0,255,0)),
    (70, RGBColor(255,255,0)),
    (80, RGBColor(255,128,0)),
    (90, RGBColor(255,0,0)),
]

CPU_ALPHA = 0.15
GPU_ALPHA = 0.15

REFRESH_RATE = 0.02

BREATHING_PERIOD = 3.0
MIN_BRIGHTNESS = 0.3
MAX_BRIGHTNESS = 1.0