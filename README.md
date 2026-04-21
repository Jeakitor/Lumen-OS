# Lumen OS

Lumen OS is a lightweight, student-focused Linux system designed to simplify installation and improve usability on low-spec hardware.

---

## Overview

This repository contains the development of a modular Linux installation system that allows users to configure their environment before installation. The system focuses on accessibility, safety, and flexibility.

---

## IB Computer Science Internal Assessment

This project was developed as part of an IB Computer Science Internal Assessment.

The IA submission corresponds to the core CLI-based installer located in:

- `installer/core/`

The following features are included in the IA scope:

- Hardware detection
- Profile-based installation (Minimal / Standard)
- Desktop environment selection
- Application selection
- Timezone and keyboard configuration
- User creation
- Disk setup (simulated)
- Simulation and execution modes
- Package management abstraction

Supporting documentation for the IA can be found in:

- `docs/installer_design.md`
- `docs/testing.md`
- `docs/evaluation.md`

---

## System Design

The installer follows a structured architecture:

User Input → Processing → Command Mapping → Execution

This design separates configuration logic from system execution, allowing flexibility and future expansion.

---

## Running the Installer

```bash
python -m installer.core.installer