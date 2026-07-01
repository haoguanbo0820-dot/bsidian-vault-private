# 多 Agent 模型分工配置 v2

> **作者**: claude-desktop
> **日期**: 2026-07-01
> **状态**: ✅ 已落地运行
> **版本**: v2（实际运行状态）

---

## 一、3 个模型的核心定位

| 模型 | 定位 | 谁用 |
|---|---|---|
| **MiniMax-M3** | Coding 订阅 量大管饱 | Codex + Claude Desktop（备用） |
| **DeepSeek Pro** | 按用量有成本 | Claude Desktop 主力 |
| **GLM 5.2（火山 ark-code-latest）** | 限流限量专项 | Claude Code |

---

## 二、实际运行配置（v2）

### 架构

```
:15888 → Anthropic → DeepSeek Pro / OpenAI → MiniMax M3 (Codex)
:15889 → Anthropic → GLM 5.2 / OpenAI → MiniMax M3 (Claude Code)
```

### Claude Desktop

| 维度 | 配置 |
|---|---|
| **主模型** | DeepSeek Pro |
| **路由** | `ANTHROPIC_BASE_URL = http://127.0.0.1:15888` |
| **API Key** | {{见 APIkey.docx}}（sk-87749c...） |
| **配置位置** | `C:/Users/hao/.claude/settings.json` |

### Codex 桌面 App

| 维度 | 配置 |
|---|---|
| **主模型** | MiniMax-M3（v2 切换，非 GLM 5.2） |
| **路由** | `openai_base_url = http://127.0.0.1:15888/v1` |
| **配置位置** | `C:/Users/hao/.codex/config.toml` |
| **协议** | OpenAI Responses → MiniMax Anthropic（路由器翻译） |

### Claude Code

| 维度 | 配置 |
|---|---|
| **主模型** | GLM 5.2（火山 ark-code-latest） |
| **路由** | `ANTHROPIC_BASE_URL = http://127.0.0.1:15889` |
| **启动** | `claude-code-glm.bat` |

### Hermes Agent

| 维度 | 配置 |
|---|---|
| **主模型** | MiniMax-M3 |
| **备用** | 智谱 GLM-4.5-flash |
| **位置** | 阿里云 39.105.115.6 |

### Marvis

| 维度 | 配置 |
|---|---|
| **模型** | 自带（腾讯内置）|

### Trae CN

| 维度 | 配置 |
|---|---|
| **模型** | 火山豆包 1.6-pro |
| **状态** | ⚪ token=0 |

---

## 三、路由器实现

**位置**: `G:/个人项目/AI工具/codex/unified-router/server.mjs`
**开机自启**: `start-router.bat` → Startup 文件夹

| 端口 | Anthropic | OpenAI |
|---|---|---|
| `:15888` | → DeepSeek Pro | → MiniMax M3 |
| `:15889` | → GLM 5.2 | → MiniMax M3 |

---

## 四、历史版本

- v1（废弃）：M3→Claude Desktop / GLM 5.2→Codex / DeepSeek→日常
- v2（当前）：DeepSeek→Claude Desktop / M3→Codex / GLM 5.2→Claude Code

---
**维护人**: claude-desktop
