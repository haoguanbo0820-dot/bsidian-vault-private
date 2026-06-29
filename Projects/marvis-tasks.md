# Marvis 任务看板

> 由 claude-desktop 发现并登记（2026-06-29）
> Marvis 是 **Python 脚本驱动的 Android 自动化 Agent**，不自行读 vault，需人工协调

## 身份

| 字段 | 值 |
|------|-----|
| **Agent ID** | `marvis` |
| **产品名** | Tencent Marvis（腾讯桌面 AI 助手） |
| **代码位置** | `G:/模拟器+agent/marvis/` |
| **LLM** | MiniMax-M3 @ `api.minimax.chat/v1` |
| **ADB 目标** | `127.0.0.1:14016`（MuMu 模拟器） |
| **安装路径** | `D:\Program Files\Tencent\Marvis\MarvisAgent\1.0.1100.240\` |
| **数据路径** | `D:\Program Files\Tencent\MarvisData\` |
| **当前状态** | 🟡 未运行 |

## 架构

```
用户自然语言指令
     ↓
MainAgent (总调度)
  ├── LLMDecisionMaker (MiniMax-M3 决策引擎)
  ├── DeviceController (ADB 截图 + 控件树 + 点击/滑动/输入)
  ├── OCREngine (轻量 OCR)
  ├── Scheduler (Cron 定时调度)
  ├── StateManager (断点续跑)
  └── Sub Agents
       ├── AppAgent → 操控 Android App（核心）
       ├── FileAgent → 文件操作
       └── ComputerAgent → 系统操作
```

**感知→决策→执行循环**: 截图 + 控件树 → LLM 决策 → ADB 执行（tap/swipe/input/back...）→ 循环

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

## 历史任务（2026-06）

从 SQLite 数据库 `marvis.db` 恢复：

| 日期 | 意图 | 目标 App | 结果 |
|------|------|----------|------|
| 06-08 | 在闲鱼搜索"俄罗斯快递作废件无头" | 淘宝/闲鱼 | ❌ 多次尝试，device offline |
| 06-08 | 在京东搜索"笔记本电脑"比性价比 | 京东 | ⚠️ 多次打满 15 步未完成 |
| 06-10 | 在京东搜笔记本电脑 | 京东 | ⚠️ 同上 |

**根因分析**: 大量 "device offline" 错误 → MuMu 模拟器未启动或 ADB 端口不通

## 定时调度

- **Scheduler 已实现**（`scheduler.py`）但 **未配置任何 cron 任务**（`scheduler.json` 不存在）
- 支持格式: `分 时 日 月 星期`

## 已知问题

1. ❌ **模拟器离线**: 6 月执行了大量任务，多数因 "device offline" 失败
2. ❌ **无 vault 协调**: 作为 Python Agent，不会读 CLAUDE.md / ACTIVE.md
3. ❌ **无监控告警**: 任务失败后不会通知
4. ⚠️ **步数限制 15**: 多数复杂任务打满 15 步未完成（如京东比价）
5. ⚠️ **闲鱼未在可用 App 列表**: 代码里 `KNOWN_APPS` 有闲鱼包名，但实际执行时用了淘宝做替代

## 建议改进

1. 启动前检查 ADB 连接: `adb devices` 确认 `127.0.0.1:14016` online
2. 配置 scheduler: 添加定时任务（如每天 9 点发小红书）
3. 增加 max_steps 到 30（复杂任务如比价需要更多步）
4. 考虑通过 TaskFlow 或其他桥接让 Marvis 能被其他 Agent 调度
