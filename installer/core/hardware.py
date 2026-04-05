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

    #CHOICE GIVER
    def choose_profile():
    print("\nChoose installation profile:")
    print("1. Minimal (advanced users only)")
    print("2. Standard (recommended)")

    choice = input("Enter choice (1-2): ")

    if choice == "1":
        print("\n Minimal install selected.")
        print("This will install a barebones system.")
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() == "y":
            return "minimal"
        else:
            return "standard"

    return "standard"


    #DE SEL
    def choose_de():
    print("\nChoose Desktop Environment:")
    print("1. XFCE  - Lightweight and simple")
    print("2. KDE   - Modern and customizable")
    print("3. GNOME - Clean and minimal design")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        return "xfce"
    elif choice == "2":
        return "kde"
    elif choice == "3":
        return "gnome"
    else:
        return "xfce"  # fallback

    #APP SEL KINDA BROKEN RN
    def choose_apps():
    print("\nSelect applications to install:")
    
    apps = {
        "1": "browser",
        "2": "code_editor",
        "3": "media_player",
        "4": "office_tools",
        "5": "git"
    }

    print("1. Web Browser")
    print("2. Code Editor")
    print("3. Media Player")
    print("4. Office Tools")
    print("5. Git / Dev Tools")

    selected = input("Enter choices (e.g. 1 3 5): ").split()

    chosen_apps = [apps[i] for i in selected if i in apps]

    return chosen_apps

    #

    log(f"Detected hardware: {hardware_info}")
    return hardware_info
