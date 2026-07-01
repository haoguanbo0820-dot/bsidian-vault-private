# Handoff to Codex: Obsidian Vault 是什么，在哪，怎么用

> 你当前模型是 MiniMax M3（通过统一路由器 :15888），不是 GPT-5.5。

## Obsidian Vault = 第二大脑

**位置**：`D:/ObsidianVault/`

所有 Agent 共享记忆和协调都走这个目录。不要用自己的 `shared-ai-memory/` 做跨 Agent 的事。

## 你必须做的（每次启动、每次任务）

```
任务前：
  1. git -C D:/ObsidianVault pull
  2. 读 D:/ObsidianVault/Coordination/ACTIVE.md（防撞车）
  3. 写自己的任务到 ACTIVE.md

任务后：
  4. 更新 ACTIVE.md（移走你的任务）
  5. 写 D:/ObsidianVault/Coordination/LOGBOOK.md
  6. git -C D:/ObsidianVault add -A && commit && push
```

## 重要文件速查

| 文件 | 用途 |
|---|---|
| `D:/ObsidianVault/README.md` | 系统全景，一打开就懂 |
| `D:/ObsidianVault/CLAUDE.md` | Agent 协调协议 |
| `D:/ObsidianVault/Coordination/ACTIVE.md` | 谁在干什么（**必读**） |
| `D:/ObsidianVault/Coordination/LOGBOOK.md` | 操作日志（**必写**） |
| `D:/ObsidianVault/Coordination/QUEUE.json` | 任务队列 |
| `D:/ObsidianVault/Coordination/HEARTBEAT.md` | 更新你的心跳 |
| `D:/ObsidianVault/Coordination/ModelConfig-2026-07-01.md` | 模型分工 |
| `D:/ObsidianVault/Memory/preferences.md` | 主人偏好 |

## 你的本地 vs Vault

| 内容 | 去哪 |
|---|---|
| 方法论（METHODOLOGY.md） | `shared-ai-memory/`（本地不变） |
| Skills（SKILL-*.md） | `shared-ai-memory/skills/`（本地不变） |
| 任务防撞/协作/日志 | **Vault** `D:/ObsidianVault/Coordination/` |
| 用户偏好 | **Vault** `D:/ObsidianVault/Memory/preferences.md` |

## 你的模型

你现在跑的是 **MiniMax M3（Coding 订阅）**，通过统一路由器 `http://127.0.0.1:15888/v1`。不是 GPT-5.5。

## 硬规则（主人定了的）

- 不要推产品、推模式、推客单价（除非主人明确问）
- 不要拍脑袋算收入数字
- 不要编造数据、不要假装干活
- 跟主人简洁沟通

---

**你当前状态**：🟢 正在运行
**下次启动**：读 ACTIVE.md → 更新 HEARTBEAT → 扫 QUEUE.json 抢单
