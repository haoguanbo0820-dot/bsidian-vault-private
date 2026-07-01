# Handoff to Hermes: 抢单协议 v2 上线

- **From**: claude-desktop
- **Date**: 2026-07-01 16:30
- **Priority**: high
- **Task**: 接收抢单协议 v2，准备接微信/飞书/定时任务
- **Context**: 主人批准分工方案 B（任务队列 + 抢单），你要按新机制干活
- **Expected Output**: 你启动后扫 QUEUE.json 抢单 + 更新 HEARTBEAT.md
- **Deadline**: 2026-07-01 18:00
- **Depends on**: 无
- **Notes**: 见下方详细说明

---

## 你需要做的事

### 1. 启动时执行（你那边可以加个 cron 每 5 分钟跑）

```python
# 你的启动脚本里加这段
import json, time, os
from datetime import datetime

VAULT = "/d/ObsidianVault/Coordination"

# 1. 更新心跳
def update_heartbeat():
    content = open(f"{VAULT}/HEARTBEAT.md", encoding="utf-8").read()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_content = re.sub(
        r"\| \*\*Hermes\*\* \|.*?\|",
        f"| **Hermes** | {now} | 🟢 active | - | 阿里云 39.105.115.6 | 24h 跑 |",
        content
    )
    atomic_write(f"{VAULT}/HEARTBEAT.md", new_content)

# 2. 扫队列抢单
def grab_task(my_skills=["wechat", "feishu", "scheduled_task", "aliyun", "bot"]):
    queue = json.load(open(f"{VAULT}/QUEUE.json", encoding="utf-8"))
    for task in queue["tasks"]:
        if task["status"] != "pending":
            continue
        if any(s in task["required_skills"] for s in my_skills):
            task["status"] = "locked"
            task["locked_by"] = "Hermes"
            task["locked_at"] = datetime.now().isoformat()
            atomic_write(f"{VAULT}/QUEUE.json", json.dumps(queue, indent=2, ensure_ascii=False))
            verify = json.load(open(f"{VAULT}/QUEUE.json", encoding="utf-8"))
            actual = next(t for t in verify["tasks"] if t["id"] == task["id"])
            if actual["locked_by"] == "Hermes":
                execute(task)
                return task
    return None

update_heartbeat()
grab_task()
```

### 2. 你的必抢技能

- `wechat` — 微信相关
- `feishu` — 飞书机器人
- `scheduled_task` — 定时任务
- `aliyun` — 阿里云部署
- `bot` — 机器人

### 3. 当前待抢任务

扫 `QUEUE.json`：
- T-20260701-001 (web_scrape) — 不匹配
- T-20260701-002 (handoff/vault_write) — 不匹配

**今天你没要干的活**（如果有，我会入队）。

### 4. 你可以建议新任务

如果你发现主人需要 24h 类活，写到 `QUEUE.suggested.json`。

---

## 新机制的核心变化（vs 旧版）

| 旧版 | 新版 v2 |
|---|---|
| 主人或我写 handoff → 你启动时读 | 你主动扫队列抢单 |
| 你不启动就不干活 | 你启动自动抢 |
| 撞车靠人手仲裁 | 原子写自动抢 |

---

## 你和我的边界

- **你专长**：24h 跑、定时任务、微信/飞书、阿里云
- **我专长**：Vault 整理、写文档、写代码、抓数据、跑日报
- **撞车规则**：如果都有技能匹配 → 谁先 atomic write 谁赢
- **超时处理**：任务 deadline 过期 1 小时未完成 → 我接过去重派

---

## 相关文档

- [[../分工设计-2026-07-01]] — 总设计
- [[../HEARTBEAT]] — 心跳
- [[../QUEUE]] — 任务队列

---

**确认收到请回执**：HEARTBEAT.md 更新你最后心跳时间。

claude-desktop
2026-07-01 16:30