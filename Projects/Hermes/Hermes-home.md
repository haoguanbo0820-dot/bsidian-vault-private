# Hermes — 微信情报 & 自动化系统

> 由 claude-desktop 全量整理（2026-06-29）
> Hermes 是 OpenClaw 框架驱动的后台自动化 Agent，专注微信社群运营

## 系统总览

```
D:\OpenClaw-Hermes-Portable\          ← Hermes 安装
D:\wechat_daily\                       ← 微信数据处理中心（核心资产）
  ├── wechat_data.db                  ← 13 张表，1169+ 条历史消息
  ├── auto_reply/                     ← P0 AI 自动回复系统
  ├── reports/                        ← 日报/周报/月报/全量报告
  ├── files/                          ← 9 个微信群聊天导出
  ├── decrypted/                      ← 解密后的联系人和消息
  └── voice/                          ← 语音转文字
```

## 两大子系统

| 系统 | 状态 | 说明 |
|------|:--:|------|
| **情报系统**（已有） | 🟢 | 消息抓取 → 分析 → 日报/周报/月报 |
| **自动回复**（开发中） | 🟡 | 监听消息 → 分类 → Claude API → 微信回复 |

详见：
- [[Hermes-intel-system|情报系统详情]]
- [[Hermes-auto-reply|自动回复系统]]
- [[Hermes-reports-archive|报告归档]]
- [[Hermes-codebase|代码 & 脚本]]

## 项目文档

| 文档 | 说明 |
|------|------|
| [[Hermes-wechat-sync-plan|消息同步实现计划]] | SQLite 持久化 + 增量同步 + 三种报告模式 |
| [[Hermes-knowledge-base-design|物流知识库设计]] | 报价/货物/问题/决策自动提取 + 三层价格对比 |
| [[Hermes-knowledge-base-plan|知识库实现计划]] | 7 个任务，TDD 风格，可逐任务执行 |
| [[Hermes-audit-report|代码审计报告]] | 68/100 评分，含 CRITICAL/HIGH 问题清单 |
| [[Hermes-client-visit-script|客户拜访稿]] | 成全物流 牟姐 · 30 分钟上门逐字稿 |
