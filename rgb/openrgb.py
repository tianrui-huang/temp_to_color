from openrgb import OpenRGBClient
import time


class OpenRGBController:
    def __init__(self):
        while True:
            try:
                client = OpenRGBClient()
                break
            except ConnectionRefusedError:
                time.sleep(2)

        BOARD = client.devices[0]

        self.gpu = BOARD.zones[1]      # Aura Addressable 2
        self.fan = BOARD.zones[2]      # Aura Addressable 3

    def set_gpu_color(self, color):
        self.gpu.set_color(color)

    def set_fan_color(self, color):
        self.fan.set_color(color)