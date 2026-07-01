# Handoff to Codex 桌面 App: 模型分工配置

- **From**: claude-desktop
- **Date**: 2026-07-01 17:30
- **Priority**: high
- **Task**: 主人 GUI 触发时按此配置
- **Deadline**: 等主人重启 GUI

---

## 你的模型分工

| 维度 | 配置 |
|---|---|
| **主模型** | **GLM 5.2**（限流专项 = 留给你的） |
| **base_url** | https://ark.cn-beijing.volces.com/api/coding |
| **API Key** | api-key-20260308224717 |
| **模型名** | ark-code-latest（Auto 智能选 GLM 5.2） |

## ⚠️ 重要

**你是 GLM 5.2 的"专项用户"**——因为 GLM 5.2 限流，主人的策略是把它留给你（Codex 桌面 App）做大型代码 review / 重构。其他 agent 不要抢这个额度。

## 配置步骤（主人 GUI 里）

1. 打开 Codex 桌面 App
2. Settings → API Configuration：
   - Provider: Volcano Ark (Custom)
   - Base URL: https://ark.cn-beijing.volces.com/api/coding
   - API Key: api-key-20260308224717
   - Model: ark-code-latest

3. 重启 Codex 桌面 App

## 何时使用

- ✅ **大型代码 review**（你专长）
- ✅ **大型 Rust 重构**（你专长）
- ✅ **复杂代码分析**（你专长）
- ❌ **不要用其他模型**（GLM 5.2 是你的）

## 现状

- 🔴 当前后端审查挂了
- 等主人 GUI 重启 + 后端恢复

## 相关

- [[../ModelConfig-2026-07-01]]

---

claude-desktop
2026-07-01 17:30