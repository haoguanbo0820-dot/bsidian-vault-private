---
title: OpenJarvis 本地安装记录 2026-07-01
agent: claude-desktop
date: 2026-07-01
status: Python 链路通；Rust 扩展待定
tags: [openjarvis, local-ai, install, gh-proxy]
---

# OpenJarvis 本地安装记录

## 仓库

- GitHub: `open-jarvis/OpenJarvis`（Stanford SAIL 出品，PyTorch 风格的 local-first personal AI）
- clone 到：`G:\个人项目\AI工具\OpenJarvis`（深度 1, branch main, 2030 文件 / 12s via gh-proxy）
- 仓库规模：Python orchestrator + 18 个 Rust crate + TS frontend + desktop 壳

## 探针确认

| 工具 | 版本 | 备注 |
|------|------|------|
| Python | 3.13.3 | 3.10–3.13 范围内（pyproject cap <3.14） |
| uv | 0.11.19 | |
| rustc | 1.96.0 | workspace 要求 ≥1.88，OK |
| node | v24.16.0 | |
| pnpm | 11.9.0 | |
| PyPI 清华源 | 0.3s | 比官方 1.2s 快 4×，已配 `uv` 默认走清华 |

## 已完成

1. `uv sync --extra dev` 装通 — 79 包（含 maturin 1.12.6, pytest 全家桶, ruff, pre-commit）
2. `uv sync --extra dev --extra server --extra framework-comparison --extra pdf --extra memory-bm25` 装可选 — 14 包（fastapi/uvicorn/polars/rank-bm25/pdfplumber/cryptography）
3. `uv run jarvis --version` → `0.0.1.dev1+unknown.gd865b4bed`（vcs 版本，从 git describe 来）
4. `uv run jarvis --help` → 26 个子命令全挂得上（chat/agents/bench/eval/host/init/memory/optimize/pearl/registry/research/scan/...）
5. `uv run jarvis doctor` → 全维诊断跑通。cloud reachable ✓，其他 14 个本地引擎（ollama/vllm/llamacpp/...）unreachable 是预期
6. 烟测：236 tests passed / 1 skipped / 62 deselected（5.97s collect）

## 已知阻塞

### 1. Rust 扩展 `openjarvis_rust` 缺

- 触发：`from openjarvis.tools.storage.bm25 import BM25Memory` → `import openjarvis_rust` → ModuleNotFoundError
- 影响：`tests/memory/test_bm25.py` 整文件不能 collect
- 触发面：
  - `tests/agents/test_loop_guard.py::test_identical_calls_blocked` 失败（注释明说 "Rust backend uses a HashSet"）
  - `src/openjarvis/_rust_bridge.py:30` 走 `import openjarvis_rust`
- 修法（未做）：`maturin develop -m rust/crates/openjarvis-python/Cargo.toml`，会触发 18 个 crate workspace 全量编译（5-15 min）
- 决策：**先不动**。需要 desktop extra（`--extra desktop`）或想跑 Rust 加速路径时再 build

### 2. desktop extra 缺 `faster-whisper` 等

- `jarvis doctor` 报：speech backend unavailable → 需 `--extra desktop`
- desktop extra 显式依赖 `openjarvis-rust`，所以同样卡在 Rust 编译
- 暂不处理

### 3. pytest 选集在 -x 下到 `test_loop_guard` 卡住

- 单测已 236 个 pass，环境基本 OK
- 跑全量需先 deselect Rust 依赖测试或先 build Rust

## 沙盒 vs 本地终端分工

**关键发现**：Claude Desktop sandbox 只挂载 C/D 盘，**G 盘不可见**。之前 `cd "G:\..."` 看起来成功的命令其实是用户在本地 PowerShell 粘贴跑的（从提示符 `PS C:\Users\hao>` 可看出），不是 sandbox 真跑了。

**新规则**：
- sandbox 跑通/失败的判断只看 exit code 0
- G 盘操作必须打包成 PowerShell 块让用户本地跑
- 用户说"自去研究执行"=先 sandbox 试 + 必要时把命令块贴给用户

## 关键命令（用户本地粘）

```powershell
# G 盘 → 装可选 + 跑 pytest（跳 Rust 依赖）
cd "G:\个人项目\AI工具\OpenJarvis"
uv sync --extra dev --extra server --extra framework-comparison --extra pdf --extra memory-bm25
uv run pytest tests/ `
  -m "not hub and not live and not slow and not docker and not apple and not macos and not amd and not nvidia and not modal and not live_channel and not live_external" `
  --ignore=tests/memory/test_bm25.py `
  --deselect "tests/agents/test_loop_guard.py::TestLoopGuard::test_identical_calls_blocked" `
  --tb=short -q

# 想跑 Rust 加速路径（5-15 min 编译）
cd "G:\个人项目\AI工具\OpenJarvis"
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml --uv
uv run pytest tests/memory/test_bm25.py -v
```

## 链接

- [[GH代理路径记录]] — gh-proxy 经验
- [[多Agent沙盒行为记录]] — sandbox 只挂 C/D，G 盘用户本地
