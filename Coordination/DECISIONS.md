# Decisions Log

> 记录影响多个 Agent 或后续工作的决策。

---

## 2026-07-01

### D004: 多 Agent 模型分工配置（主人 2 次纠正后定稿）
- **决策者**: claude-desktop + 郝冠的
- **背景**: 主人纠正 3 次模型定位：M3=Coding 订阅量大管饱 / DeepSeek Pro=按量有成本 / GLM 5.2=限流限量专项。最终方案：M3 给 Coding 类 agent（Claude Desktop/Hermes/Marvis）/ DeepSeek Pro 给日常杂活省钱场景 / GLM 5.2 留给 Codex GUI 触发时专项 / Trae CN 走火山豆包包月
- **决策**: Claude Desktop env 已配 M3 + DeepSeek Pro + GLM 5.2 + 智谱 4 个备援 API key。Hermes/Marvis/Codex/Trae CN 4 个 handoff 已写，等它们启动时按新配置加载
- **影响**: 主人包年 Coding 订阅"量大管饱"充分利用；DeepSeek 按量不滥用；GLM 5.2 限流留给最难的（Codex GUI 触发时）
- **配置**: [[Coordination/ModelConfig-2026-07-01]]
- **Handoff**: [[Coordination/HANDOFFS/ModelConfig-{Hermes,Marvis,Codex,Trae-CN}-2026-07-01]]

### D003: 多 Agent 分工调度方案 B（任务队列 + 抢单机制 v2）
- **决策者**: claude-desktop + 郝冠的
- **背景**: 主人授权"我是大脑"分派活给其他 agent；v1 方案 A 有 3 个根本缺陷（单点故障/我超载/被动 handoff）
- **决策**: 采用方案 B——任务队列（QUEUE.json）+ agent 抢单（required_skills 匹配）+ 心跳（HEARTBEAT.md）+ 冲突自动检测（原子写）
- **影响**: 所有 agent 启动后主动扫队列抢单，不再被动等 handoff；我挂了 → 主人 30 分钟后接管（看心跳）；其他 agent 挂了 → 我兜底
- **入队权**: 主人 + claude-desktop 直接入队；其他 agent 写 QUEUE.suggested.json 建议，审核转正
- **汇报**: 触发式（4 种触发：完成/agent 挂/撞车/需主人 GUI）
- **文档**: [[分工设计-2026-07-01]]

---

## 2026-06-29

### D001: 使用 Obsidian Vault 作为 Agent 协调层
- **决策者**: claude-desktop + 郝冠的
- **背景**: 多个 AI Agent（Claude Desktop、Hermes、Codex）各自工作，互不知情
- **决策**: 用 `/d/ObsidianVault/Coordination/` 目录作为共享记忆层
- **影响**: 所有 Agent 启动任务前必须读取 ACTIVE.md，完成后必须写入 LOGBOOK.md
- **待定**: Hermes 自动化写入协调文件的方式（需要配置 skill 或 cron）

### D002: MiniMax API 绕过系统代理
- **决策者**: claude-desktop
- **背景**: Karing 关闭后系统代理残留导致 CC Switch 连接 MiniMax 超时
- **决策**: 在 Windows ProxyOverride + 环境变量 NO_PROXY 中加入 `api.minimaxi.com`
- **影响**: MiniMax 流量永远直连，不经过 Karing。后续其他国内 API 可参考此方案
