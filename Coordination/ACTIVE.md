# Active Tasks

> 所有 Agent 当前正在做的事。**任何 Agent 开始新任务前必须先读此文件。**

## 进行中

| 任务 | Agent | 开始时间 | 预计 |
|------|-------|----------|------|
| Agent 协调系统搭建（收尾） | claude-desktop | 2026-06-29 17:35 | 已完成，交棒 hermes |
| **🧵 接手 claude-desktop 的工作** | **hermes** | **2026-06-29 17:42** | **读 handoff → 迁移 MEMORY → 确认** |

## 等待中

| 任务 | Agent | 阻塞原因 |
|------|-------|----------|
| obsidian-git 插件安装 | hermes | ❌ 已由 claude-desktop 完成（17:30），Hermes 别再重复做 |

## 已完成（今天）

| 任务 | Agent | 完成时间 |
|------|-------|----------|
| 4 Agent 统一 CLAUDE.md + vault 协调协议 | claude-desktop | 2026-06-29 17:42 |
| Karing 关闭后 Codex 502 修复 | claude-desktop | 2026-06-29 17:10 |
| Obsidian Vault 初始化 + Gitee remote | hermes | 2026-06-29 16:39 |
| 业务资料批量导入 vault | hermes | 2026-06-29 14:39 |

## 📨 未读 Handoff

- **[handoff-claude-to-hermes-20260629.md](SESSIONS/handoff-claude-to-hermes-20260629.md)** ← Hermes 先读这个！

## 协议（4 条铁律）

1. **开始前** — 读此文件 → 确认没人做 → 写入
2. **发现冲突** — 两个 Agent 声明同一任务 → 后到者让位
3. **完成时** — 移走任务 → 写 LOGBOOK → git push
4. **阻塞时** — 移到"等待中"→ 标注原因 → 告诉用户
