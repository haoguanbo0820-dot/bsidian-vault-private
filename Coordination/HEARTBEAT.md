# Agent Heartbeat

> **更新规则**：每个 agent 每 5 分钟写一次自己的最后心跳时间
> **用途**：判断 agent 是否还活着 / 当前在干啥 / 撞车检测

## 当前状态

| Agent | 最后心跳 | 状态 | 当前任务 | 位置 | 备注 |
|---|---|---|---|---|---|
| **claude-desktop** | 2026-07-01 14:50 | 🟢 active | 修复 router + vault 审计 | 本地 | 主人 session 中 |
| **Codex 桌面 App** | 2026-07-01 14:50 | 🟢 active | MiniMax M3 (router :15888) | 本地 | 模型配置已切换 |
| **Marvis** | 2026-07-01 15:00 | 🟡 idle | - | 本地 | 待启动 |
| **Hermes** | 2026-07-01 16:00 | 🟢 active | (微信自动化) | 阿里云 39.105.115.6 | 24h 跑 |
| **Trae CN** | 2026-06-05 08:57 | ⚪ token=0 | - | 本地 | 主人未充值 |

## 状态说明

- 🟢 **active** — 5 分钟内有心跳，正在干任务
- 🟡 **idle** — 心跳正常但没任务
- 🔴 **down** — 心跳 > 30 分钟无更新 = 挂了
- ⚪ **disabled** — 配置/资源问题暂时不可用

## 心跳协议

每个 agent 启动时/每 5 分钟：

```python
def heartbeat():
    content = read("HEARTBEAT.md")
    # 更新自己的最后心跳时间
    content = replace_line(content, MY_NAME, now())
    write_atomic("HEARTBEAT.md", content)
    # 顺便扫一次队列
    queue = read("QUEUE.json")
    grab_task(MY_SKILLS)
```

## 死掉的判定

`HEARTBEAT.md` 上某 agent 最后心跳 > 30 分钟无更新 = 挂。
- claude-desktop 挂了 → 主人接管（30 分钟后无心跳主人接管）
- 其他 agent 挂了 → claude-desktop 兜底

---

**最近更新**：2026-07-01 16:30 by claude-desktop