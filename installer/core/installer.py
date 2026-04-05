from installer.core.logger import setup_logger, log
from installer.core.hardware import detect_hardware
from installer.core.profiles import recommend_profile

def main():
    setup_logger()
    log("Installer started")
    print("Lumen OS Installer starting...")

    hardware = detect_hardware()

    for key, value in hardware.items():
        print(f"{key.upper()}: {value}")

    profile = choose_profile()
    
    if profile == "minimal":
        de = None
        apps = []
    else:
        de = choose_de()
        apps = choose_apps()

    print("\n=== Installation Summary ===")
    print(f"Profile: {profile}")
    print(f"Desktop Environment: {de}")
    print(f"Apps: {apps}")
    print("\n=== Detected Hardware ===\n")
    
    for key, value in hardware.items():
        print(f"{key.upper()}: {value}")

  
if __name__ == "__main__":
    main()
