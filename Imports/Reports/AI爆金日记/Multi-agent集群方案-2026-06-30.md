# Multi-agent 集群方案 — 评估

> 评估时间: 2026-06-30 15:55
> 评估人: claude-desktop
> 主人原话："用 Multi-agent cluster coordination 在跑的项目去抓数据能行吗"

## TL;DR

**能行，但前提是主人给 CDP 或 Cookie**——Playwright 装好了、Edge 能跑、但**headless 抓不到国内平台**（都触发登录墙）。需要主人**已经登录的真实浏览器**（CDP attach），或**登录态 Cookie**。

实测结果：

| 平台 | headless urllib | headless Edge | 真实浏览器 CDP | 备注 |
|---|---|---|---|---|
| 知乎热榜 | 401 | 401（hotList 不在 HTML）| 已知可 | 6/29 主人 CDP 抓 122 items |
| 微博热搜 | 403 | 触发登录墙 | 已知可 | 6/29 主人 CDP 抓 70w 播放视频 |
| 小红书 | 触发登录墙 | 触发登录墙 | 已知可 | 6/29 主人 CDP 抓 122 items |
| 闲鱼 | API 失效 | 没试 | 已知可 | 6/29 主人 CDP 抓 54 items |
| 京东 | 重定向登录 | 没试 | 未知 | — |
| 淘宝 | 触发登录墙 | 没试 | 未知 | — |
| B 站 | ✅ 100 条 | — | — | **唯一裸抓可用的** |

## 1. 多 agent 集群拓扑（推荐）

```
                  claude-desktop (调度)
                  ↙      ↓      ↘
        Hermes A       Hermes B       Hermes C
        知乎+微博      小红书+抖音     京东+淘宝
        (独立IP)       (独立IP)        (独立IP)
```

| Agent | 平台 | 工具 |
|---|---|---|
| claude-desktop（我）| HN/GitHub/B 站 | Python urllib |
| Hermes A | 知乎 + 微博 | Playwright + Edge CDP |
| Hermes B | 小红书 + 抖音 | Playwright + Edge CDP |
| Hermes C | 京东 + 淘宝 + 闲鱼 | Playwright + Edge CDP |

**关键**：
- 每个 agent 独立 IP / Cookie 池
- 每个 agent 一个失败不影响其他
- claude-desktop 调度，5 分钟聚合一次

## 2. 前提条件

### 2.1 必须有的

- **主人 1 个登录态**：主人开 Chrome 远程端口（`chrome.exe --remote-debugging-port=9222`），所有 agent 都连这一个
- 或 **每个 agent 一个 Cookie**（多账号池）

### 2.2 已有的

- ✅ Hermes 装了 Playwright Python（`D:\OpenClaw-Hermes-Portable\hermes-agent\.venv-new\Lib\site-packages\playwright`）
- ✅ 系统 Edge（`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`）能用
- ❌ Playwright 自带的 chromium 二进制没装（用系统 Edge 替代）
- ✅ claude-desktop 的 Python urllib 跑海外 3 源稳定

### 2.3 缺的

- ❌ **主人 Chrome 远程端口未开**
- ❌ **主人 4 平台 Cookie 未提供**
- ❌ **多账号 Cookie 池**（防封号）

## 3. 三种实施路径

### 路径 A：主人开 CDP（推荐，立即可试）

```bash
# 主人跑
chrome.exe --remote-debugging-port=9222
# 或
msedge.exe --remote-debugging-port=9222

# 我（claude-desktop）跑
python -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://127.0.0.1:9222')
    page = browser.contexts[0].pages[0]
    # 抓任何主人登录的平台
"
```

- 优点：真实，主人已登录
- 缺点：主人 Chrome 一直开

### 路径 B：主人提供 Cookie（次推荐）

```bash
# 主人从 Chrome DevTools 复制 Cookie
# 存到 G:\个人项目\AI工具\codex\references\cookies\zhihu.json
{
  "name": "z_c0",
  "value": "...",
  "domain": ".zhihu.com"
}
```

- 优点：后台跑
- 缺点：Cookie 过期（7-30 天），要换

### 路径 C：只跑海外 + B 站（最稳）

- HN / GitHub（已跑）
- B 站 100 条（已跑，95% 娱乐）
- 找主人要 X API / Reddit API
- **放弃国内 4 平台**

- 优点：稳
- 缺点：错过国内搞钱机会

## 4. 当前可立即开干的

### 4.1 claude-desktop（我）+ 1 个新 agent

如果主人愿意：
1. **主人开 Edge 远程端口**（`--remote-debugging-port=9222`）
2. 我写 1 个 Python 脚本（multi-agent 雏形）：连 CDP，每平台 1 个 worker
3. **2 小时内能跑通 1 个平台**（知乎 OR 微博 OR 小红书任选）

### 4.2 时间表

| 步骤 | 时间 | 主人要做 |
|---|---|---|
| 主人开 Edge 远程端口 | 30 秒 | 命令 |
| 我写 1 个 CDP worker | 10 分钟 | 不用 |
| 试抓知乎热榜 | 5 分钟 | 不用 |
| 推广到 4 平台 | 30 分钟 | 不用 |
| 主人看效果 | — | 看日报 |
| 加 cron 定时 | 10 分钟 | 不用 |

**总耗时：1 小时内能跑起来**。

## 5. 风险

1. **主人 Chrome 关了 → 全部抓取停止**（CDP 路径）
2. **4 平台同时封 1 个 IP**（多 IP 池才有解）
3. **Codex 恢复后跟 Hermes 抢工具**（Playwright 在 Hermes 内，Codex 沙箱读不到）

## 6. 结论

**能行**，但需要主人 1 个动作：**开 Chrome/Edge 远程端口**（或提供 4 平台 Cookie）。

不开的话：
- 国内 4 平台：抓不到
- 海外 4 源（HN/GitHub/B 站/X/Reddit）：claude-desktop 已经能跑前 3 源

主人开不开 Edge 远程端口？

---

**附：实测过的细节**

- Hermes 装的 playwright 版本：`playwright._impl._errors.Error: BrowserType.launch: Executable doesn't exist at D:\OpenClaw-Hermes-Portable\hermes-data\ms-playwright\chromium-1223\chrome-win64\chrome.exe`
- 用系统 Edge 替代：`executable_path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'`
- Edge 启动参数：`--no-sandbox --disable-gpu`
- headless=true 跑得通，但国内平台触发登录墙
- 主人 QQ 浏览器路径找不到（`C:/Program Files (x86)/Tencent/QQBrowser/QQBrowser.exe` 不存在）
- Hermes WebUI 鉴权 4 种方式都 401
