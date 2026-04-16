from installer.core.logger import setup_logger, log
from installer.core.hardware import detect_hardware
#3
import subprocess
#
from installer.core.packages import PACKAGE_MAP, DE_PACKAGES
import getpass



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
        return []
    else:
        return selected

def create_user():
    print("\n=== User Setup ===")

    username = input("Enter username: ").strip()

    while True:
        password = getpass.getpass("Enter password: ").strip()
        confirm = getpass.getpass("Confirm password: ").strip()

        if password == confirm:
            break
        else:
            print("Passwords do not match. Try again.")

    print("\nUser type:")
    print("1. Student (restricted)")
    print("2. Admin (full access)")

    choice = input("Choose user type (1-2): ").strip()
    user_type = "admin" if choice == "2" else "student"

    return {
        "username": username,
        "password": password,
        "type": user_type
    }
###
def choose_timezone():
    print("\n=== Timezone Setup ===")

    print("Common options:")
    print("1. Asia/Kolkata")
    print("2. Europe/London")
    print("3. America/New_York")
    print("4. Custom")

    choice = input("Choose option (1-4): ").strip()

    if choice == "1":
        return "Asia/Kolkata"
    elif choice == "2":
        return "Europe/London"
    elif choice == "3":
        return "America/New_York"
    else:
        #timezones fetch lines:
        zones = subprocess.check_output(
            "timedatectl list-timezones",
            shell=True
        ).decode().split("\n")

        while True:
            tz = input("Enter custom timezone: ").strip()

            if tz in zones:
                return tz
            else:
                print("Invalid timezone. Try again.")

def get_install_command(pkg, source):
    if source == "pacman":
        return f"sudo pacman -S --needed --noconfirm {pkg}"
    elif source == "aur":
        return f"yay -S --noconfirm {pkg}"
    elif source == "flatpak":
        return f"flatpak install -y flathub {pkg}"
    else:
        return f"# Unknown source for {pkg}"

#
#
def simulate_install(profile, de, apps, user, timezone, execute=False):
    print("\n=== Installation Plan ===")

    # Base system
    print("Installing base system...")

    #USERS
    print(f"Creating user: {user['username']}")
    print(f"User type: {user['type']}")
    #

    print(f"Setting timezone: {timezone}")            
    
    # Profile handling
    if profile == "minimal":
        print("Minimal setup: no extra packages")

    # Desktop Environment
    if de:
        pkg = DE_PACKAGES.get(de)
        if pkg:
            cmd = f"sudo pacman -S --needed --noconfirm {pkg}"
    
            if execute:
                subprocess.run(cmd, shell=True)
            else:
                print(f" - {cmd}")
    # Applications
    if apps:
        print("Installing selected applications:")
        for app in apps:
            data = PACKAGE_MAP.get(app)
    
            if data:
                pkg = data["package"]
                src = data["source"]
                cmd = get_install_command(pkg, src)
    
                if execute:
                    subprocess.run(cmd, shell=True)
                else:
                    print(f" - {cmd}")
            else:
                print(f" - Unknown app: {app}")
    else:
        print("No additional applications selected")
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
    
    user = create_user()
    timezone = choose_timezone()
        
    print("\n------------------------------")
    print("\n=== Installation Summary ===")
    print(f"Profile: {profile}")
    print(f"Desktop Environment: {de}")
    print(f"Apps: {apps}")
    print(f"User: {user['username']} ({user['type']})")
    print(f"Timezone: {timezone}")

    ###
    print("\n=== Commands to be executed ===")
    
    # Preview DE install
    if de:
        from installer.core.packages import DE_PACKAGES
        pkg = DE_PACKAGES.get(de)
        if pkg:
            print(f"sudo pacman -S --needed --noconfirm {pkg}")
    
    # Preview app installs
    for app in apps:
        data = PACKAGE_MAP.get(app)
        if data:
            cmd = get_install_command(data["package"], data["source"])
            print(cmd)

    ###

    
    log(f"Final selection → Profile: {profile}, DE: {de}, Apps: {apps}")

    #
    print("\nChoose installation mode:")
    print("1. Simulate (safe)")
    print("2. Execute (experimental)")
    
    mode = input("Enter choice (1-2): ").strip()
        
    if mode == "2":
        confirm = input("\n This will run real install commands. Continue? (y/n): ").lower()
        if confirm == "y":
            simulate_install(profile, de, apps, user, timezone, execute=True)
        else:
            print("Execution cancelled.")
    else:    
        simulate_install(profile, de, apps, user, timezone, execute=False)
    #
  
if __name__ == "__main__":
    main()
