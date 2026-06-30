# Android 聊天记录提取 SOP

> 无需破解加密，通过 MuMu 模拟器 + ADB + OCR 提取钉钉/微信消息到 vault
> 由 Marvis (`chat_extractor.py`) 执行

## 原理

```
MuMu 模拟器 (钉钉/微信)
  ↓ ADB 截图
PaddleOCR 识别文字
  ↓ 去重 + 合并
Obsidian Vault (Markdown)
```

对比桌面端的优势：Android App 的 UI 是可见的，不需要解密本地数据库。

## 前置条件

1. MuMu 模拟器已启动，ADB 已连接 (`adb devices`)
2. 模拟器中已安装**钉钉**和/或**微信**并已登录
3. Python 环境有 `paddlepaddle` + `paddleocr`

## 运行

```bash
cd G:/模拟器+agent/marvis

# 提取钉钉
python run_extract.py dingtalk

# 提取微信
python run_extract.py wechat

# 全部
python run_extract.py all
```

## 流程

1. 打开 App → 处理弹窗
2. 扫描对话列表（uiautomator2 控件树）
3. 逐个进入对话 → 向上滚动加载历史 → 截图 → OCR
4. 去重合并 → 写入 `D:/ObsidianVault/Imports/{钉钉|微信}/`
5. 返回对话列表 → 下一个

## 参数

可在 `chat_extractor.py` 的 `extract_app()` 中调整：
- `max_conversations=10` — 最多提取几个对话
- `scrolls_per_chat=5` — 每个对话向上滚几次

## 输出

```
D:/ObsidianVault/Imports/
├── 钉钉/
│   ├── CEL畅达工作群-2026-06-30.md
│   ├── 物流协调群-2026-06-30.md
│   └── ...
└── 微信/
    ├── 彭总-2026-06-30.md
    └── ...
```

## 定时执行

通过 Marvis Scheduler 或 Windows 任务计划：

```powershell
schtasks /create /tn "聊天记录提取" /tr "python G:\模拟器+agent\marvis\run_extract.py all" /sc daily /st 09:00
```
