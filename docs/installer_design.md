# Installer Design

## 1. Overview
Explain purpose of installer

## 2. System Architecture
User → Logic → Execution

## 3. Hardware Detection
(you already started this)

## 4. User Interaction
Profile, DE, Apps

## 5. Environment Configuration
Timezone, Keyboard

## 6. User Management
create_user()

## 7. Package Management
PACKAGE_MAP explanation

## 8. Execution System
simulate vs execute

## 9. Safety Design
Why simulation exists

## 10. Limitations
(no real partitioning etc.)##HARDWARE DETECITON

The installer performs read only hardware detection to gether CPU, RAM, and system architecture information. This data is later used to guide installation profile selection and ensure suitability for for low-spec systems.
