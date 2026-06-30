# 钉钉/微信消息同步到 Vault

> 最终方案：MuMu 模拟器 + ADB + OCR（无需 API、无需解密）

## 探索结论（2026-06-30）

| 方法 | 状态 | 原因 |
|------|------|------|
| 本地数据库 `dingtalk.db` | ❌ | SQLCipher 加密 |
| 网页版 `im.dingtalk.com` | ❌ | 已下线 |
| CEF 调试端口 | ❌ | 未启用 |
| 开放平台 API | ❌ | 非管理员账号 |
| **Android 模拟器 + OCR** | ✅ | UI 层文本可见，无需解密 |

## 当前方案

Marvis `chat_extractor.py` — 通过 ADB 操控 MuMu 模拟器中的钉钉/微信 App，截图后用 PaddleOCR 提取文字：

```bash
cd G:/模拟器+agent/marvis
python run_extract.py dingtalk   # 钉钉
python run_extract.py wechat     # 微信
python run_extract.py all        # 全部
```

输出路径: `D:/ObsidianVault/Imports/{钉钉|微信}/`

详见 [[SOP/android-chat-extract|Android 聊天提取 SOP]]

## 脚本文件

| 文件 | 用途 |
|------|------|
| `G:/模拟器+agent/marvis/chat_extractor.py` | 核心提取逻辑 |
| `G:/模拟器+agent/marvis/run_extract.py` | 命令行入口 |
| `G:/模拟器+agent/marvis/device.py` | ADB 设备控制 |
| `G:/模拟器+agent/marvis/ocr.py` | PaddleOCR 封装 |

## 废弃方案

- `D:/claude desktop/dingtalk-sync/` — API 方案（已放弃，凭据无效）
- webhook-server.js — Outgoing 机器人（可作为实时补充）
