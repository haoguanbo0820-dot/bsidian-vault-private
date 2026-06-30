# Marvis 任务看板

> 由 claude-desktop 发现并登记（2026-06-29），2026-06-30 接入 vault 自动协调
> Marvis 通过 `vault_coordinator.py` 接入 vault，与 4 个文件型 Agent 协同

## 身份

| 字段 | 值 |
|------|-----|
| **Agent ID** | `marvis` |
| **产品名** | Tencent Marvis（腾讯桌面 AI 助手） |
| **代码位置** | `G:/模拟器+agent/marvis/` |
| **状态存储** | `G:/模拟器+agent/state/`（16 个 JSON 文件） |
| **导出目录** | `G:/模拟器+agent/output/` |
| **LLM** | MiniMax-M3 @ `api.minimax.chat/v1` |
| **ADB 目标** | `127.0.0.1:14016`（MuMu 模拟器） |
| **安装路径** | `D:\Program Files\Tencent\Marvis\MarvisAgent\1.0.1100.240\` |
| **Vault 协调** | ✅ `vault_coordinator.py`（2026-06-30 接入） |
| **当前状态** | 🟢 已接入协调，待下次运行生效 |

## 架构

```
用户自然语言指令
     ↓
MainAgent (总调度)
  ├── vault_coordinator → pull / check_conflicts / register / complete / push
  ├── LLMDecisionMaker (MiniMax-M3 决策引擎)
  ├── DeviceController (ADB 截图 + 控件树 + 点击/滑动/输入)
  ├── OCREngine (轻量 OCR)
  ├── Scheduler (Cron 定时调度)
  ├── StateManager (断点续跑，./state/*.json)
  └── Sub Agents
       ├── AppAgent → 操控 Android App（核心）
       ├── FileAgent → 文件操作
       └── ComputerAgent → 系统操作
```

**感知→决策→执行循环**: 截图 + 控件树 → LLM 决策 → ADB 执行（tap/swipe/input/back...）→ 循环，max 15 步/子任务

## 支持的 App

| App | 包名 |
|-----|------|
| 抖音 | `com.ss.android.ugc.aweme` |
| 小红书 | `com.xingin.xhs` |
| 微信 | `com.tencent.mm` |
| 淘宝 | `com.taobao.taobao` |
| 闲鱼 | `com.taobao.idlefish` |
| 京东 | `com.jingdong.app.mall` |
| 哔哩哔哩 | `com.bilibili.app.in` |
| 快手 | `com.kuaishou.nebula` |

---

## 运行状况

| 问题 | 状态 | 说明 |
|------|:--:|------|
| Vault 协调 | ✅ | `vault_coordinator.py`（2026-06-30 接入） |
| Scheduler | ⚠️ | `scheduler.json` 不存在，未配置定时任务 |
| max_steps | ⚠️ | 默认 15，复杂任务可能不够 |

## 启动前检查

1. MuMu 模拟器已启动且 `adb devices` 确认 `127.0.0.1:14016` online
2. vault_coordinator 自动生效：任务前后自动拉取/推送 vault
