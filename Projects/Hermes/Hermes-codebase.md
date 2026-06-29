# Hermes 代码 & 脚本

> Hermes 相关的全部可执行资产

## 自动回复系统

代码位置：`D:\wechat_daily\auto_reply\`

| 文件 | 功能 |
|------|------|
| `main.py` | 主循环入口 |
| `monitor.py` | 监听 messages 表新消息 |
| `classifier.py` | 5 类问题分类（报价/查单/政策/催办/其他） |
| `generator.py` | Claude API 调用生成回复 |
| `sender.py` | 微信 hook 发送 |
| `dedup.py` | 5 分钟内去重 |
| `fallback.py` | API 失败时静态模板兜底 |
| `config.py` | 配置加载 |
| `models.py` | 数据模型 |
| `db.py` | 数据库操作 |
| `migrations/` | SQL 迁移脚本（2 张新表） |
| `prompt_templates/` | 5 个分类的 system prompt |
| `tests/` | 6 个单元测试 |
| `requirements.txt` | Python 依赖 |

启动方式：
```bash
cd D:\wechat_daily
.venv\Scripts\activate
py auto_reply.py               # 前台
pythonw auto_reply.py           # 后台
py auto_reply.py --check        # 环境检查
py auto_reply.py --test         # 分类器自检
```

## Hermes 维护脚本

位置：`D:\OpenClaw-Hermes-Portable\hermes-data\scripts\`

| 脚本 | 用途 |
|------|------|
| `smoke_test.py` | 启动前冒烟测试 |
| `reauth-and-restart.ps1` | 重新认证 + 重启 |
| `reauth-weixin.py` | 微信重新登录 |
| `scan_all_skills.py` | 扫描全部 skills |
| `scan_skills.py` | 扫描 skills |
| `patch_*.py` | 各类热修复脚本 |
| `fix_memory_*.py` | MEMORY 修复脚本（已不用） |
| `debug_drift.py` | 调试 drift 问题 |

## WeChat 辅助工具

位置：`D:\wechat_daily\`

| 文件 | 用途 |
|------|------|
| `auto_reply.py` | 自动回复入口 |
| `_db_check.py` | 数据库完整性检查 |
| `wechat_data.db` | 主数据库（13 表，724KB） |
| `启动Claude-Code-开发auto_reply.bat` | 一键启动 Claude Code 开发 |

## 设计文档

| 文件 | 说明 |
|------|------|
| `PRD-AI-ASSISTANT-MISSING.md` | 完整 PRD：现有功能 vs 缺失功能 |
| `CLAUDE-CODE-INSTRUCTIONS.md` | Claude Code 接手开发的启动指令 |
| `auto_reply/README.md` | auto_reply 项目 README |

## Hermes 配置

| 文件 | 说明 |
|------|------|
| `hermes-data/config.yaml` | 主配置 |
| `hermes-data/SOUL.md` | Hermes 人格定义 |
| `hermes-data/SHARED_MEMORY.md` | 共享记忆 |
| `hermes-data/team-agents.json` | 团队 Agent 配置 |
