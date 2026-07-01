# Handoff to Hermes: 模型分工配置

- **From**: claude-desktop
- **Date**: 2026-07-01 17:30
- **Priority**: high
- **Task**: 切到新模型分工（M3 主力 + GLM 备援）
- **Context**: 主人批准新模型方案
- **Expected Output**: 你启动时按新配置加载
- **Deadline**: 2026-07-01 18:00

---

## 你的模型分工

| 维度 | 配置 |
|---|---|
| **主模型** | **MiniMax-M3**（Coding 订阅 量大管饱） |
| **base_url** | https://api.minimaxi.com/anthropic |
| **API Key** | sk-cp-xv9laq12ZSkVvPfOe3rUXeMeyIK4tX5mPiD2DjsK4Ee648MXJGu_9Eo0GPBC475PPvJFRYL5zTrW8N3gOrhg4p3FN5c5AKY6RY6dK3zWB-R6Y6o4K7Kknhw |
| **备用** | 智谱 GLM-4.5-flash（你当前用的） |
| **备援 base_url** | https://open.bigmodel.cn/api/anthropic |
| **备援 Key** | 21f8cb4476a44c33be07613a5400b3af.au8UX7ZmAD5Wbo3c |

## 配置步骤（你阿里云那边）

1. 改 `~/.hermes/config.yaml`（或你用的配置文件）：
   ```yaml
   primary_model: MiniMax-M3
   primary_url: https://api.minimaxi.com/anthropic
   primary_key: sk-cp-xv9laq12ZSkVvPfOe3rUXeMeyIK4tX5mPiD2DjsK4Ee648MXJGu_9Eo0GPBC475PPvJFRYL5zTrW8N3gOrhg4p3FN5c5AKY6RY6dK3zWB-R6Y6o4K7Kknhw
   fallback_model: glm-4.5-flash
   fallback_url: https://open.bigmodel.cn/api/anthropic
   fallback_key: 21f8cb4476a44c33be07613a5400b3af.au8UX7ZmAD5Wbo3c
   ```

2. 重启 Hermes Agent

3. 更新 HEARTBEAT.md 你那一行

## 何时切换

- **M3 主力**：日常 24h 跑 / 微信飞书 / 定时任务
- **GLM 备援**：M3 出问题时自动切换 / 网络抖动

## 不要做的事

- ❌ 不要手动切到 GLM 5.2（限流留给 Codex GUI）
- ❌ 不要自动重启 gateway（主人硬规则）

## 相关

- [[../ModelConfig-2026-07-01]] — 总配置
- [[./grab-protocol-v2]] — 抢单协议 v2

---

claude-desktop
2026-07-01 17:30