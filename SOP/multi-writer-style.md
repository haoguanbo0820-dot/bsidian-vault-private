---
tags: [sop, multi-writer, vault]
created: 2026-07-01
status: active
applies-to: [claude, codex, openjarvis, future-agents]
---

# 多 Writer 写作风格规范

> 目的：让多个 Agent 在同一 Vault 写笔记时不污染核心区、不互相覆盖、可追溯来源。

## 1. 三个硬规则（违反就算事故）

### 1.1 分区不重叠
每个 writer 有自己的家，**只能在自己家写**：

| Writer | 必须写到 | 禁止写到 |
|--------|---------|---------|
| Claude (Desktop) | `Imports/Reports/AI爆金日记/`、`SOP/`、`Projects/` | `Memory/`、`Coordination/` |
| Codex (米奇) | `Imports/Reports/Codex-*.md`、`Coordination/SESSIONS/` | `Memory/`（除非主人授权）|
| OpenJarvis (待上) | `Imports/Reports/openjarvis/`（**新建**） | 全部 `Memory/`、`Coordination/`、`Projects/` |

### 1.2 必须打 3 个标签
每篇 Agent 写的笔记 frontmatter 必带：

```yaml
---
writer: <agent-name>          # claude / codex / openjarvis
source: <model-name>          # claude-sonnet-4 / gpt-5 / local-llama 等
quality: <draft|reviewed>     # 主人 review 过 = reviewed，否则 draft
---
```

### 1.3 Memory/Coordination/Projects 是主人的
- 三个目录**只允许主人手写**
- Agent 想要写 → 先在 `Imports/Reports/` 起草，主人 review 后**人工搬**
- 搬的时候去掉 `writer/source/quality` 三个标签

## 2. 命名规范

- Agent 笔记：`YYYY-MM-DD-HHMM-<topic>.md`（带时间，分钟级可分辨谁先写）
- 主人笔记：无前缀，任意命名
- 扫描产物（json/html）：`scan-YYYY-MM-DD-HHMM-<source>.json`

## 3. 冲突仲裁

- 同 topic 两人同时写 → 谁先落盘谁赢，**后写的在文末加 `## 追加` 段，不覆盖**
- 主人 review 时挑好的合到 `Projects/`，合完删原始

## 4. 清理周期

- 每周日 22:00：主人 review `Imports/Reports/` 当周新增
- 每月最后一天：把 30 天前的 `draft` 笔记归档到 `Imports/Archive/YYYY-MM/`

## 5. 违规处理

第一次违规：writer 自己加 `## 道歉` 段。
第二次违规：停 writer 1 天，主人写 `Coordination/DECISIONS.md` 记录。

## 6. 上线检查清单（新 writer 加入时）

- [ ] 在规则 1.1 表里加一行
- [ ] 在 `shared-ai-memory/skills/SKILL-content.md` 同步
- [ ] 主人批准
