# 🤖 AI Agent Infrastructure

> **Multi-LLM AI agent deployed on a Raspberry Pi — Discord-integrated, automation-driven, cloud-ready.**

[![Linux](https://img.shields.io/badge/OS-Linux%20(ARM64)-orange)]()
[![Node.js](https://img.shields.io/badge/Runtime-Node.js-green)]()
[![Python](https://img.shields.io/badge/Automation-Python-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)]()

---

## Overview

A production-style AI agent infrastructure running on a Raspberry Pi, integrating multiple large language models via OpenRouter, real-time Discord messaging, sensor data ingestion, and autonomous automation scripts. Designed with extensibility, observability, and reliability in mind — the same principles that power enterprise cloud services.

---

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   Discord   │◄───►│  OpenClaw    │◄───►│  OpenRouter  │
│  (Channel)  │     │  (Agent)     │     │  API         │
└─────────────┘     └──────┬───────┘     └──────┬───────┘
                           │                    │
                           │              ┌─────┴──────┐
                           │              │ DeepSeek V4 │
                           │              │ Grok 4.3    │
                           │              │ Gemini Flash│
                           │              │     Lite    │
                           │              └─────────────┘
                    ┌──────┴───────┐
                    │   systemd    │
                    │  (Service)   │
                    │  (Auto-start)│
                    └──────────────┘
                    ┌──────┴───────┐
                    │  Cron Jobs   │
                    │  (Scheduled  │
                    │   Tasks)     │
                    └──────────────┘
                    ┌──────┴───────┐
                    │  Python      │
                    │  Automation  │
                    │  Scripts     │
                    └──────────────┘
                    ┌──────┴───────┐
                    │  Tempest     │
                    │  Weather API │
                    │  Proton Mail │
                    └──────────────┘
```

---

## Key Features

### 🧠 Multi-LLM Orchestration
- Routes queries to **DeepSeek V4**, **Grok 4.3**, and **Gemini Flash Lite** via OpenRouter API
- Model routing based on task type and complexity
- Pluggable — swap or add models without infrastructure changes

### 💬 Discord Integration
- Real-time conversational interface
- Automated channel posting (weather reports, garden alerts)
- Direct message and group chat support

### 🌡️ Autonomous Monitoring
- **WeatherFlow Tempest** station integration — real-time temperature, wind, rain, solar radiation
- Cron-based garden watering recommendations using sensor data + plant lifecycle analysis
- Automated email alerts via Proton Mail API

### ⚙️ Infrastructure
- **Raspberry Pi (ARM64 Linux)** — low-power, always-on deployment
- **systemd** service management — auto-start, restart on failure
- **YAML-based configuration** — all settings in one place, easy to modify
- **Python automation scripts** — modular, testable, scheduled via cron

### 🔄 Version Control & Backup
- **Git-based** change tracking with automated daily backup
- Backup pipeline to remote GitHub repository
- Configuration version history for rollback safety

---

## Tech Stack

| Category | Technologies |
|---|---|
| **Runtime** | Node.js, Python |
| **LLM APIs** | OpenRouter (DeepSeek, Grok, Gemini) |
| **Integration** | Discord API, WeatherFlow Tempest REST API, Proton Mail |
| **Infrastructure** | Raspberry Pi OS (ARM64 Linux), systemd |
| **Configuration** | YAML, environment variables |
| **Automation** | Cron, Python scripting |
| **Version Control** | Git, GitHub |
| **Secrets Management** | Token-based auth, environment variable store |

---

## Skills Demonstrated

- **Cloud & Infrastructure**: Linux system administration, service orchestration, configuration management
- **AI/ML Integration**: LLM API consumption, model evaluation, prompt engineering
- **API Development**: REST API integration, token-based authentication, rate limit handling
- **Automation**: Scripted workflows, cron scheduling, event-driven architecture
- **DevOps**: Git workflow, CI/CD pipelines, backup automation
- **Monitoring**: Real-time sensor data ingestion, alert systems, cron-based health checks

---

## Why This Matters

This project demonstrates the ability to:

1. **Design and deploy** production-quality AI infrastructure from scratch
2. **Integrate multiple services** into a cohesive, reliable system
3. **Automate real-world workflows** using sensor data and AI processing
4. **Manage a Linux server** with proper service management, security, and backup practices
5. **Ship and maintain** a living system that runs 24/7

These are the same skills required for cloud engineering, AI operations, and infrastructure roles at any organization using modern AI tooling.

---

## Related

- [OpenClaw AI Framework](https://github.com/openclaw) — the agent platform powering this infrastructure
- [WeatherFlow Tempest](https://weatherflow.com/) — weather station hardware and API

---

*Built with curiosity, maintained with care — deployed on a Pi since 2025.*