# Hermes 任务看板

> 从 `G:/个人项目/AI工具/codex/shared-ai-memory/TASK-Hermes.md` 同步（2026-06-29）
> 所有 Agent 都可以看到 Hermes 的任务进度

## 当前使命

**微信社群自动化 → 变现**

## 任务清单

### 自动化接入

| 优先级 | 任务 | 状态 | 备注 |
|--------|------|:--:|------|
| 🔴 P0 | 配置微信消息监听 | ⬜ | 捕获所有群聊消息 |
| 🔴 P0 | 飞书日报推送 | ⬜ | 每日 9:00 推送到飞书群 |
| 🟡 P1 | cron 定时任务 | ⬜ | 每小时汇总群消息 |
| 🟡 P1 | WhatsApp 桥接确认 | ⬜ | 检查可用性 |

### 接入渠道

- ✅ 微信桥（需确认活跃）
- ✅ 飞书桥（FEISHU_HOME_CHANNEL: oc_bd977e825b360772c0c5a1974081f355）
- ⚠️ WhatsApp（目录存在，待测试）

### 技能（已启用）

social-media, software-development, research, productivity, notion, github

### 心跳协议

- 每小时读取 vault `Coordination/ACTIVE.md`
- 所有任务进度写入 vault `Coordination/LOGBOOK.md`
- 遇到阻塞 @到 Coordination/ACTIVE.md 等待中

### 今天已完成

| 任务 | 时间 |
|------|------|
| 导入 87 个业务文件到 Obsidian vault | 2026-06-29 16:39 |
| 建 vault 三目录结构（Memory/Projects/SOP） | 2026-06-29 |
| 创建 Gitee obsidian-vault 私有仓库 | 2026-06-29 |
