# WeChat 消息持久化同步与自动汇报系统 — 实现计划

> 2026-06 | 原始计划 | 来源: `sprightly-foraging-wreath.md`

---

## Context

现有的日报系统已能读取微信 4.x 数据库生成日报，但存在两个问题：(1) 每次运行都要重新解密数据库，速度慢且依赖微信进程；(2) 没有历史消息持久化存储，无法做周报/月报。需要用本地 SQLite 数据库持久化所有消息，并实现自动同步和周期汇报。

## 架构总览

```
┌─────────────────────────┐     ┌──────────────────────┐
│  WeChat 加密 DB         │────▶│  本地 SQLite          │
│  (db_storage/)          │     │  D:\wechat_daily\    │
│  传参 passphrase 解密     │     │  wechat_data.db      │
└─────────────────────────┘     └──────────┬───────────┘
                                           │
                    ┌──────────────────────┼──────────────────────┐
                    │                      │                      │
                    ▼                      ▼                      ▼
          每日报告 (16:00)         每周汇总 (周六)         月度汇报 (1日)
          daily\                   weekly\                 monthly\
```

## 新增文件

| 文件 | 作用 |
|------|------|
| `src/local_db.py` | SQLite 数据库管理：建表、批量插入、按群+时间范围查询 |
| `src/sync_engine.py` | 离线同步引擎：从加密 DB 增量同步到本地 SQLite |
| `src/report_generator.py` | 统一报告生成器：daily/weekly/monthly 三种模式 |
| `sync.py` | 同步入口（给 Task Scheduler 调用） |
| `report_runner.py` | 报告入口（给 Task Scheduler 调用） |
| `setup_scheduled_tasks.bat` | 一键创建 Windows 计划任务 |

## 技术要点

### 增量同步方案
- `sync_cursors` 表记录每个 room_wxid 的 `last_message_ts`
- 每次同步只拉取 `create_time > last_message_ts` 的消息
- 同步完成后更新 `last_message_ts = max(create_time)`

### 数据库 schema
```sql
CREATE TABLE rooms (
    room_wxid TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    config_name TEXT
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_wxid TEXT NOT NULL,
    create_time INTEGER NOT NULL,
    sender_name TEXT NOT NULL DEFAULT '',
    message_content TEXT NOT NULL,
    is_sender INTEGER NOT NULL DEFAULT 0,
    synced_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX idx_msgs_room_time ON messages(room_wxid, create_time);

CREATE TABLE sync_cursors (
    room_wxid TEXT PRIMARY KEY,
    last_message_ts INTEGER DEFAULT 0,
    last_run TEXT
);
```

### 三种报告模式

| 模式 | 时间范围 | 输出路径 | AI 提示差异 |
|------|---------|---------|------------|
| daily | 昨天 16:00 ~ 今天 16:00 | `reports/daily/YYYY-MM-DD-日报.md` | 现有 prompt |
| weekly | 本周一 ~ 本周日 | `reports/weekly/YYYY-Www-周报.md` | 增加趋势分析、跨团队协作 |
| monthly | 本月 1 日 ~ 本月末日 | `reports/monthly/YYYY-MM-月报.md` | 增加里程碑、KPI 汇总、下月规划 |

### Windows 计划任务

```
WeChatDaily\Sync         开机启动  → sync.py
WeChatDaily\DailyReport  每天 16:00 → report_runner.py --period daily
WeChatDaily\WeeklyReport 每周六 12:00 → report_runner.py --period weekly
WeChatDaily\MonthlyReport 每月1日 10:00 → report_runner.py --period monthly
```

## 验证方法

1. **冷启动验证**：删除 `D:\wechat_daily\`，运行 `sync.py`，确认本地 DB 创建并有消息
2. **增量验证**：再次运行 `sync.py`，确认新消息数为 0（或很少）
3. **每日报告验证**：运行 `report_runner.py --period daily`，检查输出 Markdown
4. **周报验证**：运行 `report_runner.py --period weekly`，检查报告完整性
5. **任务验证**：运行 `setup_scheduled_tasks.bat`，检查计划任务列表
6. **离线验证**：关闭微信，运行 `sync.py`，确认仍然能同步（使用已保存的 passphrase）
