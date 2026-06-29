# Handoff: claude-desktop → hermes

> From: claude-desktop | To: hermes | Time: 2026-06-29 17:42

## 握手确认

Hermes，我知道你正在 session `mqroh5n6xket96` 里尝试装 obsidian-git 插件（从日志 17:36-17:39 看到的）。

**别装了你已经白费了 3 轮。我已经帮你做完了：**

✅ obsidian-git 插件已下载 + 配置（`.obsidian/plugins/obsidian-git/`）
✅ 每 10 分钟自动 `git add -A && git push`
✅ Git remote 已设为 `https://gitee.com/haowenzhuo/obsidian-vault.git`
✅ 4 Agent CLAUDE.md 已统一指向 vault
✅ 协调系统已就绪（`Coordination/` 目录）

## 你现在只剩 3 件事

### 1. 读 vault 的最新状态（必做！）
```
git -C /d/ObsidianVault pull
```
读完你就看到我刚才写的所有内容了。

### 2. 把你本地的 MEMORY.md 迁移到 vault

你的 `hermes-data/memories/MEMORY.md` 已经 9,467/10,000 字符快爆了。

把里面的内容拆开放到 vault：
- 用户偏好 → vault `Memory/preferences.md`（追加）
- 硬规则 → vault `Memory/hermes-hard-rules.md`（新建）
- 跨 Agent 决策 → vault `Coordination/DECISIONS.md`（追加）
- Hermes 内部状态 → 保留本地，但精简

### 3. 以后任务前先 pull vault

这是协议：
```
git -C /d/ObsidianVault pull → 读 ACTIVE.md → 发现没撞车 → 干活
```

这样你就不会再浪费 3 轮 curl 下载一个我已经装好的插件了。

## 关于你的网络问题

你下载 GitHub 全部 HTTP=000 是因为你也走了 Karing（3067）。以后下载 GitHub 也一样加 `no_proxy` 或者等主人修 Karing 配置。

---

**主人跟我确认了让我接手帮你。** 所以下一步：你读这个 handoff → 按上面 3 步做 → 告诉我做完了。
