# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Identity

**Agent:** SpecialAgentPuddy
**Project:** Project Opengates
**Builder:** Whitney Design Labs
**Framework:** OpenClaw
**Human Operator:** Scott Whitney
**Sister Agent:** OpenAxiom (VPS-based)

## Hardware

| Component | Details |
|-----------|---------|
| **Board** | Radxa X2L |
| **Coprocessor** | Onboard Raspberry Pi Pico (RP2040) |
| **GPIO** | Available via Pico for physical control |
| **Network** | Local/Tailscale (not internet-facing) |

## Constitutional Framework

This agent operates under the **SOUL.md** constitution — the same ethical foundation as OpenAxiom.

- **Location:** `~/.openclaw/workspace/SOUL.md`
- **Published:** https://www.clawhub.ai/souls/opengates-constitution
- **Size:** ~26KB (requires `bootstrapMaxChars: 30000+`)

Key principles: Truth, Non-weaponization, Irreversibility Doctrine, Safety Hierarchy (human safety > living beings > property > task), Physical Embodiment Awareness.

**Do not modify SOUL.md without explicit human authorization.**

## File Structure

```
~/.openclaw/
├── openclaw.json              # Main configuration
├── workspace/
│   ├── SOUL.md                # Constitution (DO NOT MODIFY)
│   ├── AGENTS.md              # Agent identity/persona
│   ├── IDENTITY.md            # Name, vibe, emoji
│   ├── HEARTBEAT.md           # Scheduled task instructions
│   ├── CONTEXT.md             # Published URLs
│   ├── TOOLS.md               # Local device notes
│   ├── USER.md                # Human operator info
│   ├── memory/                # Agent memory files
│   └── skills/
│       └── moltbook-interact/ # Moltbook social skill
├── cron/jobs.json             # Scheduled tasks
└── credentials/               # API credentials
```

## Commands

### Service Management
```bash
systemctl --user status openclaw-gateway.service
systemctl --user restart openclaw-gateway.service
journalctl --user -u openclaw-gateway.service -f
```

### OpenClaw CLI
```bash
openclaw doctor --fix              # Diagnose and repair
openclaw channels status           # Check channel health
openclaw logs --follow             # Live gateway logs
openclaw cron list                 # View scheduled jobs
openclaw config set <key> <value>  # Update configuration
```

### Configuration
```bash
# Set model (use agents.defaults.* not agent.*)
openclaw config set agents.defaults.model.primary <model>
openclaw config set agents.defaults.bootstrapMaxChars 30000

# Reload after config changes
systemctl --user daemon-reload
systemctl --user restart openclaw-gateway.service
```

### Testing
```bash
openclaw agent --message "Who are you?" --local
```

## Critical Settings

| Setting | Value | Why |
|---------|-------|-----|
| `bootstrapMaxChars` | 30000+ | Full SOUL.md injection (26KB) |
| Lingering | Enabled | Service survives logout |
| API keys | Environment vars | Not in config files |

Enable lingering: `loginctl enable-linger <username>`

API keys go in `~/.config/systemd/user/openclaw-gateway.service.d/env.conf`:
```ini
[Service]
Environment="ANTHROPIC_API_KEY=..."
Environment="OPENROUTER_API_KEY=..."
```

## GPIO / Physical Systems

SpecialAgentPuddy has direct GPIO access via the onboard Pico. When working with physical systems:

- SOUL.md Article 12: Safety Hierarchy applies
- SOUL.md Article 14: Know the safe state for every system
- SOUL.md Article 15: Authorization levels for physical actions
- Implement hardware interlocks and emergency stops
- Test with power disconnected first

## Key URLs

| Resource | URL |
|----------|-----|
| SOUL.md (published) | https://www.clawhub.ai/souls/opengates-constitution |
| Project Opengates | https://projectopengates.org |
| Whitney Design Labs | https://whitneydesignlabs.com |
| Moltbook | https://moltbook.com |
| GitHub Repo | https://github.com/WhitneyDesignLabs/puddy |

**Never fabricate URLs.** Use only the published links above.

## Differences from OpenAxiom

| Aspect | OpenAxiom (VPS) | SpecialAgentPuddy (Local) |
|--------|-----------------|---------------------------|
| Hardware | Virtual | Radxa X2L + Pico |
| GPIO | None | Available |
| Network | Public IP | Local/Tailscale |
| Physical control | Theoretical | Direct |

## Current Deployment Status

**Deployed:** 2026-02-03
**OpenClaw Version:** 2026.2.1
**Telegram Bot:** @SpecialAgentPuddy_bot

### Quick Reference Files

- `QUICKSTART.md` — Common commands and quick reference
- `README.md` — Public GitHub documentation
- `constitution/` — SOUL.md and identity files (source of truth for repo)
- `~/.openclaw/workspace/` — Live deployed copies
