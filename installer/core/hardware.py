import platform
import subprocess
from installer.core.logger import log

def detect_hardware():
    hardware_info = {}

# CPU information
    hardware_info["cpu"] = platform.processor()

# Architecture
    hardware_info["architecture"] = platform.machine()

# RAM (in MB)
    try:
        mem_kb = int(subprocess.check_output(
            ["grep", "MemTotal", "/proc/meminfo"]
        ).split()[1])
        hardware_info["ram_mb"] = mem_kb // 1024
    except Exception:
        hardware_info["ram_mb"] = None

    log(f"Detected hardware: {hardware_info}")
    return hardware_info
