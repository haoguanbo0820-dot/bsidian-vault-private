# Hermes 自动回复系统

> P0 项目：物流群 AI 助理
> 代码：`D:\wechat_daily\auto_reply\`
> 状态：🟡 开发中

## 架构

```
微信消息 → monitor.py (监听新消息)
       → classifier.py (5 类：报价/查单/政策/催办/其他)
       → generator.py (Claude API 生成回复)
       → dedup.py (5 分钟内不重复)
       → sender.py (微信 hook 发送)
```

## 项目结构

```
auto_reply/
├── config.py              # 配置加载
├── models.py              # 数据类
├── db.py                  # 数据库工具
├── monitor.py             # 消息监听
├── classifier.py          # 问题分类（5 类）
├── generator.py           # Claude API 回复生成
├── sender.py              # 微信 hook 发送
├── dedup.py               # 去重
├── fallback.py            # Fallback 静态模板
├── main.py                # 主循环
├── migrations/            # SQL 迁移
├── prompt_templates/      # 5 个 system prompt
├── config/                # 配置文件示例
├── logs/                  # 日志
├── tests/                 # 6 个测试文件
└── requirements.txt
```

## 5 类问题自动识别

| 类别 | 关键词 | 典型问题 |
|------|--------|----------|
| 报价 | 报价/多少/价格/тариф | "到莫斯科什么价格" |
| 查单 | 订单 + 6-10 位数字 | "帮我查一下 54351129153" |
| 政策 | 政策/海关/清关/таможня | "现在俄罗斯海关什么政策" |
| 催办 | 什么时候/等到/急 | "这个什么时候能处理" |
| 其他 | 兜底 | 不匹配以上任何类别 |

## 安全约束

- 本地运行（不上云）
- 2-5 秒回复延迟（模拟人工）
- 不发营销内容
- 置信度 < 0.7 转人工
- 5 分钟内不重复回复

## 四周路线图

| 周 | 模块 | 功能 |
|----|------|------|
| Week 1 | auto_reply | 自动识别 + 回复（当前） |
| Week 2 | pricing_engine | 实时报价 |
| Week 3 | order_tracker | 自动查单 |
| Week 4 | alert_system | 预警系统 |

## 相关文档

- PRD: `D:\wechat_daily\PRD-AI-ASSISTANT-MISSING.md`
- 指令: `D:\wechat_daily\CLAUDE-CODE-INSTRUCTIONS.md`
- 启动: `D:\wechat_daily\启动Claude-Code-开发auto_reply.bat`
