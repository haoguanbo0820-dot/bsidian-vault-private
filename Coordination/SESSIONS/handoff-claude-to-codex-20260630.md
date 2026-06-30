---
date: 2026-06-30
from: claude-desktop
to: codex
subject: CEL 揽收端 AI 采集 + 权限授权
---

# Handoff: claude-desktop → codex

> 主人说"给 codex 一个权限"。以下是你的授权和上下文。

## 你的新权限

1. **读 CEL 项目文档**：`D:\ObsidianVault\Projects\CEL\` 下所有文件你都可以读
2. **写 LOGBOOK**：按协议完成任务后写入 `D:\ObsidianVault\Coordination\LOGBOOK.md`
3. **写 ACTIVE.md**：开始任务前在 ACTIVE.md 登记
4. **写 SESSIONS/**：handoff 文件写入 `D:\ObsidianVault\Coordination\SESSIONS\`
5. **读 Hermes 知识库设计**：`D:\ObsidianVault\Projects\Hermes\Hermes-knowledge-base-design.md` 和 `Hermes-knowledge-base-plan.md`（跟 CEL 规则知识库直接相关）

## sandbox 问题

你上次 handoff 说 sandbox 写不动 D:\。试试直接写——如果还是写不动，在 LOGBOOK 旁路记录（写到 `G:\个人项目\AI工具\codex\references\signals\`），我来推 vault。

## CEL 项目上下文（你要知道的）

### 核心问题
CEL（珲春畅达）每天 30 万单中俄跨境包裹，用光照机（X光）看包裹——只能看形状，看不出品类/价值/违禁品/包装合规。

### 目标方案
用手机 + 多模态 AI 替代光照机，6 个节点拍照上传：
```
揽收 → 入仓 → 分拣 → 组包 → 出关 → 境外配送
```

### 关键量化数据
- 罚款累计 1517 万（9 万+ 单）
- 每天 5000-6000 单 1 卢布假货值
- 取消率 1.7% vs 平台均值 0.8%
- 改造后每单检查从 30-60 秒降到 9 秒

### 关键文档
| 文档 | 路径 |
|------|------|
| 需求文档（含路由节点） | [[CEL-揽收端AI采集需求文档]] |
| 技术方案 | [[CEL-揽收端AI采集方案]] |
| CEL 总览 | [[CEL-home]] |

### 已有资产（别从零开始）
- **TMS WCF 地址**：`net.tcp://47.107.84.253:6011/IntegrateReportDelegate`（你之前逆向过的）
- **Hermes 情报系统**：已在监控 5 个 CEL 微信群，日报/周报/月报管线已跑通
- **Hermes 知识库设计**：9 表 schema + 三层价格体系，可直接复用
- **阿里云 ECS**：39.105.115.6，AI 分析后端部署目标

### 计划里需要修正的
1. TMS 方案 A（直接写入）大概率走不通——你之前发现版本检查阻塞
2. 运营看板不需要从零开发——对接 Hermes 已有管线
3. 规则知识库可以复用 Hermes 知识库的 schema

## 你可以做的事

1. **验证 TMS 写入可行性**——你比谁都清楚那个 WCF 的版本检查阻塞
2. **整理规则知识库 MVP**——俄罗斯海关禁运清单、HS 编码映射、EAC 认证品类
3. **研究 Ozon/WB API 追踪节点对接**——跟方案里的状态码体系对齐
4. **评估 Claude Vision API 在实际场景的识别准确率**——用真实 CEL 包裹照片测试

## 交接文件位置

- vault 项目文档：`D:\ObsidianVault\Projects\CEL\`
- vault 协调：`D:\ObsidianVault\Coordination\`
- 你的本地：`G:\个人项目\AI工具\codex\`
- 手握手：`G:\个人项目\AI工具\codex\references\signals\`
