# 灾难恢复手册 — 电脑挂了也能重建

> **作者**: 郝冠的 + claude-desktop
> **日期**: 2026-07-01
> **目的**: 电脑完全挂了（硬盘坏/重装/换电脑），从零恢复整个 AI 调度系统
> **目标**: 任何机器 + 任何人都能照着 1-2 小时搞定

---

## 1. 灾难前提

**最坏情况**：
- ❌ 硬盘损坏，系统全没
- ❌ 本地所有配置文件丢失
- ❌ D 盘、G 盘都不可访问
- ❌ 所有 Agent 软件都没装
- ✅ **唯一保留**：Obsidian Vault（已同步到 Gitee 私有仓）

**核心资产都在 vault 里**：
- 22+ 平台 API key 清单（README.md）
- 5 个 Agent 模型配置（ModelConfig + HANDOFFS）
- 任务队列/心跳协议（QUEUE/HEARTBEAT）
- 协调协议（CLAUDE.md）
- 决策日志（DECISIONS.md）

---

## 2. 备份清单（灾难前要确认）

### 已自动备份（推荐）

| 资产 | 备份位置 | 状态 |
|---|---|---|
| **Obsidian Vault** | Gitee `gitee.com/haowenzhuo/obsidian-vault.git` | ✅ 自动推 |
| **API Key 文档** | `G:/CC-Switch-v3.15.0-Windows-Portable.bak.20260627_130921/APIkey.docx` | ⚠️ 本地 G 盘，需手动备份到云盘 |

### ⚠️ 本地必须手动备份的（不然就丢）

| 资产 | 路径 | 备份方式 |
|---|---|---|
| API Key 原文档 | `G:/CC-Switch.../APIkey.docx` | 拷到云盘（OneDrive/百度网盘） |
| Claude Desktop 配置 | `C:/Users/hao/.claude/settings.json` | vault README.md 已记录内容 |
| Hermes 阿里云 SSH key | `C:/Users/Administrator/Downloads/openclaw0417.pem` | 拷到云盘 |
| 飞书 App1/2 secret | README.md 已记录 | — |
| 华为云 ECS API | README.md 已记录 | — |
| Codex 后端配置 | 不明（Codex GUI 桌面 app 内部） | ⚠️ 主人自己 GUI 备份 |

### 🔧 建议：每天自动跑备份（可选）

主人可以让我写一个 cron：
```python
# 每天 23:00 备份到云盘
# - vault 已自动推 Gitee
# - APIkey.docx + .pem + settings.json 拷到 D:/CloudBackup/
```

---

## 3. 恢复步骤（从零开始）

### 步骤 1：买新电脑 / 重装系统（30 分钟）

最低配置：
- Windows 11
- 8GB+ 内存
- 100GB+ 可用空间
- 能上网

### 步骤 2：装基础软件（30 分钟）

```powershell
# 必装
- Git              https://git-scm.com/download/win
- Python 3.11+     https://www.python.org/downloads/
- Node.js 20+      https://nodejs.org/
- VSCode           https://code.visualstudio.com/
- Obsidian         https://obsidian.md/download
- CC Switch        https://github.com/farion1231/cc-switch/releases
- Claude Desktop   https://claude.ai/download
- Claude Code CLI  npm i -g @anthropic-ai/claude-code
- ADB (Android)    https://developer.android.com/tools/releases/platform-tools

# 可选
- Trae CN          winget install Trae.CN
- Docker Desktop   https://www.docker.com/products/docker-desktop/
- Obsidian Git 插件（在 Obsidian 里装）
```

### 步骤 3：拉 Obsidian Vault（5 分钟）

```bash
mkdir D:/ObsidianVault
cd D:/ObsidianVault
git clone https://gitee.com/haowenzhuo/obsidian-vault.git .
# 输入 Gitee 用户名密码
```

**验证**：
```bash
ls D:/ObsidianVault/
# 应该看到：README.md CLAUDE.md Coordination/ Memory/ Projects/ SOP/ Imports/ Daily/
```

### 步骤 4：装各 Agent 软件（30 分钟）

#### 4.1 Claude Desktop（必须）

```powershell
# 1. 装 Claude Desktop
winget install Anthropic.ClaudeDesktop

# 2. 启动 Claude Desktop 一次（生成 settings 目录）
# 3. 关闭
# 4. 复制配置（从 vault 恢复）
# C:/Users/hao/.claude/settings.json 内容：

{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "PROXY_MANAGED",
    "ANTHROPIC_BASE_URL": "http://127.0.0.1:15721",
    "API_KEY": "sk-cp-xv9laq12ZSkVvPfOe3rUXeMeyIK4tX5mPiD2DjsK4Ee648MXJGu_9Eo0GPBC475PPvJFRYL5zTrW8N3gOrhg4p3FN5c5AKY6RY6dK3zWB-R6Y6o4K7Kknhw",
    "API_URL": "https://api.minimaxi.com/anthropic",
    "DEEPSEEK_API_KEY": "sk-7a94da46ef44467e97289151a111a2c4",
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com/anthropic",
    "VOLC_ARK_API_KEY": "api-key-20260308224717",
    "VOLC_ARK_BASE_URL": "https://ark.cn-beijing.volces.com/api/coding",
    "VOLC_ARK_MODEL": "ark-code-latest",
    "ZHIPU_API_KEY": "21f8cb4476a44c33be07613a5400b3af.au8UX7ZmAD5Wbo3c"
  },
  "theme": "dark"
}
```

#### 4.2 CC Switch（必须，M3 走它代理）

```powershell
winget install farion1231.cc-switch
# 启动 CC Switch，确保端口 15721 在跑
```

#### 4.3 Marvis（半自动）

```powershell
# Marvis 是腾讯 Android Agent
# 装 MuMu 模拟器 + Marvis APK
# 从 G:/模拟器+agent/marvis/ 备份恢复（如果有）
```

#### 4.4 Hermes（自动，24h 跑）

```bash
# Hermes 跑在阿里云 ECS（39.105.115.6），不需要重装
# 1. SSH 到阿里云：ssh -i openclaw0417.pem root@39.105.115.6
# 2. 检查：systemctl status hermes-agent
# 3. 启动（如果挂了）：systemctl start hermes-agent
```

⚠️ **关键**：`openclaw0417.pem` 必须先从云盘恢复！没有这个 key 进不了阿里云。

#### 4.5 Codex 桌面 App（主人 GUI 触发）

```powershell
winget install OpenAI.Codex
# 启动 Codex → Settings → API → 配 GLM 5.2
# 详细：Coordination/HANDOFFS/ModelConfig-Codex-2026-07-01.md
```

#### 4.6 Trae CN（主人 GUI + 充值）

```powershell
winget install Trae.CN
# ⚠️ 主人必须 GUI 充值（token=0 → 不能用）
# 详细：Coordination/HANDOFFS/ModelConfig-Trae-CN-2026-07-01.md
```

### 步骤 5：验证各 Agent（15 分钟）

打开 `Coordination/HEARTBEAT.md`，每个 agent 启动后应该自动更新心跳：

```bash
# Claude Desktop
# 直接问 Claude "在吗？" → 应该回

# Marvis
# 启动后看 HEARTBEAT.md Marvis 行最后心跳 < 5 分钟

# Hermes（阿里云）
ssh -i openclaw0417.pem root@39.105.115.6 "systemctl status hermes-agent"

# Codex（GUI）
# 启动 Codex → 配 API → 测试一条命令

# Trae CN（GUI）
# 启动 → 充值 → 测试一条命令
```

### 步骤 6：恢复关键文件（10 分钟）

```powershell
# 1. 从云盘恢复 SSH key
cp /d/CloudBackup/openclaw0417.pem C:/Users/Administrator/Downloads/

# 2. 从云盘恢复 APIkey.docx（参考用）
cp /d/CloudBackup/APIkey.docx "G:/CC-Switch-v3.15.0-Windows-Portable/"

# 3. 启动 Obsidian → 设置 obsidian-git 插件
#    → 自动同步 vault
```

### 步骤 7：跑通验证（10 分钟）

测试场景：
1. **Claude Desktop 能调 M3**：问"在吗" → 回
2. **抓数据能跑**：让 claude-desktop 跑 AI 爆金日记
3. **QUEUE.json 能写**：写 handoff 给 Hermes → 看它能不能扫到
4. **Gitee push 通**：vault 改一个字 → commit → push

---

## 4. 验证清单（恢复后必查）

| 项 | 验证方法 | 通过标志 |
|---|---|---|
| Claude Desktop 模型 | 问 "你是什么模型" | 回 "MiniMax-M3" |
| CC Switch 代理 | 浏览器开 http://127.0.0.1:15721 | 显示 CC Switch 界面 |
| MiniMax API 通 | 在 Claude Desktop 问问题 | 正常回 |
| DeepSeek API 通 | （不直接测） | — |
| 火山 API 通 | （不直接测） | — |
| Hermes 阿里云 | ssh 看 systemctl status | active (running) |
| Vault 同步通 | git -C /d/ObsidianVault pull | 无错误 |
| Obsidian Git 自动同步 | 改 vault 一个字 → 等 5 分钟 | Gitee 自动 commit |
| HEARTBEAT 更新 | 启动各 agent | 各自心跳时间 < 5 分钟 |
| 任务队列工作 | 入队一个任务 | agent 抢单 |

---

## 5. 故障排查（恢复后出问题）

### 问题 1：Claude Desktop 不通 M3
- **检查 CC Switch** 是否在跑（http://127.0.0.1:15721）
- **检查 settings.json** 的 API_KEY 是否对（从 vault README 复制）
- **检查网络**：ping api.minimaxi.com

### 问题 2：Hermes 阿里云连不上
- **检查 SSH key**：C:/Users/Administrator/Downloads/openclaw0417.pem 存在？
- **检查密钥权限**：icacls openclaw0417.pem（Windows 上自动）
- **检查 ECS**：阿里云控制台看 ECS 在不在运行

### 问题 3：vault push 不上去
- **检查 Gitee 凭据**：git config --global credential.helper
- **检查远端**：git remote -v
- **手动 push**：cd /d/ObsidianVault && git push origin master

### 问题 4：某个 Agent 找不到
- **检查路径**：winget list | grep AgentName
- **重装**：winget install AgentName

### 问题 5：MCP servers 全没了
- **重新配**：参考 [[Coordination/ModelConfig]] 和 handoff 文件
- **备份恢复**：从云盘恢复 `C:/Users/hao/.claude.json`

---

## 6. 时间估算

| 步骤 | 时间 |
|---|---|
| 买电脑 / 重装系统 | 30 分钟 |
| 装基础软件 | 30 分钟 |
| 拉 vault | 5 分钟 |
| 装 Claude Desktop + CC Switch + 配置 | 15 分钟 |
| 装其他 Agent | 30 分钟 |
| 恢复关键文件 | 10 分钟 |
| 验证 | 15 分钟 |
| **总计** | **约 2 小时** |

---

## 7. 关键路径速查

| 资产 | 路径 |
|---|---|
| Vault 根目录 | `D:/ObsidianVault/` |
| Claude Desktop 配置 | `C:/Users/hao/.claude/settings.json` |
| Claude 全局配置 | `C:/Users/hao/.claude.json` |
| API Key 文档 | `G:/CC-Switch-v3.15.0-Windows-Portable.bak.20260627_130921/APIkey.docx` |
| SSH key | `C:/Users/Administrator/Downloads/openclaw0417.pem` |
| Hermes 阿里云 | `39.105.115.6` (SSH) |
| 华为云 ECS | 阿里云控制台 → Hermes Agent-tkpc |
| Gitee vault | `gitee.com/haowenzhuo/obsidian-vault` |
| 任务队列 | `D:/ObsidianVault/Coordination/QUEUE.json` |
| 心跳 | `D:/ObsidianVault/Coordination/HEARTBEAT.md` |
| 协调协议 | `D:/ObsidianVault/CLAUDE.md` |
| 模型配置 | `D:/ObsidianVault/Coordination/ModelConfig-2026-07-01.md` |
| 第二大脑 | `D:/ObsidianVault/README.md` |

---

## 8. 预防措施（建议主人做）

### 8.1 每天自动备份（推荐）

让我（claude-desktop）写个 cron 脚本，每天 23:00 备份：
```python
# 备份到 D:/CloudBackup/（同步 OneDrive/坚果云）
files_to_backup = [
    "C:/Users/hao/.claude/settings.json",
    "C:/Users/hao/.claude.json",
    "G:/CC-Switch-*/APIkey.docx",
    "C:/Users/Administrator/Downloads/openclaw0417.pem",
]
```

### 8.2 每月手动备份（推荐）

主人每月 1 号手动做：
1. 备份 D 盘到移动硬盘
2. 备份 G 盘到移动硬盘
3. 检查 Gitee vault 同步正常

### 8.3 异地备份（强烈推荐）

把 vault 推两个远端：
- Gitee（国内，快）
- GitHub（国外，备份）

```bash
cd /d/ObsidianVault
git remote add github https://github.com/haowenzhuo/obsidian-vault.git
git push github master
```

---

## 9. 验证本手册

**本手册最后一次演练**：2026-07-01（纸上谈兵）

**建议主人做的事**：
1. 找一台干净机器，按本手册演练一次（验证可行性）
2. 修正本手册
3. 每季度演练一次

---

**维护人**: claude-desktop
**审核人**: 郝冠的
**下次演练**: 待定

---

📌 **重要提醒**：电脑挂是**最低概率事件**，但**每天都有小概率**：密码忘了 / 配置坏了 / 软件更新挂了。本手册 = 兜底。