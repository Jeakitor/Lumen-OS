# Lumen OS

Lumen OS is a lightweight, student-focused Linux system designed to simplify installation and improve usability on low-spec hardware.

---

## Overview

This repository contains the development of a modular Linux installation system that allows users to configure their environment before installation. The system focuses on accessibility, safety, and flexibility.

---

## IB Computer Science Internal Assessment

This project was developed as part of an IB Computer Science Internal Assessment.

The IA submission corresponds to the CLI-based installer contained in the `final-ia` branch of this repository.

Within that branch, the relevant components are:

- `installer/core/` — Core installer logic
- `docs/` — Design, testing, and evaluation documentation

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

The IA version reflects a stable implementation of the installer at the time of submission.

---

## System Design

The installer follows a structured architecture:

User Input → Processing → Command Mapping → Execution

This design separates configuration logic from system execution, allowing flexibility and future expansion.

---

## Running the Installer

```bash
python -m installer.core.installer