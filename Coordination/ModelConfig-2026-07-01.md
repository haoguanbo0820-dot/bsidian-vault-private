# 多 Agent 模型分工配置 v1

> **作者**: claude-desktop (大脑)
> **日期**: 2026-07-01
> **状态**: ✅ 主人已批准"按分析最优方案"
> **决策**: D004 in `Coordination/DECISIONS.md`
> **版本**: v1

---

## 一、3 个模型的核心定位（主人教的）

| 模型 | 真正定位 | 主用场景 |
|---|---|---|
| **MiniMax-M3** | **Coding 订阅 量大管饱** | 编程任务主力（Coding/调度/写文档/抓数据 = 本质都是 Coding 类活） |
| **DeepSeek Pro** | **按用量有成本** | 日常杂活主力（筛选/分类/简单任务 - 用它的成本可控） |
| **GLM 5.2（火山 ark-code-latest）** | **限流限量专项** | 留到最难的专项任务（Codex GUI 触发时 / 我写大型代码时） |

**关键洞察**（主人教的）：
- Claude Desktop/Hermes/Marvis 干的活本质上都是 Coding 类（写代码、调 API、写脚本、抓数据），所以 M3 给它们是合理的
- 量大管饱 = 包年 Coding 订阅就要**多用**才回本
- 按量有成本 = DeepSeek Pro **不能滥用**，给日常
- 限流专项 = GLM 5.2 **留给最难的**，不能浪费

---

## 二、5 个 Agent 模型分工表

### Claude Desktop（我）

| 维度 | 配置 |
|---|---|
| **主模型** | MiniMax-M3 (Coding 订阅) |
| **base_url** | https://api.minimaxi.com/anthropic |
| **API Key** | sk-cp-xv9laq12ZSkVvPfOe3rUXeMeyIK4tX5mPiD2DjsK4Ee648MXJGu_9Eo0GPBC475PPvJFRYL5zTrW8N3gOrhg4p3FN5c5AKY6RY6dK3zWB-R6Y6o4K7Kknhw |
| **配置位置** | `C:/Users/hao/.claude/settings.json` env.API_URL |
| **何时切 DeepSeek Pro** | 简单筛选/分类/省钱场景 |
| **何时切 GLM 5.2** | 写大型代码/复杂逻辑/重要 review |
| **何时不切** | 重要任务不要切 Pro（质量不够）；日常不要切 GLM（浪费限流） |

### Hermes Agent

| 维度 | 配置 |
|---|---|
| **主模型** | MiniMax-M3 |
| **备用** | 智谱 GLM-4.5-flash（APIkey 已有） |
| **配置位置** | 阿里云 39.105.115.6 配置文件 |
| **何时切 GLM** | M3 出问题时；阿里云网络抖动 |
| **当前状态** | 🟢 active（阿里云 24h 跑） |

### Marvis

| 维度 | 配置 |
|---|---|
| **主模型** | MiniMax-M3 |
| **备用** | DeepSeek Pro (OCR 后简单分类) |
| **配置位置** | 待 Marvis 启动时按 handoff 配置 |
| **何时切 Pro** | OCR 结果分类/简单筛选任务 |
| **当前状态** | 🟡 idle（等启动） |

### Codex 桌面 App

| 维度 | 配置 |
|---|---|
| **主模型** | **GLM 5.2**（限流专项 = 留给 Codex） |
| **base_url** | https://ark.cn-beijing.volces.com/api/coding |
| **API Key** | api-key-20260308224717 |
| **模型名** | ark-code-latest |
| **何时用** | 主人 GUI 重启 + 后端恢复后 |
| **当前状态** | 🔴 down（后端审查挂了） |

### Trae CN

| 维度 | 配置 |
|---|---|
| **主模型** | 火山豆包 1.6-pro（包月） |
| **备用** | MiniMax-M3 |
| **配置位置** | Trae CN GUI 里设置（主人充值 token 后） |
| **何时用** | 主人充值 + 开 GUI |
| **当前状态** | ⚪ token=0 |

---

## 三、图形 / 视频 / 多模态

| 用途 | 模型 | 平台 | Key |
|---|---|---|---|
| **图像生成** | 火山 SeeDream | 火山包月 | api-key-20260308224717 |
| **视频生成** | 可灵 | klingai.com | An8PYpedfHBfAPRD83kFBTQnNmgmPRag |
| **视频备** | MiniMax Hailuo 2.3 / 2.3Fast | MiniMax 平台 | 同 M3 key |
| **OCR** | 百度 OCR（APIkey 已有） | console.bce.baidu.com | ALTAKcnOdkv1s2zXjrPc3nWqDm |

---

## 四、Claude Desktop env 配置（已落地）

**文件**：`C:/Users/hao/.claude/settings.json`

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "PROXY_MANAGED",
    "ANTHROPIC_BASE_URL": "http://127.0.0.1:15721",
    "API_KEY": "sk-cp-xv9laq12ZSkVvPfOe3rUXeMeyIK4tX5mPiD2DjsK4Ee648MXJGu_9Eo0GPBC475PPvJFRYL5zTrW8N3gOrhg4p3FN5c5AKY6RY6dK3zWB-R6Y6o4K7Kknhw",
    "API_URL": "https://api.minimaxi.com/anthropic",

    "DEEPSEEK_API_KEY": "sk-7a94da46ef44467e97289151a111a2c4",
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com/anthropic",

    "VOLC_ARK_API_KEY": "api-key-20260308224717",
    "VOLC_ARK_BASE_URL": "https://ark.cn-beijing.volces.com/api/coding",
    "VOLC_ARK_MODEL": "ark-code-latest",

    "ZHIPU_API_KEY": "21f8cb4476a44c33be07613a5400b3af.au8UX7ZmAD5Wbo3c"
  },
  "theme": "dark"
}
```

**注意**：env 字段加了 4 个备援 API key + URL，模型路由器可以根据任务类型切换。

---

## 五、模型切换规则（智能路由思路）

主人没让我**实现自动切换**，但我设计**切换决策表**给主人/未来 router 用：

| 任务类型 | 默认模型 | 切换 |
|---|---|---|
| 写代码/调试/重构 | M3 | 复杂 review → GLM 5.2 |
| 调度协调/写文档 | M3 | 简单筛选 → DeepSeek Pro |
| 抓数据/解析 HTML | M3 | 简单分类 → DeepSeek Pro |
| brainstorm/策划 | M3 | — |
| 24h 跑（Hermes/Marvis） | M3 | — |
| 大型代码 review | GLM 5.2 | — |
| 极复杂推理 | GLM 5.2 | — |
| 编程新手教程 | M3 | — |
| 视频脚本 | M3 | — |
| 图像生成 | 火山 SeeDream | — |
| 视频生成 | 可灵 / Hailuo 2.3 | — |

---

## 六、主人当前订阅清单

| 平台 | 类型 | 状态 |
|---|---|---|
| MiniMax-M3 | **包年 Coding 订阅** | ✅ 活跃（主力） |
| DeepSeek Pro | 按 token | ✅ 充值中（按量） |
| 火山 ark-code-latest | 包月 + 套餐 | ✅ 活跃（GLM 5.2 + 豆包 + SeeDream） |
| 智谱 GLM-4.5-flash | 按 token | ✅ 备援 |
| 智谱 GLM-5.2 | 火山 ark 包月里 | ✅ 限流专项 |
| 豆包 1.6-pro | 火山包月 | ✅ Trae CN 用 |
| MiniMax Hailuo 2.3/2.3Fast | MiniMax 包 | ✅ 视频 |
| 可灵 Kling | 按量 | ✅ 视频（已有 Key） |
| 百度 OCR | 按量 | ✅ OCR |

**未用**：Gemini 免费 / NVIDIA 免费 / Grok / OpenRouter / 多数中转 API（按主人"别浪费"原则暂不激活）

---

## 七、成本估算（粗算）

| 项 | 单价 | 月预估 |
|---|---|---|
| M3（包年已付） | ¥0 | ¥0 |
| DeepSeek Pro（按量） | input ¥3/M + output ¥6/M | ¥30-80/月（看用量） |
| 火山 ark 包月 | ¥X (固定) | 已付 |
| 智谱 GLM-4.5-flash | input ¥0.5/M | ¥5-20/月 |
| 合计 | — | **¥50-150/月**（不含已付包年） |

---

## 八、回滚方案

如果新方案跑 2 周发现：
- **症状 A**：DeepSeek Pro 用超预算 → 强制只 M3（删除 env）
- **症状 B**：GLM 5.2 限流触发频繁 → M3 顶上去
- **症状 C**：M3 质量不够某专项 → 切回 GLM 5.2（专项）

回滚决策权 = 主人。

---

## 九、版本

- v1（2026-07-01）：主人批准"按分析最优方案"——M3 主力 / DeepSeek Pro 日常 / GLM 5.2 限流专项

---

**审批栏**：
- 主人：✅ 已批准"按分析最优方案"（2026-07-01）
- 实施日期：2026-07-01
- 维护人：claude-desktop