from pathlib import Path

class CPUSensor:
    def __init__(self):
        self.temp_file = self._find_temp_file()

    def _find_temp_file(self):
        hwmon = Path("/sys/class/hwmon")

        for device in hwmon.iterdir():
            try:
                name = (device / "name").read_text().strip()

                if name == "k10temp":      # Ryzen
                    return device / "temp1_input"
            except FileNotFoundError:
                pass

        raise RuntimeError("CPU temperature sensor not found")

    def temperature(self) -> float:
        """返回 CPU 温度（℃）"""
        value = int(self.temp_file.read_text().strip())
        return value / 1000