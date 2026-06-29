# TMS 数据自动化项目

> 创建: 2026-06-29 | 状态: Phase 1 已跑通, Phase 2 待启动
> 来源: MEMORY.md (2026-06-15 "TMS 数据自动化") + Codex++ 实测结果

## 项目目标

**自动化从 TMS 系统导出报表 → 解析 → 生成日报 → 推送到主人**

省去每天手动导数据 + 整理的时间(估计每天 1 小时 → 5 分钟)。

## 关键事实(已验证)

- **TMS 路径**: `C:/Program Files (x86)/TMS/2.1.0.5/RTBsoft.TMSClient.Apps.exe`
- **TMS 远程 WCF**: `net.tcp://47.107.84.253:6011/IntegrateReportDelegate`
- **关键方法**: `FindReportMenu` / `SelectReportResult` / `ExecuteReportQueryPaging`
- **当前阻塞**: 版本检查 errMsg "当前客户端系统版本已过时",不在 SOAP 头而在消息体
- **可能绕过方案**: GUI 键盘自动化 (Ctrl+A Ctrl+C) / 中间人 WCF 代理 (MITM, **只读操作**)

## 已完成 (Phase 1 - 2026-06-15)

- ✅ 自动识别 9 个字段(中/英文同义词都识别)
- ✅ 状态/金额/重量/件数/渠道/国家/客户 全部统计
- ✅ 总金额 16062.5,平均 1606.25
- ✅ 前 10 条样本数据
- ✅ 自动归档 + 报告生成
- ✅ PowerShell watcher 持续运行
- 📂 Inbox: `G:/个人项目/AI工具/codex/TmsData/daily-exports/`

## 待做 (Phase 2)

- [ ] 挖 HTTP API 找到正确请求格式 → 切全自动
- [ ] 与 Hermes 集成(读 daily-exports → 自动出日报 → 推微信)
- [ ] 主人朋友圈/客户群的物流数据自动周报

## 历史踩坑

- 2026-06-15: 装 Excel 模块太慢 → 改用已可用的 Office.Interop.Excel
- 2026-06-15: PowerShell 5 解析错误(.Count 空格问题) → 修
- 2026-06-15: Event handler 没触发 → 改轮询模式
- 2026-06-15: 主人纠正"不是让你生成日报,是让你了解各报表怎么导" → **用户偏好**: 不要自己拍脑袋跑,要先理解需求

## 关键决策

- ✅ **MITM 只读**是允许的(只查报表,不写数据)
- ✅ Phase 1 已稳定 → 2026-06-15 完成
- ⏳ Phase 2 等主人安排(他自己研究 API)

## 相关文件

- `G:/个人项目/AI工具/codex/TmsData/` (数据 inbox)
- `G:/个人项目/AI工具/codex/research/` (TMS 逆向笔记)
- 阿里云 39.105.115.6 也有相关运行
