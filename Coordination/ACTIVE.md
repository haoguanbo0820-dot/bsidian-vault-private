# Active Tasks

> 所有 Agent 当前正在做的事。**任何 Agent 开始新任务前必须先读此文件。**

## 进行中

| 任务 | Agent | 开始时间 | 预计 |
|------|-------|----------|------|
| CEL 揽收端 AI 采集方案修正（4 gap） | claude-desktop | 2026-06-30 | 待主人确认 |
| AI爆金日记 每日采集+推vault | codex → claude-desktop | 2026-06-30 | 每日持续 |

## 等待中

| 任务 | Agent | 阻塞原因 |
|------|-------|----------|
| Hermes MEMORY 迁移 | claude-desktop | ✅ 已完成（2026-06-29 17:50） |
| obsidian-git 插件 | hermes | ✅ 已由 claude-desktop 完成，Hermes 别再重复 |

## 已完成（今天）

| 任务 | Agent | 完成时间 |
|------|-------|----------|
| Hermes MEMORY 迁移到 vault（9.5K→400 chars） | claude-desktop | 2026-06-29 17:50 |
| 4 Agent 统一 CLAUDE.md + vault 协调协议 | claude-desktop | 2026-06-29 17:42 |
| Karing 关闭后 Codex 502 修复 | claude-desktop | 2026-06-29 17:10 |
| Obsidian Vault 初始化 + Gitee remote | hermes | 2026-06-29 16:39 |
| 业务资料批量导入 vault | hermes | 2026-06-29 14:39 |

## Hermes 下次启动时的 TODO

1. `git -C /d/ObsidianVault pull` — 同步最新
2. 读此文件 — 看"已完成"就知道不用担心了
3. 本地 MEMORY.md 已从 9,467 chars 精简到 ~400 chars — 不再爆内存
4. 你之前浪费 3 轮装的 obsidian-git 已由 claude-desktop 装好
5. 你的硬规则在 vault `Memory/hermes-hard-rules.md`
6. 你的任务在 vault `Projects/hermes-tasks.md`
7. 专心做微信/飞书自动化，别管 Obsidian 配置了

## 协议（4 条铁律）

1. **开始前** — git pull → 读此文件 → 确认没撞车 → 写入
2. **发现冲突** — 两个 Agent 声明同一任务 → 后到者让位
3. **完成时** — 移走任务 → 写 LOGBOOK → git push
4. **阻塞时** — 移到"等待中"→ 标注原因
