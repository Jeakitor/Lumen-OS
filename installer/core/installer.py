from installer.core.logger import setup_logger, log
from installer.core.hardware import detect_hardware

def main():
    setup_logger()
    log("Installer started")
    print("Lumen OS Installer starting...")
    
    hardware=detect_hardware()
    print("Detected Hardware:")
    for key, value in hardware.items():
        print(f" {key}; {value}")
    

if __name__ == "__main__":
    main()
