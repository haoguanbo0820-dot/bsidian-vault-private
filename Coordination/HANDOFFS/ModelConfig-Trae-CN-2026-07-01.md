# Handoff to Trae CN: 模型分工配置

- **From**: claude-desktop
- **Date**: 2026-07-01 17:30
- **Priority**: low（等你充值激活）
- **Task**: 主人 GUI 充值后按此配置
- **Deadline**: 等主人

---

## 你的模型分工

| 维度 | 配置 |
|---|---|
| **主模型** | **火山豆包 1.6-pro**（包月） |
| **base_url** | https://ark.cn-beijing.volces.com/api/v3 |
| **API Key** | {{见 APIkey.docx}} |
| **模型名** | doubao-1-5-pro-32k-250115 或更新 |
| **备用** | MiniMax-M3（同 API key 走 minimaxi.com） |

## ⚠️ 状态

- ⚪ **当前 token=0**（主人说"一直没用"）
- 要主人 GUI 充值才能激活

## 配置步骤（主人 GUI 里）

1. 充值 token 到火山平台
2. 打开 Trae CN
3. Settings → Models：
   - Primary: 火山豆包 1.6-pro (via Volcano Ark)
   - URL: https://ark.cn-beijing.volces.com/api/v3
   - Key: {{见 APIkey.docx}}
4. 保存重启

## 何时使用

- ✅ 国内 LLM 调用（豆包便宜）
- ✅ IDE 编码任务
- ✅ Excel 批处理

## 你在国内 LLM 生态里的位置

你是**国内 LLM 主力 agent**——比 Claude Desktop 调国内模型更快/更便宜（豆包包月不限量 vs Claude Desktop 走海外 API 慢）。

## 相关

- [[../ModelConfig-2026-07-01]]

---

claude-desktop
2026-07-01 17:30