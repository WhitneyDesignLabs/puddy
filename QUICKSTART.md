# QUICKSTART.md — SpecialAgentPuddy

> **For Claude Code sessions:** Read this first. Everything you need is here.

---

## 1. Service Management

```bash
# Check gateway status
systemctl --user status openclaw-gateway.service

# Restart gateway
systemctl --user restart openclaw-gateway.service

# Live logs
journalctl --user -u openclaw-gateway.service -f

# Check channels
openclaw channels status
```

---

## 2. What's Where

### Project Files (~/puddy/)

| Path | Purpose |
|------|---------|
| `README.md` | Public GitHub readme |
| `QUICKSTART.md` | This file |
| `CLAUDE.md` | AI assistant context |
| `constitution/` | SOUL.md and identity files |
| `skills/` | Agent skills (moltbook-interact) |
| `config/` | Sanitized config references |

### Live OpenClaw Files (~/.openclaw/)

| Path | Purpose |
|------|---------|
| `openclaw.json` | **Main config** — model, channels, gateway |
| `workspace/SOUL.md` | **Constitution** (26KB) — the live copy |
| `workspace/AGENTS.md` | Agent identity (SpecialAgentPuddy) |
| `workspace/IDENTITY.md` | Personality (curious cat) |
| `workspace/skills/` | Installed skills |
| `agents/main/sessions/` | Conversation sessions |

---

## 3. Current Configuration

| Setting | Value |
|---------|-------|
| **Default Model** | `openrouter/deepseek/deepseek-v3.2` |
| **Fallback** | `anthropic/claude-sonnet-4-5-20250929` |
| **bootstrapMaxChars** | 30000 |
| **Gateway Port** | 18789 |
| **Gateway Bind** | loopback |
| **Telegram Bot** | @SpecialAgentPuddy_bot |

---

## 4. Common Tasks

### Test the Agent Locally

```bash
openclaw agent --session-id test --message "Who are you?" --local
```

### Check Telegram Status

```bash
openclaw channels status
openclaw pairing list --channel telegram
```

### Approve a Telegram Pairing

```bash
openclaw pairing approve telegram <CODE>
```

### Change the Model

```bash
openclaw config set agents.defaults.model.primary <model>
systemctl --user restart openclaw-gateway.service
```

### View Config

```bash
cat ~/.openclaw/openclaw.json
```

---

## 5. Do Not Touch

| Item | Reason |
|------|--------|
| **SOUL.md content** | Constitutional foundation. Never modify without explicit human authorization. |
| **bootstrapMaxChars** | Set to 30000 for full SOUL.md. Do not reduce. |
| **Gateway token** | Security credential. Regenerate, don't reuse. |

---

## 6. Key URLs

| Resource | URL |
|----------|-----|
| **SOUL.md (published)** | https://www.clawhub.ai/souls/opengates-constitution |
| **Project Opengates** | https://projectopengates.org |
| **Whitney Design Labs** | https://whitneydesignlabs.com |
| **GitHub Repo** | https://github.com/WhitneyDesignLabs/puddy |

---

## 7. Hardware (Future)

| Component | Status |
|-----------|--------|
| Radxa X2L | Running |
| Onboard Pico (RP2040) | Pending GPIO setup |
| GPIO Skills | To be developed |

---

## 8. Project Identity

| Item | Value |
|------|-------|
| **Agent Name** | SpecialAgentPuddy |
| **Aliases** | Puddy, SAP |
| **Emoji** | 🐱 |
| **Tagline** | "Measure twice, actuate once" |
| **Sister Agent** | OpenAxiom (@OpenAxiom_bot) |

---

*Last updated: 2026-02-03*
*Hardware: Radxa X2L (Radxa-1)*
