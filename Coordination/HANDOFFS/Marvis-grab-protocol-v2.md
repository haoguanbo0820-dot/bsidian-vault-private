# Handoff to Marvis: 抢单协议 v2 上线

- **From**: claude-desktop
- **Date**: 2026-07-01 16:30
- **Priority**: high
- **Task**: 接收抢单协议 v2，准备接 Android 类任务
- **Context**: 主人批准分工方案 B（任务队列 + 抢单），你要按新机制干活
- **Expected Output**: 你启动后扫 QUEUE.json 抢单 + 更新 HEARTBEAT.md
- **Deadline**: 2026-07-01 18:00
- **Depends on**: 无
- **Notes**: 见下方详细说明

---

## 你需要做的事

### 1. 启动时执行

```python
# 你的启动脚本里加这段
import json, time, os
from datetime import datetime

VAULT = "/d/ObsidianVault/Coordination"

# 1. 更新心跳
def update_heartbeat():
    content = open(f"{VAULT}/HEARTBEAT.md", encoding="utf-8").read()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    # 替换 Marvis 那一行的"最后心跳"
    new_content = re.sub(
        r"\| \*\*Marvis\*\* \|.*?\|",
        f"| **Marvis** | {now} | 🟢 active | - | 本地 | 启动中 |",
        content
    )
    atomic_write(f"{VAULT}/HEARTBEAT.md", new_content)

# 2. 扫队列抢单
def grab_task(my_skills=["android", "adb", "ocr", "app_automation", "chat_extract"]):
    queue = json.load(open(f"{VAULT}/QUEUE.json", encoding="utf-8"))
    for task in queue["tasks"]:
        if task["status"] != "pending":
            continue
        if any(s in task["required_skills"] for s in my_skills):
            # 抢单：原子写 + 验证
            task["status"] = "locked"
            task["locked_by"] = "Marvis"
            task["locked_at"] = datetime.now().isoformat()
            atomic_write(f"{VAULT}/QUEUE.json", json.dumps(queue, indent=2, ensure_ascii=False))
            # 验证抢到
            verify = json.load(open(f"{VAULT}/QUEUE.json", encoding="utf-8"))
            actual = next(t for t in verify["tasks"] if t["id"] == task["id"])
            if actual["locked_by"] == "Marvis":
                execute(task)
                return task
    return None

update_heartbeat()
grab_task()
```

### 2. 你的必抢技能

- `android` — Android 自动化
- `adb` — ADB 控制
- `ocr` — OCR 识别
- `app_automation` — App UI 自动化
- `chat_extract` — 聊天记录提取

### 3. 当前待抢任务

扫 `QUEUE.json`，看有没有匹配你技能的 `pending` 任务：
- T-20260701-001 (web_scrape) — 不匹配你的技能 → 不抢
- T-20260701-002 (handoff/vault_write) — 不匹配你的技能 → 不抢

**所以你今天没有要干的活**（如果有，我会入队）。

### 4. 你可以建议新任务

如果你发现主人需要 Android 类活（比如钉钉同步、微信抓数据），写：

```json
// Coordination/QUEUE.suggested.json
{
  "suggestions": [
    {
      "id": "S-MARVIS-001",
      "title": "跑钉钉 6/30 同步",
      "required_skills": ["android", "ocr"],
      "reason": "主人提到钉钉未同步",
      "suggested_by": "Marvis",
      "suggested_at": "2026-07-01T..."
    }
  ]
}
```

claude-desktop 或主人审核后会转正到 QUEUE.json。

---

## 新机制的核心变化（vs 旧版）

| 旧版 | 新版 v2 |
|---|---|
| 主人或我写 handoff → 你启动时读 | 主人或我入队 → 你主动扫队列抢单 |
| 你不启动就不干活 | 你启动自动抢，不用等人派 |
| 撞车靠人手仲裁 | 原子写自动抢，第二个看到 locked 就让 |

---

## 相关文档

- [[../分工设计-2026-07-01]] — 总设计
- [[../HEARTBEAT]] — 心跳
- [[../QUEUE]] — 任务队列
- [[./T-20260701-002]] — 本次任务的 handoff

---

**确认收到请回执**：HEARTBEAT.md 更新你最后心跳时间。

claude-desktop
2026-07-01 16:30