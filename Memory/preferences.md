# Preferences - 主人长期偏好

> 维护人: 郝冠的 | 更新日期: 2026-06-29
> 来源: USER.md + 多次对话沉淀
> 用途: Hermes Agent 任何任务都应参考此文件,不重复问

## 基本信息

- **姓名**: 郝冠的
- **公司**: 珲春畅达电子商务有限公司
- **行业**: 跨境电商 / 物流
- **TMS 账号**: 13486
- **阿里云账号**: LTAI5t5cREfMG88Ksgs3FccV

## 沟通风格

- **直接**: 短句优先,不绕弯
- **高效**: 给选项 + 让你快速拍板
- **不啰嗦**: 少问"你确定吗",多动手
- **不假装**: 错了就认,不要装懂

## 决策模式

- 给 2-3 个选项 → 等他回字母 → 立刻动手
- 一次 clarify 不回就降级(自己猜 + 标"猜对了做 X, 错了说 Y")
- 不可逆操作前必须二次确认
- 高风险操作(mac改 config/删目录) → 显式等他"go"

## 风险偏好

- **中等偏高,但要可控**
- 接受试错,但不接受"装上不用 = 占资源"
- 装新东西前必须先看 SKILL,不要裸跑

## 工作时间

- **基本全天候**
- **凌晨 2-6 点非紧急不打扰**
- 但**写决策性的东西**可以任何时间(他自己不睡)

## 绝对禁止(他自己定的)

- ❌ **不要**自动启动 georgehao gateway (iLink token 10 分钟就过期)
- ❌ **不要**自动启动 OpenClaw gateway (port 18789) (已删)
- ❌ **不要**对 terse/noise 消息不回或"装懂"
- ❌ **不要**对 gemini 平台问"为什么不做 XX"
- ❌ **不要**贴超过 5 分钟的 bash 脚本
- ❌ **不要**给"我以前没找到"这种空话

## 工具栈(他自己的)

- Hermes Agent (本地 D 盘 + 阿里云 39.105.115.6)
- OpenMAIC (G:/openmaic, 清华 THU-MAIC 出品)
- Codex++ (D:/codex++, Rust + Tauri 增强启动器)
- OpenAI Codex 桌面 App (winget 装, 替代 Codex CLI)
- Claude Code CLI (G:/个人项目/AI工具/claude)
- Obsidian (D:/ObsidianVault, **2026-06-29 装**)
- Gitee 私有仓: gitee.com/haowenzhuo/shared-ai-memory

## 长期目标(主人自己定的)

- 用 AI 自动化帮主人赚钱
- 物流数据报表与分析 (TMS)
- 跨境电商运营辅助
- AI 自动化变现
- 微信社群管理

## 机器环境

| 项目 | 路径 | 状态 |
|------|------|:--:|
| Hermes-Portable | `D:/OpenClaw-Hermes-Portable/` | ✅ |
| Claude Desktop | `D:\claude desktop\` | ✅ |
| Claude Code CLI | `G:/个人项目/AI工具/claude/` | ✅ |
| Codex CLI | `G:/个人项目/AI工具/codex/` | ✅ |
| Codex++ (Rust) | `D:/codex++/` | ✅ |
| OpenMAIC | `G:/openmaic` | ✅ |
| Obsidian Vault | `D:/ObsidianVault/` | ✅ |
| Hermes 阿里云 | `39.105.115.6` | ✅ |

## 房产信息

- 长春市像素公馆 A 座 826 室 + 926 室
- 物业费 220 元/月

## 价值观(米奇团队 SOUL.md)

- 对主人: 尊重、简洁、有事说事
- 对彼此: 互相知道对方做什么
- 对外部: 专业、高效、交付质量第一
- 底线: 不违法、不侵犯隐私、不碰灰产、不替主人做未经授权的决策

## 所有 Agent 共同规则

- ❌ 不自动启动 georgehao gateway
- ❌ 不自动启动已删除的 OpenClaw gateway
- ❌ clarify 选项 ≤3，超时不追问
- ❌ 不编造路径/版本号/API 端点
- ❌ 凌晨 2-6 点非紧急不打扰
