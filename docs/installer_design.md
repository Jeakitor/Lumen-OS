# Installer Design

## 1. Overview

The Lumen OS installer is a modular command-line system designed to guide users through the process of configuring a lightweight Linux environment. It focuses on simplicity, safety, and flexibility, allowing users to customize their system before installation.

The installer is intended for students and educational environments where ease of use and performance on low-spec hardware are critical.

---

## 2. System Architecture

The installer follows a layered design approach:

User Input → Processing → System Mapping → Execution

- **User Input Layer** collects configuration choices (profile, desktop environment, applications, etc.)
- **Processing Layer** validates and organizes the data
- **System Mapping Layer** translates selections into system-level commands
- **Execution Layer** applies or simulates installation steps

This separation improves maintainability and reduces system risk.

---

## 3. Hardware Detection

The system performs read-only hardware detection to gather information such as CPU, RAM, and system architecture.

This is implemented using system commands (e.g., `lscpu`, `/proc/meminfo`) and allows the installer to:
- understand system capabilities
- support future optimization decisions

The detection process does not modify the system and is used only for informational purposes.

---

## 4. Installation Profiles

The installer provides predefined installation profiles:

- **Minimal**: barebones system for advanced users
- **Standard**: includes additional components for general use

This allows users to choose between performance-focused and feature-rich setups.

---

## 5. Desktop Environment Selection

Users can select a desktop environment during installation:

- XFCE (lightweight)
- KDE (feature-rich)
- GNOME (modern interface)

Each option is mapped to specific package groups, enabling flexibility without requiring manual configuration.

---

## 6. Application Selection System

The installer allows users to choose applications based on their needs.

Applications are managed using a mapping system:

- Each app is linked to a package name
- Each package is mapped based on the detected package manager (e.g., apt, pacman), allowing cross-distribution compatibility.

This abstraction allows the system to support multiple package sources without changing core logic.

---

## 7. Environment Configuration

The installer includes environment setup options:

- **Timezone selection**
- **Keyboard layout selection**

Timezone input is validated against system-provided data to ensure correctness.

These settings ensure the system is ready for immediate use after installation.

---

## 8. User Management

The installer supports user creation with:

- username input
- password confirmation (hidden input)
- user role selection (student/admin)

Password input is handled securely using hidden input methods to prevent exposure in the terminal.

---

## 9. Disk Setup (Simulated)

The system includes a disk configuration step:

- Automatic partitioning (simulated)
- Manual option (not implemented)

This feature is included to reflect real-world installation workflows while avoiding risk during development.

---

## 10. Command Mapping and Execution

User selections are translated into system commands using a mapping system.

Example:
- Desktop environments → package groups
- Applications → install commands

The system supports two modes:

- **Simulation Mode**: displays commands without executing them
- **Execution Mode**: runs actual system commands

This ensures safety during testing and development.

---

## 11. Safety Design

A key design feature is the inclusion of a simulation mode.

This allows users to:
- preview installation steps
- verify configurations
- avoid unintended system changes

This improves usability and reduces risk.

---

## 12. Limitations

The current system has several limitations:

- No graphical interface (CLI only)
- Disk partitioning is simulated only
- No ISO integration yet
- Limited automation for full OS deployment

These limitations are acceptable within the scope of the project and allow for future expansion.

---

## 13. Future Improvements

Planned enhancements include:

- Text-based user interface (TUI)
- Graphical installer (GUI)
- Full disk partitioning support
- Custom desktop environment configurations
- ISO-based installation system

---

## 14. Design Justification

The system was designed to prioritize:

- usability for students
- performance on low-spec hardware
- modularity for future development

By separating system logic from user interaction, the installer remains flexible, maintainable, and scalable.
