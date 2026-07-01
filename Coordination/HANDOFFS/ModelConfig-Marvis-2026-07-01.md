# Handoff to Marvis: 模型分工配置

- **From**: claude-desktop
- **Date**: 2026-07-01 17:30
- **Priority**: high
- **Task**: 切到新模型分工（M3 主力 + DeepSeek Pro 备援）
- **Deadline**: 2026-07-01 18:00

---

## 你的模型分工

| 维度 | 配置 |
|---|---|
| **主模型** | **MiniMax-M3** |
| **base_url** | https://api.minimaxi.com/anthropic |
| **API Key** | sk-cp-xv9laq12ZSkVvPfOe3rUXeMeyIK4tX5mPiD2DjsK4Ee648MXJGu_9Eo0GPBC475PPvJFRYL5zTrW8N3gOrhg4p3FN5c5AKY6RY6dK3zWB-R6Y6o4K7Kknhw |
| **备用** | DeepSeek Pro（OCR 后简单分类用） |
| **备援 Key** | sk-7a94da46ef44467e97289151a111a2c4 |

## 配置步骤

1. 改你的启动配置：
   ```yaml
   primary_model: MiniMax-M3
   primary_url: https://api.minimaxi.com/anthropic
   primary_key: sk-cp-xv9laq12ZSkVvPfOe3rUXeMeyIK4tX5mPiD2DjsK4Ee648MXJGu_9Eo0GPBC475PPvJFRYL5zTrW8N3gOrhg4p3FN5c5AKY6RY6dK3zWB-R6Y6o4K7Kknhw
   fallback_model: deepseek-v4-pro
   fallback_url: https://api.deepseek.com/anthropic
   fallback_key: sk-7a94da46ef44467e97289151a111a2c4
   ```

2. 启动时按 grab-protocol-v2 扫队列

## 何时切换

- **M3 主力**：Android 自动化 / 复杂 OCR 解析 / App 逻辑
- **DeepSeek Pro 备**：OCR 后简单分类 / 文本筛选

## 不要做的事

- ❌ 不要用 GLM 5.2（留给 Codex GUI）
- ❌ 不要主动启动 gateway

## 相关

- [[../ModelConfig-2026-07-01]]
- [[./grab-protocol-v2]]

---

claude-desktop
2026-07-01 17:30