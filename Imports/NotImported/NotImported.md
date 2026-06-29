# 没进 vault 的文件清单 (NotImported)

> 维护: 2026-06-29
> 用途: 告诉主人哪些文件**没**进 vault, 以及为什么

## 跳过原因: 太大 (>10MB)

| 原文件 | 大小 | 原因 |
|--------|------|------|
| `C:/Users/hao/Desktop/CEL文件/ozon/OZON客诉SOP.docx` | 14.6MB | 单文件超限 |
| `C:/Users/hao/Desktop/CEL文件/ozon/2026年4月罚款/...` | 100+ MB | 单文件超限 |
| `C:/Users/hao/Desktop/CEL文件/ozon/2026年5月罚款/...` | 100+ MB | 单文件超限 |
| `C:/Users/hao/Downloads/765..._record_audio.m4a` × 9 | 200MB | 录音, 大 |
| `C:/Users/hao/Downloads/Hermes.Studio...exe` | 130MB | 安装包 |
| `C:/Users/hao/Downloads/ToDesk_Setup.exe` | 92MB | 安装包 |

## 跳过原因: 重复 3 份 (解压/未解压/原名)

280+ 个 `CEL文件/ozon/2026年抵扣赔偿/` PDF 扫描件, 3 个文件夹完全一样。
理由: 历史归档, 不需要 vault 重复; 保留在原位置

## 跳过原因: 跟项目无关

| 文件 | 原因 |
|------|------|
| `Desktop/aero_hand_preview/*.png` (8 个) | 3D 打印项目, 跟跨境/自媒体无关 |
| `Desktop/CEL文件/ozon/第一季度*/...xlsx` (4 个 22-100MB) | 历史数据导出, 已归档 |
| `Desktop/CEL文件/ozon/2026年*月罚款/*原表-4月/...xlsx` (6 个 100+MB) | 历史数据导出, 已归档 |

## 跳过原因: 敏感

见 `Imports/Sensitive/` (已隔离)

## 跳过原因: 临时工具

- `transcribe_*.py` (5 个 ffmpeg 包装脚本) - 一次性使用
- `setup_ffmpeg.py` / `install_ffmpeg.py` - 已完成
- `generate_weekly_report.py` - 待主人确认是否有用
- `C盘一键优化.bat` - 临时
- `~$26-06-运营问题通报-会议版.docx` - Office 临时文件
