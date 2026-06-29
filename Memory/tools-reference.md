# 参考: 工具与 API 速查

> 从 Hermes MEMORY.md 提取（2026-06-29）
> 跨 Agent 通用工具信息

## pandoc

- 版本: 3.10
- 路径: `C:/Users/hao/AppData/Local/Microsoft/WinGet/Packages/JohnMacFarlane.Pandoc_Microsoft.Winget.Source_8wekyb3d8bbwe/pandoc-3.10/pandoc.EXE`
- docx→md: `pandoc src.docx -t gfm -o dst.md`

## OpenMAIC API

- 启动: `cd G:/openmaic && pnpm dev` → :3000
- 端点: `/api/generate/scene-outlines-stream`
- Body: `{"requirements": {"requirement":"...","userNickname":"...","webSearch":false}}`
- SSE: `data:{type:languageDirective|courseTitle|outline, data:...}`
- MiniMax-M3 Stage 1: 23 scenes 65s

## Hermes 阿里云

- IP: 39.105.115.6
- 端口: 9119

## 扫文件过滤规则

忽略: `.lnk` / `desktop.ini` / `~$*` / `__pycache__/*.pyc`
