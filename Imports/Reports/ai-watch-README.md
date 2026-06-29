# ai-watch — AI 行业每日情报 (ECS + Agnes 自动产出)

## 这是什么

每天 09:00 + 20:00 自动跑：
1. 抓 GitHub Trending 当日双榜（all + python）
2. 用 Agnes-2.0-Flash 写中文摘要（Top 8 + 深度 3 + 行动建议）
3. 落到 `/opt/ai-watch/reports/YYYY-MM-DD-morning.md` (ECS)
4. 同步到 G 盘 `G:\AI项目\ai-watch\reports\ecs\`

## 文件结构

```
G:\AI项目\ai-watch\
├── README.md               ← 你正在看
├── scripts\                ← 3 个核心脚本
│   ├── fetch_github_trending.py    # 抓 trending HTML → JSON
│   ├── summarize_with_agnes.py     # Agnes 写中文摘要
│   ├── run_daily.sh                # 串联 + cron 入口
│   └── pull_from_ecs.sh            # Windows 端拉取报告
├── data\                   # ECS 抓的原始 JSON
├── reports\                # 最终报告 (md)
│   └── ecs\                # 从 ECS 拉回来的副本
├── logs\                   # ECS 跑日志
└── archive\                # 30 天滚动归档
```

## ECS 部署

| 路径 | 用途 |
|------|------|
| `/opt/ai-watch/scripts/` | 主脚本 |
| `/home/admin/.hermes/scripts/ai-watch/` | Hermes cron 调用入口 |
| `/opt/ai-watch/reports/` | 报告输出 |
| `/opt/ai-watch/logs/` | 跑日志 |

## Cron

- `AI Watch Morning` — 每天 09:00
- `AI Watch Evening` — 每天 20:00

注册方式：`hermes cron create --no-agent --deliver local --script ai-watch/run_daily.sh "0 9 * * *" "morning"`

## 成本估算

每次 cron 调用：
- GitHub HTML: 2 次 GET (all + python)，无 key
- Agnes chat: 1 次，~1500 tokens 输入 + ~700 tokens 输出
- 假设 0.01 元/千 token（参考 Agnes 定价），**每次任务约 ¥0.02**
- 每天 2 次 × 30 天 = **每月约 ¥1.2**

## 挣钱路径（W3-W4）

1. 内容积累：积累 14 篇日报（W1-W2）
2. 公众号 / 知乎专栏：W2-W3 开通，每天发
3. 知识星球付费：W3 起，¥99/年
4. 企业 BD：W4 起，把日报做成 PDF 合集，¥99-299 卖给 AI 从业者

## 后续要加的

- [ ] Apify ProductHunt 抓取（AI 工具）
- [ ] HuggingFace 论文抓取（ai.PapersWithCode 替代源）
- [ ] 抖音博主 + GitHub 双源合并报告
- [ ] 微信公众号自动发布（draftbox 推送）
- [ ] Telegram bot 通知（绕开微信 iLink）

## 关键决定

- **不接微信 iLink** — 用户硬规则：会话 10 分钟失效，重启 gateway 触发失效窗口
- **不主动重启 gateway** — 同上
- **破坏性操作需确认** — 用户硬规则
