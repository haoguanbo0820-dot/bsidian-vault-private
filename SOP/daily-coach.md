# 每日教练协议 (Daily Coach)

> 复用度: ⭐⭐⭐⭐⭐ (每天用)
> 来源: `G:/个人项目/AI工具/codex/shared-ai-memory/DAILY-COACH-PROTOCOL.md`
> 维护人: Hermes Agent

## 目的

每天自动采集多源数据 → 分析 → 生成建议 → 推送给主人

## 触发

- 时间: 每天早上 (主人起床后)
- 数据源: 抖音兴趣追踪 / 微信群消息 / TMS 数据 / 朋友圈

## 流程

1. **采集**: `daily-observe.ps1` 跑多源抓取
2. **存储**: `observations/YYYY-MM-DD.md`
3. **分析**: 主人读后,Agent 接收反馈
4. **建议**: 写进 `GROWTH.md` 进度更新

## 已有组件

- `shared-ai-memory/GROWTH.md` - 成长日志
- `shared-ai-memory/DAILY-COACH-PROTOCOL.md` - 协议原文
- `shared-ai-memory/daily-observe.ps1` - 每日数据采集脚本
- `shared-ai-memory/douyin-tracker.ps1` - 抖音兴趣追踪
- `shared-ai-memory/observations/` - 每日观察目录

## 关键问题(待主人确认)

- 报告用什么格式推送?(微信 / 邮件 / 飞书)
- 多少字算"合适"?
- 什么时候复盘?(周末?每月?)

## 历史使用

- 2026-06-13: 系统上线
- 2026-06-15: 与 TMS 集成
- 待 Hermes 接管
