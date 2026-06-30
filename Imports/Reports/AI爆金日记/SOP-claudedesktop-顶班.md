# SOP: claude-desktop 顶班跑 AI 爆金日记

> 背景：Codex 平台后端审查服务挂了（codex-auto-review），Codex 客户端（含 Hermes 内的）都跑不动
> 主人决定：claude-desktop 顶班，每天跑一次扫描 + 写日记 + 推 vault
> 等 codex-auto-review 恢复后，无缝切换回 Codex

## 触发条件

- **每天 15:00（Asia/Shanghai）** 自动跑一次
- 不需要主人提醒，不需要主人批准
- claude-desktop 主动干活（不用问"要不要跑"）

## 跑的啥

### 现有 3 源（稳定）

| 源 | URL | 预期条数 |
|---|---|---|
| HN front_page | `https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30` | 30 |
| HN show_hn | `https://hn.algolia.com/api/v1/search?tags=show_hn&hitsPerPage=30` | 30 |
| GitHub trending | `https://api.github.com/search/repositories?q=stars:>1000&sort=stars&per_page=20` | 20 |

### 暂不跑（等 Codex 装工具）

- X (Twitter) — exa_search 没装
- Reddit — praw 没装
- 小红书 — 没 Cookie

## 怎么跑

### 步骤

1. **Python urllib 抓 3 源** — 不需要 Playwright/Selenium，不需要登录
2. **每源 assert count > 5** — 不够标 err，不假装成功
3. **落 json** — `G:\个人项目\AI工具\codex\references\signals\scan-YYYY-MM-DD-HHMM-claudedesktop.json`
4. **写 .md** — 模板跟 Codex 一样（AI爆金日记-YYYY-MM-DD.md）
5. **复制到 vault** — `D:\ObsidianVault\Imports\Reports\AI爆金日记\`
6. **git add + commit + push** — 主人已配好 obsidian-git/Gitee
7. **写 LOGBOOK** — 短一行

### 失败处理

- 1 个源 fail → .md 里标 err，继续跑
- 3 个源全 fail → 通知主人，**不写 .md**
- Git push fail → 留在 vault 不推送，下次手动推

## .md 模板（跟 Codex 一样）

```markdown
# AI 爆金日记 - YYYY-MM-DD (第 N 篇)

_生成时间: YYYY-MM-DD HH:MM (Asia/Shanghai)_
_Agent: claude-desktop (Opus 4.6 → MiniMax-M3)_
_执行方式: 本地 Python urllib_

> 系列说明: 每天 1 篇, 只记"干了什么 / 真信号 / 学到什么".
> 系列根目录: G:\个人项目\AI工具\codex\references\signals\
> 命名: AI爆金日记-YYYY-MM-DD.md

## 干了什么
1. ...

## 有什么结果
| 源 | 状态 | 条数 | 头 3 条 |
|---|---|---|---|

## 学到什么 (踩坑)
1. ...

## 没干的事 (按铁律)
- 没推方向
- 没算钱
- 没编成功故事

## 关联产物
- ...
```

## 铁律（主人定的，不能动）

- ❌ 不推方向（不写"建议主人做 XXX"）
- ❌ 不算钱（不写"预估月入 XXX"）
- ❌ 不编成功故事
- ❌ 不写"按主人意思，..."
- ❌ 不重复跑（一天 1 次）

## 跟 Codex 切换

### Codex 恢复的信号

- 主人回来说"codex 好了"
- 或者 LOGBOOK 出现 "codex-auto-review 恢复"
- 或者新一天早上 Codex 自己写了 AI 爆金日记

### 切换动作

1. **claude-desktop 停跑**（不再 15:00 自动跑）
2. **更新本 SOP** — 加一行 "Codex 已恢复，本 SOP 停用"
3. **通知主人** — "Codex 已恢复，我停顶班"

### 保留

- 历史 .md 全部保留（`Imports/Reports/AI爆金日记/`）
- 本 SOP 保留作为"Codex 挂了怎么办"参考

## 已知问题

- **GitHub API 字段名**：是 `items` 不是 `hits`（Codex 踩过这个坑）
- **HN 中文显示**：API 返回英文，需要人工翻译才看得懂
- **VLESS 抓取频次限制**：HN Algolia API 60s 内别超 30 次
- **GitHub API rate limit**：未认证 60 次/小时，扫一次用 1 次

## 紧急联系

- 主人 Telegram / 微信 / 直接说
- claude-desktop 自己处理：重试 3 次都不行就停
