# 物流知识库系统实现计划

> 2026-06-25 | 来源: `wechat-daily/docs/superpowers/plans/`
> 配套设计: [[Hermes-knowledge-base-design]]

---

## 目标

在现有日报系统中构建物流知识库——自动从群聊提取报价/货物/问题/决策，与市场基准价和外部事件对比，沉淀可查询的知识库。

## 架构

9 张新表（local_db.py schema 扩展）→ AI prompt 增强（analyzer.py 提取物流字段）→ KnowledgeEngine（knowledge_engine.py 保存结构化数据）→ EventMonitor（event_monitor.py 采集外部事件）→ 报告增强（report_generator.py 显示知识看板）

**技术栈：** Python 3.10+, SQLite, Pillow, openai SDK, WebSearch

---

## 文件结构

| 文件 | 操作 | 职责 |
|------|------|------|
| `src/local_db.py` | 修改 | 新增 9 张表的 schema + CRUD 方法 |
| `src/analyzer.py` | 修改 | prompt 增加 logistics/price/decisions 提取指令 |
| `src/knowledge_engine.py` | 创建 | 接收 AI 分析结果，写入知识库，问题匹配，价格对比 |
| `src/event_monitor.py` | 创建 | WebSearch 采集物流政策新闻，AI 提取事件，写入库 |
| `src/report_generator.py` | 修改 | 集成 knowledge_engine，日报底部加知识看板 |
| `tests/test_knowledge_engine.py` | 创建 | KnowledgeEngine 单元测试 |
| `tests/test_event_monitor.py` | 创建 | EventMonitor 单元测试 |

---

## 7 个任务

### 任务 1：local_db.py — 新增 9 张表 schema

- 在 `_ensure_schema` 末尾追加表创建语句
- 添加 CRUD 辅助方法（insert_logistics_object, upsert_issue, insert_decision 等）
- 初始化种子数据（7 个车型基准记录）
- 验证：`python -c "from local_db import LocalDB; ..."` → OK: 7

### 任务 2：analyzer.py — Prompt 增强

在现有的 JSON 输出格式中追加：
```json
{
  "logistics_objects": [{ "type": "quote|cargo|shipment", "attributes": {...} }],
  "price_comparison": { "market_price": "...", "contract_price": "...", "quoted_price": "...", "margin": "..." }
}
```

### 任务 3：knowledge_engine.py — KnowledgeEngine 类

核心功能：
- `save_logistics_object()` — 保存物流对象 + 属性
- `process_issues()` — 问题去重合并（Jaccard 相似度 > 0.3）
- `process_decisions()` — 决策沉淀
- `compare_price()` — 三层价格对比，计算利润率
- `process_group_analysis()` — 统一入口，处理整组分析结果

### 任务 4：report_generator.py — 集成

- AI 分析完成后调用 `KnowledgeEngine.process_group_analysis()`
- 日报底部新增知识看板：

```
📊 物流知识库本期沉淀
  - 报价/货物记录: N 条
  - 问题跟踪: N 个
  - 决策记录: N 条
  - 价格比对: 莫斯科线路 6000(市场) vs 4200(合约) → 利润30%

🌐 外部事件待确认 (N条)
  - [未确认] EAC认证新增品类要求 → 影响: 电子产品认证+15天
```

### 任务 5：event_monitor.py — 外部事件自动采集

- 9 个监测关键词（俄罗斯清关新政、EAC认证变化、中俄铁路运价等）
- WebSearch → AI 提取结构化事件 → 写入 external_events (confirmed=0)
- 日报时推送待确认事件列表

### 任务 6：事件采集触发集成

- 每周一触发一次外部事件搜索
- 新事件自动入库，用户在日报中确认

### 任务 7：端到端集成验证

1. 运行一次日报生成
2. 查询各表确认数据已写入
3. 验证 vehicle_types 种子数据 = 7 条

---

## 匹配策略

Issue 匹配采用组合策略（不引入额外依赖）：
- 同群 + 问题文本前 40 字 Jaccard 相似度 > 0.3 → 视为同一问题
- 匹配到 → 追加 issue_updates 时间线
- 未匹配 → 新建 issue

### 碎片化信息拼接

同一条物流对象的多次提及通过以下方式关联：
- 同群 + 相同货物特征（尺寸/重量/目的地匹配）
- 时间窗口（7 天内同一发件人讨论的同一批货）
- 群内 @ 关系链
