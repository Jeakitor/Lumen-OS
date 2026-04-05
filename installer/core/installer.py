from installer.core.logger import setup_logger, log
from installer.core.hardware import detect_hardware
#3
from installer.core.packages import PACKAGE_MAP

def choose_profile():
    print("\nChoose installation profile:")
    print("1. Minimal (advanced users only, choose only if you know what you're doing)")
    print("2. Standard (recommended)")

    while True:
        choice = input("Enter choice (1-2): ").strip()

        if choice == "1":
            print("\nMinimal install selected.")
            print("This will install a barebones system.")
            confirm = input("Are you sure? (y/n): ").strip().lower()
            if confirm == "y":
                return "minimal"
            else:
                return "standard"

        elif choice == "2":
            return "standard"

        else:
            print("Invalid input. Please enter 1 or 2.")


def choose_de():
    print("\nChoose Desktop Environment:")
    print("1. XFCE  - Lightweight and simple")
    print("2. KDE   - Modern and customizable")
    print("3. GNOME - Clean and minimal")

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        return "xfce"
    elif choice == "2":
        return "kde"
    elif choice == "3":
        return "gnome"
    else:
        print("Invalid choice. Defaulting to XFCE.")
        return "xfce"


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

    choices = input("Enter choices (e.g. 1 3 5): ").split()

    selected = [apps[c] for c in choices if c in apps]

    if not selected:
        print("No apps selected.")
        return[]
    else:
        return selected

#
def simulate_install(profile, de, apps):
    print("\n=== Installation Plan ===")

    # Base system
    print("Installing base system...")

    # Profile handling
    if profile == "minimal":
        print("Minimal setup: no extra packages")

    # Desktop Environment
    if de:
        if de == "xfce":
            print("Installing XFCE desktop...")
        elif de == "kde":
            print("Installing KDE desktop...")
        elif de == "gnome":
            print("Installing GNOME desktop...")

    # Applications
    if apps:
        print("Installing selected applications:")
        for app in apps:
            data = PACKAGE_MAP.get(app)

            if data:
                pkg = data["package"]
                src = data["source"]
                print(f" - Installing {pkg} via {src}")
            else:
                print(f" - Unknown app: {app}")
    else:
        print("No additional applications selected")

    print("\nInstallation simulation complete.")
#

def main():
    setup_logger()
    log("Installer started")
    print("Lumen OS Installer starting...")

    hardware = detect_hardware()

    print("\n=== Detected Hardware ===")
    for key, value in hardware.items():
        print(f"{key.upper()}: {value}")

    profile = choose_profile()
    
    if profile == "minimal":
        de = None
        apps = []
    else:
        de = choose_de()
        apps = choose_apps()

    print("\n------------------------------")
    print("\n=== Installation Summary ===")
    print(f"Profile: {profile}")
    print(f"Desktop Environment: {de}")
    print(f"Apps: {apps}")

    log(f"Final selection → Profile: {profile}, DE: {de}, Apps: {apps}")

    #
    simulate_install(profile, de, apps)
    #
  
if __name__ == "__main__":
    main()
