# Lumen OS

A lightweight, student-focused Linux distribution designed to provide a simple, efficient, and customizable experience on low-spec hardware.

---

## --Project Goal

Lumen OS aims to make Linux more accessible to students by reducing complexity, improving performance on older systems, and allowing users to tailor their environment based on their needs.

---

## --Key Features

- Lightweight and optimized for low-spec hardware
- Student-focused system design
- Customizable installation process
- Desktop environment selection (XFCE, KDE, GNOME)
- Application selection during setup
- Secure user configuration
- Timezone and keyboard setup
- Safe installation simulation mode

---

## --Installer System

Lumen OS includes a modular CLI-based installer that allows users to:

- Configure system settings before installation
- Preview installation steps safely
- Execute installation based on selected options

This ensures flexibility while maintaining system stability.

---

## --Design Approach

The system follows a modular architecture:

User Input → Processing → System Mapping → Execution

This allows:
- safer installation workflows
- easier customization
- future expansion (TUI/GUI support)

---

## --Current Status

This project is in active development. Core installer functionality has been implemented and tested.

---

## --Running the Installer (Development)

```bash
python -m installer.core.installer
