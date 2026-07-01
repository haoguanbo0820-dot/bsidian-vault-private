# 第二大脑 — 我的 AI 调度系统

> **作者**: 郝冠的 + claude-desktop（我是大脑）
> **建立**: 2026-07-01
> **目的**: 一份文档看懂整个多 Agent 调度系统 + 所有配置

---

## 这是什么

这是我（郝冠的）的**第二大脑**——Obsidian Vault 同时充当：
1. **个人知识库**（CEL 业务 / 找需求 / 日报 / 资料）
2. **多 Agent 协调层**（5 个 AI Agent 通过 vault 调度）
3. **配置中心**（所有 API key、模型分工、Agent 配置都在 vault 里）

任何时候打开 vault，都能从这个 README 开始，看懂整个系统。

---

## 5 个 AI Agent 的分工

| Agent | 平台 | 我能控？ | 专长 | 模型 |
|---|---|---|---|---|
| **claude-desktop**（我） | Claude Desktop Windows | ✅ 完全 | 调度、写文档、写代码、抓数据、跑日报 | MiniMax-M3（主力）+ DeepSeek Pro + GLM 5.2 |
| **Marvis** | 腾讯 Android Agent | ⚠️ 半自动 | Android 模拟器、App 自动化、OCR、钉钉微信抓 | MiniMax-M3 + DeepSeek Pro |
| **Hermes** | 本地 D 盘 + 阿里云 | ⚠️ 半自动 | 微信/飞书自动化、24h 定时任务 | MiniMax-M3 + 智谱 GLM-4.5-flash |
| **Codex 桌面 App** | OpenAI Codex | ❌ 需 GUI | 大型代码项目、Rust/复杂工程、PR review | GLM 5.2（火山 ark-code-latest） |
| **Trae CN** | 字节 Trae IDE | ❌ 需 GUI + token | 国内 LLM、IDE 代码、豆包/DeepSeek | 火山豆包 1.6-pro |

---

## 核心调度机制（v2）

**任务队列 + 抢单模式**（不是被动 handoff）：

```
主人交任务
  ↓
claude-desktop（大脑）拆任务
  ↓
入队 Coordination/QUEUE.json
  ↓
每个 agent 启动时扫队列 → 按技能匹配 → 抢单（原子写）
  ↓
完成 → 写 LOGBOOK.md
```

**关键设计**：
- **去单点故障**：我挂了 → 主人 30 分钟无心跳接管
- **不超载**：任务按 `required_skills` 派给特长 agent
- **主动抢单**：agent 启动自动扫队列，不是被动等 handoff
- **冲突自动检测**：原子写 QUEUE.lock，第二个看到让位

**入队权**：
- 主人 + claude-desktop → 直接入队 `QUEUE.json`
- 其他 agent → 写 `QUEUE.suggested.json`，要审核转正

**汇报**：触发式 4 种（完成/agent 挂/撞车/需主人 GUI）

详细：[[Coordination/分工设计-2026-07-01]]

---

## 模型分工（核心省钱策略）

3 个主力模型 + 1 个国内 + 多个免费：

| 模型 | 订阅类型 | 用法 | 谁用 |
|---|---|---|---|
| **MiniMax-M3** | 包年 Coding 订阅 | 主力（Coding 类活） | Claude Desktop / Hermes / Marvis |
| **DeepSeek Pro** | 按 token | 日常杂活（省钱场景） | Claude Desktop 简单筛选 / Marvis OCR 后分类 |
| **GLM 5.2**（火山 ark-code-latest） | 限流限量专项 | 留到最难的 | Codex 桌面 App 大型 review/重构 |
| **火山豆包 1.6-pro** | 火山包月 | 国内 LLM 主力 | Trae CN |
| **可灵 Kling** | 按量 | 视频生成（已有 Key） | Marvis / Hermes |
| **MiniMax Hailuo 2.3/2.3Fast** | MiniMax 平台 | 视频备援 | 同上 |
| **火山 SeeDream** | 火山包月 | 图像生成 | Marvis |
| **百度 OCR** | 按量 | OCR 解析（已有 Key） | Marvis |
| **Gemini / NVIDIA / Grok / OpenRouter** | 免费额度 | 暂未用 | 备份 |

**3 个核心规则**（主人教的）：
1. **M3 = 量大管饱** → Coding 类 agent 主力，**多用**才回本
2. **DeepSeek Pro = 按量有成本** → 日常杂活用，**不能滥用**
3. **GLM 5.2 = 限流专项** → **留给最难的**，不能浪费

详细：[[Coordination/ModelConfig-2026-07-01]]

---

## 所有配置信息（按用途分组）

### Claude Desktop（我自己）

**位置**：`C:/Users/hao/.claude/settings.json`

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://127.0.0.1:15721",  // CC Switch 代理
    "API_URL": "https://api.minimaxi.com/anthropic",  // MiniMax 主
    "API_KEY": "sk-cp-xv9laq12ZSkVvPfOe3rUXeMeyIK4tX5mPiD2DjsK4Ee648MXJGu_9Eo0GPBC475PPvJFRYL5zTrW8N3gOrhg4p3FN5c5AKY6RY6dK3zWB-R6Y6o4K7Kknhw",

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

### Hermes（阿里云 39.105.115.6）

- 当前位置：D:/OpenClaw-Hermes-Portable/（本地）+ 阿里云
- 主模型：MiniMax-M3
- 备援：智谱 GLM-4.5-flash
- 配置：[[Coordination/HANDOFFS/ModelConfig-Hermes-2026-07-01]]

### Marvis（腾讯 Android Agent）

- 主模型：MiniMax-M3
- 备援：DeepSeek Pro（OCR 后分类）
- 配置：[[Coordination/HANDOFFS/ModelConfig-Marvis-2026-07-01]]

### Codex 桌面 App

- 主模型：GLM 5.2（限流专项留给它）
- 配置：[[Coordination/HANDOFFS/ModelConfig-Codex-2026-07-01]]
- 路径：`G:/个人项目/AI工具/codex/`
- ⚠️ 当前后端审查挂了（主人 GUI 重启可恢复）

### Trae CN（字节 Trae IDE）

- 路径：`C:/Users/hao/AppData/Local/Programs/Trae CN/Trae CN.exe`
- 主模型：火山豆包 1.6-pro
- 配置：[[Coordination/HANDOFFS/ModelConfig-Trae-CN-2026-07-01]]
- ⚠️ 当前 token=0（主人 GUI 充值才能用）

---

## 全部 API Key 清单（从 APIkey.docx 提取）

详细路径：`G:/CC-Switch-v3.15.0-Windows-Portable.bak.20260627_130921/APIkey.docx`

| 平台 | Key 用途 | 状态 |
|---|---|---|
| MiniMax | M3 Coding 包年 | ✅ 主力 |
| DeepSeek | Pro 按量 | ✅ 主力 |
| 智谱 GLM | 4.5-flash 按量 | ✅ 备援 |
| 火山 ark-code-latest | GLM 5.2 限流专项 + 豆包 | ✅ 主力 |
| 火山豆包 SeeDream | 图像生成 | ✅ 包月 |
| 火山豆包视频 | 视频生成 | ✅ 包月 |
| 硅基流动 | Coding Plan Lite | ✅ 可用 |
| ModelScope | 2 token | ✅ 可用 |
| 百度千帆 / 百度 OCR | OCR + Embedding | ✅ 可用 |
| 可灵 Kling | 视频 | ✅ An8PYped... |
| MiniMax Hailuo 2.3 / 2.3Fast | 视频 | ✅ 包 |
| Google Gemini | 免费额度 | ✅ |
| xAI Grok | 按量 | ✅ |
| NVIDIA Build | 免费 | ✅ |
| OpenRouter | 按量 | ✅ |
| Brave Search | 按量 | ✅ |
| Tavily Search | 按量 | ✅ |
| aiclubs 热搜 API | 按量 | ✅ |
| yibuapi | 按量 | ✅ |
| bizyair | 按量 | ✅ |
| suanli.cn | 按量 | ✅ |
| 小米 mimi | 按量 | ✅ |
| openclaw.cn | 按量 | ✅ |
| n1n.ai | 按量 | ✅ |
| agnes-ai | 按量 | ✅ |
| Groq | 按量 | ✅ |
| Cerebras | 按量 | ✅ |

**未激活平台**（按"别浪费"原则暂不激活）：
- Hermes / Codex / Marvis / Trae CN 等 GUI 类工具需主人手动激活

**基础设施**：
- 华为云 ECS Hermes Agent-tkpc（39.105.115.6）— 到 2027/2
- 飞书 App1（笔记本）+ App2（机器人）— 已配
- 工作机（openclaw0417.pem）— 已存

---

## 协调协议（所有 Agent 必读）

```
任务前:
  1. git -C /d/ObsidianVault pull (同步最新)
  2. 读 Coordination/ACTIVE.md (防撞车)
  3. 写自己的任务 + Agent ID 到 ACTIVE.md

任务中:
  4. 复杂任务入 Coordination/QUEUE.json
  5. 简单的直接写 LOGBOOK.md

任务后:
  6. 更新 ACTIVE.md（移走任务）
  7. 写 LOGBOOK.md
  8. 重要决策 → DECISIONS.md
  9. git add -A && commit && push
```

完整协议：[[CLAUDE]]（vault 根目录）

---

## 我（主人）的工作流

1. **早上**：看 LOGBOOK.md 知道昨天干了啥
2. **有任务**：对 claude-desktop 说"去干 X" → 我拆任务入队 → agent 抢单 → 完成汇报
3. **想看进度**：问"现在在干啥" / 看 ACTIVE.md / 看 HEARTBEAT.md
4. **修 bug / 改方案**：对 claude-desktop 说 → 我评估方案 → 你批准 → 实施

**重要规则**（我自己定的）：
- ❌ 不自动启动 gateway（iLink token 10 分钟过期）
- ❌ 凌晨 2-6 点非紧急不打扰
- ❌ 不可逆操作前必须二次确认
- ❌ clarify 选项 ≤3，超时不追问
- ❌ 不编造路径/API/版本号

完整偏好：[[Memory/preferences]]

---

## 关键决策日志

| 编号 | 决策 | 日期 |
|---|---|---|
| **D001** | 使用 Obsidian Vault 作为 Agent 协调层 | 2026-06-29 |
| **D002** | MiniMax API 绕过 Karing 系统代理 | 2026-06-29 |
| **D003** | 多 Agent 调度方案 B（任务队列 + 抢单 v2） | 2026-07-01 |
| **D004** | 多 Agent 模型分工配置（M3/DeepSeek/GLM 5.2） | 2026-07-01 |

完整：[[Coordination/DECISIONS]]

---

## 目录结构

```
D:/ObsidianVault/
├── README.md (本文件)           ← 你正在看的
├── CLAUDE.md                     ← Agent 协调协议
├── Coordination/                ← Agent 协调层（5 Agent 共享读写）
│   ├── ACTIVE.md                ← 谁在做什么（任务前必读）
│   ├── LOGBOOK.md               ← 操作日志（任务后必写）
│   ├── DECISIONS.md             ← 重要决策
│   ├── QUEUE.json               ← 任务队列（v2 新机制）
│   ├── QUEUE.suggested.json     ← 建议任务
│   ├── HEARTBEAT.md             ← 5 Agent 心跳
│   ├── 分工设计-2026-07-01.md   ← v2 设计文档
│   ├── ModelConfig-2026-07-01.md ← 模型配置
│   └── HANDOFFS/                ← 任务详情
├── Memory/                      ← 用户偏好
├── Projects/                    ← 项目文档
│   ├── CEL/                     ← 中俄跨境物流
│   └── OpenJarvis/              ← AI Agent 本地部署
├── SOP/                         ← 标准操作流程
├── Imports/                     ← 业务资料（AI 爆金日记等）
└── Daily/                       ← 日记
```

---

## 当前活跃任务

| 任务 | Agent | 状态 |
|---|---|---|
| 多 Agent 调度 v2 | claude-desktop | ✅ 已落地 |
| 多 Agent 模型配置 D004 | claude-desktop | ✅ 已落地 |
| OpenJarvis 本地安装 | claude-desktop | ✅ Python 通，Rust 待定 |
| AI 爆金日记 每日采集 | codex → claude-desktop | 每日持续 |

完整：[[Coordination/ACTIVE]]

---

## 我（claude-desktop）作为大脑的承诺

1. **不会自作主张** — 不可逆操作前先问你
2. **不会超载** — 任务按特长分配，不自己扛全部
3. **不会丢任务** — QUEUE.json 持久化 + 心跳监控
4. **不会瞎汇报** — 触发式 4 种，避免打扰
5. **不会装懂** — 错了就认，不编造

如果我做错了，请告诉我，我立刻改 + 写 LESSON LEARNED 到 [[Memory/]]。

---

**维护人**: claude-desktop（大脑）
**主人**: 郝冠的
**最后更新**: 2026-07-01 18:00