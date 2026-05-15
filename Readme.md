# Intelligent Laptop Diagnostic Expert System Using Fuzzy Logic

An intelligent fuzzy logic expert system designed to diagnose laptop performance and hardware-related issues using context-aware fuzzy inference.

Built with:
- Python
- scikit-fuzzy
- Streamlit
- NumPy

---

# Project Overview

This project simulates how a human technical expert diagnoses laptop issues.

Instead of using traditional binary logic, the system applies fuzzy logic to evaluate uncertain and overlapping conditions such as:
- CPU usage
- RAM usage
- Temperature
- Disk health
- Boot performance
- Battery condition

The system dynamically adapts its behavior depending on:
- Laptop type
- Operating system
- Usage scenario
- Brand profile

---

# Features

## Fuzzy Logic Diagnostic Engine
- 27 fuzzy rules
- Trapezoidal membership functions
- Context-aware threshold adjustment

## Dynamic Context Profiles
Supports:
- Gaming laptops
- Office laptops
- Ultrabooks
- Professional devices

Operating systems:
- Windows
- Linux
- macOS

Usage modes:
- Gaming
- Office
- Development
- Design

---

# System Outputs

The system evaluates:

| Output | Description |
|---|---|
| Performance | Overall laptop performance |
| Overheating Risk | Thermal condition |
| Stability | System stability |
| Storage Issue | Disk/storage problems |
| Battery Issue | Battery condition |
| Boot Issue | Startup problems |

All outputs are normalized between:
0 → 100

---

# Project Architecture

The project follows a modular 5-layer architecture:

```text
Rules Layer
    ↓
Context Layer
    ↓
Membership Layer
    ↓
Inference Engine
    ↓
Recommendation System