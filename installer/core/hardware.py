import platform
import subprocess
from installer.core.logger import log

def detect_hardware():
    hardware_info = {}

    # CPU information
    try:
        cpu = subprocess.check_output(
            "lscpu | grep 'Model name'",
            shell=True
        ).decode().strip()

        cpu = cpu.split(":")[1].strip()
    except Exception:
        cpu = "Unknown"

    hardware_info["cpu"] = cpu

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

    
