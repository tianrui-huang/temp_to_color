from openrgb import OpenRGBClient
from openrgb.utils import RGBColor
from sensors.cpu import CPUSensor
from sensors.gpu import GPUSensor
from effects.gradient import Gradient
from effects.smoother import ExponentialSmoother
from effects.breathing import Breathing
from effects.utils import apply_brightness
from rgb.openrgb import OpenRGBController
from config import *
import time


rgb = OpenRGBController()

cpu = CPUSensor()
gpu = GPUSensor()
cpu_smoother = ExponentialSmoother(alpha=CPU_ALPHA)
gpu_smoother = ExponentialSmoother(alpha=GPU_ALPHA)

breathing = Breathing(period=BREATHING_PERIOD, min_brightness=MIN_BRIGHTNESS, max_brightness=MAX_BRIGHTNESS)
 
cpu_gradient = Gradient(TEMPERATURE_POINTS)
gpu_gradient = Gradient(TEMPERATURE_POINTS)

#**调控接口**
effect = breathing  # 可选


last = time.monotonic()
while True:
    now = time.monotonic()
    dt = now - last
    last = now
   
    brightness = effect.update(dt)
    cpu_temp = cpu.temperature()
    gpu_temp = gpu.temperature()
    
    cpu_display = cpu_smoother.update(cpu_temp)
    gpu_display = gpu_smoother.update(gpu_temp)

    cpu_color = cpu_gradient.color(cpu_display)
    gpu_color = gpu_gradient.color(gpu_display)
    
    cpu_color = apply_brightness(cpu_color, brightness)
    gpu_color = apply_brightness(gpu_color, brightness)

    rgb.set_gpu_color(gpu_color)
    rgb.set_fan_color(cpu_color)
    print(f"CPU Temperature: {cpu.temperature()}°C")
    print(f"GPU Temperature: {gpu.temperature()}°C")
    time.sleep(REFRESH_RATE)