import subprocess


class GPUSensor:
    def temperature(self) -> float:
        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=temperature.gpu",
                "--format=csv,noheader,nounits",
            ],
            text=True,
        )

        return float(output.strip())