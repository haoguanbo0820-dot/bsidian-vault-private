# Obsidian Vault - Agent Coordination Hub

这是郝冠的的 Obsidian 知识库，也是所有 AI Agent 的**共享记忆层**。

## 核心规则

1. **开始任何任务前** → 先读 [[Coordination/ACTIVE]]，确认没人在做同样的事
2. **任务完成后** → 写入 [[Coordination/LOGBOOK]]，更新 [[Coordination/ACTIVE]]
3. **做重要决策时** → 写入 [[Coordination/DECISIONS]]
4. **首次加入时** → 在 [[Coordination/AGENTS]] 登记自己

## 目录结构

```
Coordination/     ← Agent 协调层（共享记忆）
  AGENTS.md       ← Agent 注册表
  ACTIVE.md       ← 当前进行中的任务
  LOGBOOK.md      ← 操作日志
  DECISIONS.md    ← 关键决策记录
  SESSIONS/       ← 单个任务的详细笔记
Memory/           ← 持久化记忆（跨会话）
Projects/         ← 项目文档
SOP/              ← 标准操作流程
Imports/          ← 导入的业务资料
Daily/            ← 日记
```

## Agent 协调协议

```
开始任务:
  1. git pull (同步最新)
  2. 读 Coordination/ACTIVE.md
  3. 如果任务已有 Agent 在做 → 找别的事做
  4. 如果空闲 → 写入自己的任务

完成任务:
  1. 更新 Coordination/ACTIVE.md（移除/标记完成）
  2. 写 Coordination/LOGBOOK.md
  3. git add + commit + push
```
