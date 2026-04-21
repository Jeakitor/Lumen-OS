PACKAGE_MAP = {
    "browser": {
        "package": "firefox",
        "source": "pacman"
    },
    "code_editor": {
        "package": "visual-studio-code-bin",
        "source": "aur"
    },
    "media_player": {
        "package": "vlc",
        "source": "pacman"
    },
    "office_tools": {
        "package": "org.libreoffice.LibreOffice",
        "source": "flatpak"
    },
    "git": {
        "package": "git",
        "source": "pacman"
    }
}
DE_PACKAGES = {
    "xfce": "xfce4 xfce4-goodies",
    "kde": "plasma kde-applications",
    "gnome": "gnome"
}

def get_install_command(pkg, manager):
    if manager == "pacman":
        return f"sudo pacman -S --needed --noconfirm {pkg}"
    elif manager == "apt":
        return f"sudo apt install -y {pkg}"
    else:
        return f"# Unknown package manager for {pkg}"

#ARCH PACMAN USED ONLY FOR WHEN TESTING