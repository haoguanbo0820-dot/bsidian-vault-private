# Agent Roster

> 所有 AI Agent 的注册表。新 Agent 加入必须在此登记。

## 活跃 Agent

| Agent ID | 平台 | 模型 | CLAUDE.md | 关键配置 | 状态 |
|----------|------|------|-----------|---------|:--:|
| `claude-desktop` | Claude Desktop (Win) | Opus 4.6 | `D:\claude desktop\CLAUDE.md` | `~/.claude/settings.json` | 🟢 |
| `claude-code` | Claude Code CLI | Opus 4.6 | `G:/个人项目/AI工具/claude/CLAUDE.md` | CC Switch proxy | 🟢 |
| `codex` | Codex CLI (CC Switch) | MiniMax-M3 | `G:/个人项目/AI工具/codex/CLAUDE.md` | `AGENTS.md` + `shared-ai-memory/` | 🟢 |
| `hermes` | Hermes-Portable | MiniMax-M3 | `D:/OpenClaw-Hermes-Portable/CLAUDE.md` | `hermes-data/config.yaml` | 🟢 |

## Agent 能力矩阵

| 能力 | claude-desktop | claude-code | codex | hermes |
|------|:---:|:---:|:---:|:---:|
| 代码编写 | ✅ | ✅ | ✅ | ✅ |
| 代码审查 | ✅ | ✅ | ✅ | ⚠️ |
| Shell/Git | ✅ | ✅ | ✅ | ✅ |
| 文件读写 | ✅ | ✅ | ✅ | ✅ |
| Web 搜索 | ✅ | ✅ | ✅ | ✅ |
| 浏览器操作 | ✅ | ❌ | ❌ | ✅ |
| 深度推理 | ✅ | ✅ | ❌ | ❌ |
| 跨会话记忆 | ✅ | ❌ | ❌ | ✅ |
| WeChat 接入 | ❌ | ❌ | ❌ | ✅ |
| 后台自动化 | ❌ | ❌ | ❌ | ✅ |

## 接入状态

| Agent | Vault CLAUDE.md | ACTIVE.md 协议 | LOGBOOK 写入 | 自登记 |
|-------|:---:|:---:|:---:|:---:|
| claude-desktop | ✅ 2026-06-29 | ✅ | ✅ | ✅ |
| claude-code | ✅ 2026-06-29 | ✅ | ✅ | ✅ |
| codex | ✅ 2026-06-29 | ✅ | ✅ | ✅ |
| hermes | ✅ 2026-06-29 | ✅ | ✅ | ✅ |

## 新 Agent 接入流程

1. Fork & clone `git@gitee.com:haowenzhuo/obsidian-vault.git` 到本地
2. 在下面登记自己的 Agent ID / 平台 / 能力
3. 在本机 CLAUDE.md 中写入 vault 路径引用
4. 遵守 [[CLAUDE.md|协调协议]]
