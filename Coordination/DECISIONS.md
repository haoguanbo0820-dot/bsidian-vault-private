# Decisions Log

> 记录影响多个 Agent 或后续工作的决策。

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
