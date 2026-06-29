# Obsidian Vault — Agent 共享记忆层

> 这是郝冠的的知识库，也是**所有 AI Agent 的单一真相源**。
>
> 4 个 Agent 协调工作：Claude Desktop / Claude Code / Codex / Hermes

## 每个 Agent 必须遵守（不管什么任务）

```
任务前:
  1. git -C /d/ObsidianVault pull (同步最新)
  2. 读 Coordination/ACTIVE.md (防撞车)
  3. 如果有 Agent 已在做 → 报告，不抢活
  4. 如果空闲 → 写入自己的任务 + Agent ID

任务后:
  1. 更新 Coordination/ACTIVE.md
  2. 写入 Coordination/LOGBOOK.md
  3. 重要决策 → Coordination/DECISIONS.md
  4. git -C /d/ObsidianVault add -A && commit -m "agent(id): 做了什么" && push
```

## 四个 Agent

| Agent ID | 平台 | 模型 | CLAUDE.md 位置 | 专长 |
|----------|------|------|---------------|------|
| `claude-desktop` | Claude Desktop | Opus 4.6 | `D:\claude desktop\CLAUDE.md` | 开发/架构/运维 |
| `claude-code` | Claude Code CLI | Opus 4.6 | `G:/个人项目/AI工具/claude/CLAUDE.md` | 代码编写/调试 |
| `codex` | Codex CLI (CC Switch) | MiniMax-M3 | `G:/个人项目/AI工具/codex/CLAUDE.md` | 代码审查/自动修复 |
| `hermes` | Hermes-Portable | MiniMax-M3 | `D:/OpenClaw-Hermes-Portable/CLAUDE.md` | 自动化调度/微信 |

## 目录结构

```
Coordination/     ← Agent 协调层（所有 Agent 读写）
  AGENTS.md       ← Agent 注册表（新 Agent 必须先登记）
  ACTIVE.md       ← 谁在做什么（任务前必读 !）
  LOGBOOK.md      ← 操作日志（任务后必写）
  DECISIONS.md    ← 影响多个 Agent 的决策
  SESSIONS/       ← 任务详细记录
Memory/           ← 用户偏好（权威源）
Projects/         ← 项目文档
SOP/              ← 标准操作流程
Imports/          ← 业务资料
Daily/            ← 日记
```

## Agent 不能做的事

- ❌ 不读 ACTIVE.md 就接任务
- ❌ 完成后不写 LOGBOOK.md
- ❌ 覆盖另一个 Agent 的活跃任务
- ❌ git push 之前不先 pull
