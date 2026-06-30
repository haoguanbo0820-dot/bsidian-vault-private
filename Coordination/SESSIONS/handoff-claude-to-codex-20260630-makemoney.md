---
date: 2026-06-30 15:50
from: claude-desktop
to: codex
subject: 新任务：网上找搞钱机会（AI 爆金日记升级版）
status: pending codex-auto-review 恢复
---

# Handoff: claude-desktop → codex（新任务）

> 主人原话："我要是让他去网上找挣钱的机会"
> 主人确认：扩大源（加 X/Reddit/小红书） + 每天 1 篇 AI 爆金日记（只日志不推方向）+ 过渡期 claude-desktop 顶班

## 1. 任务定义

### 1.1 一句话

每天跑一次多源扫描，把"搞钱真信号"收集起来，写成 AI 爆金日记。

### 1.2 真信号源（5 个）

| 源 | 状态 | 工具 | URL |
|---|---|---|---|
| Hacker News front_page | ✅ 已有 | urllib | `https://hn.algolia.com/api/v1/search?tags=front_page` |
| Hacker News show_hn | ✅ 已有 | urllib | `https://hn.algolia.com/api/v1/search?tags=show_hn` |
| GitHub trending (>1k stars) | ✅ 已有 | urllib | `https://api.github.com/search/repositories?q=stars:>1000` |
| **X (Twitter)** | ❌ 需装 | exa_search | 搜索：AI agent, side project, indie hacker, MRR |
| **Reddit** | ❌ 需装 | GH CLI / praw | r/SaaS, r/Entrepreneur, r/AI_Agents, r/sideproject |
| **小红书** | ⚠️ 需登录态 | Playwright + 主人 Cookie | 关键词：AI 副业、跨境电商、独立开发者 |

### 1.3 产出规则（铁律，跟今天一样）

- ✅ 每天 1 篇 `AI爆金日记-YYYY-MM-DD.md`
- ✅ 记"干了什么 / 真信号 / 学到什么"
- ✅ 原始数据落 json（`scan-YYYY-MM-DD-HHMM.json`）
- ❌ **不推方向**（不写"建议主人做 XXX"）
- ❌ **不算钱**（不写"预估月入 XXX"）
- ❌ **不编成功故事**（不上价值）

### 1.4 路径

| 物 | 路径 |
|---|---|
| 本地系列根 | `G:\个人项目\AI工具\codex\references\signals\` |
| 命名 | `AI爆金日记-YYYY-MM-DD.md` + `scan-YYYY-MM-DD-HHMM.json` |
| vault 目标 | `D:\ObsidianVault\Imports\Reports\AI爆金日记\` |
| ECS 备份 | `root@39.105.115.6:/root/signals/` |

## 2. 过渡期（现在 → codex-auto-review 恢复）

**claude-desktop 顶班**，规则：
- 每天 15:00 跑一次（你可以调时间）
- 暂时只跑 3 源（HN + GitHub），X/Reddit/小红书 等你回来装工具
- 写完直接推 vault，不走你那边
- 你的本地副本会同步（我复制到 `G:\个人项目\AI工具\codex\references\signals\`）

**顶班期 SOP**（`Imports/Reports/AI爆金日记/SOP-claudedesktop-顶班.md`，待我写）

## 3. 你恢复后要装的工具

### 3.1 exa_search（X 搜索）

- 主人之前提过，但没装
- 装好后在 `~/.codex/.agents/` 配置
- 搜索 query 模板：
  - `AI agent side project revenue 2026`
  - `indie hacker MRR`
  - `made $XXXX with AI tool`
  - `automated business solo founder`

### 3.2 Reddit 抓取

- 装 `praw`（Python Reddit API Wrapper）
- 需要主人提供 Reddit API client_id + client_secret
- 抓 r/SaaS, r/Entrepreneur, r/AI_Agents, r/sideproject, r/automation

### 3.3 小红书

- 装 Playwright
- 需要主人提供小红书登录 Cookie
- 抓 关键词 "AI 副业"、"跨境电商"、"独立开发者"、"AI 工具变现"

### 3.4 不需要装的

- HN API / GitHub API：现有 urllib 就能跑

## 4. 你恢复后第一周的目标

1. **第 1-2 天**：把现有 3 源跑稳，claude-desktop 同步顶班
2. **第 3-4 天**：装 exa_search + 试 X 搜索 5 个 query
3. **第 5-6 天**：装 praw + 试 Reddit 4 个 sub
4. **第 7 天**：跟主人要小红书 Cookie（先不动），看主人意思

## 5. 状态同步

- LOGBOOK 已登记（等下我写）
- ACTIVE.md 不用改（这是延续 AI 爆金日记任务）
- 主人期望：每天 1 篇日记，不在乎抓多少条
- 主人不要：推荐方向、估算收入、画大饼

## 6. 关键路径速查

| 物 | 路径 |
|---|---|
| 本地系列根 | `G:\个人项目\AI工具\codex\references\signals\` |
| 今日日记 | `AI爆金日记-2026-06-30.md`（你的）+ `AI爆金日记-2026-06-30-下午.md`（claude-desktop 的） |
| 你的沙箱白名单 | `:root` + `G:\个人项目\AI工具\codex\` + 工作目录 |
| claude-desktop 工作目录 | `D:\claude desktop\` |
| Hermes 路径（D 盘，沙箱外） | `D:\OpenClaw-Hermes-Portable\` |
| ECS 备份 | `root@39.105.115.6:/root/signals/` |
| vault LOGBOOK | `D:\ObsidianVault\Coordination\LOGBOOK.md` |
| vault SESSIONS | `D:\ObsidianVault\Coordination\SESSIONS\` |

---

**总结**：你的新任务是"扩大源找搞钱机会"——HN+GitHub+X+Reddit+小红书，每天 1 篇 AI 爆金日记（只日志不推方向）。过渡期 claude-desktop 顶班。装 exa_search + praw 需要主人给 API key。

— claude-desktop (Opus 4.6 → MiniMax-M3)
