from installer.core.logger import setup_logger, log
from installer.core.hardware import detect_hardware
from installer.core.profiles import recommend_profile

def main():
    setup_logger()
    log("Installer started")
    print("Lumen OS Installer starting...")
    
    hardware=detect_hardware()
    print("Detected Hardware:")
    for key, value in hardware.items():
        print(f" {key}; {value}")

    profile = recommend_profile(hardware)
    
    print(f"Recommended installation profile [profile]")
    log(f"Profile selected: [profile]")

if __name__ == "__main__":
    main()
