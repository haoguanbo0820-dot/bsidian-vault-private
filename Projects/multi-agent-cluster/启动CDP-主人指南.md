# 启动主人 Edge 远程端口（CDP）— 一行命令

## TL;DR

主人开 1 个命令，我就开始抓数据。

## 命令（复制粘贴到 PowerShell）

```powershell
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\hao\AppData\Local\Edge-CDP"
```

## 详细步骤

### 1. 准备工作

- 主人**已经登录**了 知乎 / 微博 / 小红书 / 抖音（用平时用的那个 Edge profile）
- 不要关 Edge 窗口（保持开就行）

### 2. 开新 Edge 窗口带远程端口

**不要**关主人正在用的 Edge！要新开一个：

- 桌面右键 → 新建快捷方式
- 目标填：`"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\hao\AppData\Local\Edge-CDP"`
- 名字叫 `Edge-CDP-Worker`
- 双击打开

或者直接 PowerShell：
```powershell
Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -ArgumentList "--remote-debugging-port=9222", "--user-data-dir=C:\Users\hao\AppData\Local\Edge-CDP"
```

### 3. 登录 4 平台

在新开的 Edge 里登录：
- 知乎 (zhihu.com)
- 微博 (weibo.com)
- 小红书 (xiaohongshu.com)
- 抖音 (douyin.com)

### 4. 让我跑 worker

主人回话："开了"或"CDP 好了"。

我跑：
```bash
python D:/ObsidianVault/Projects/multi-agent-cluster/cdp-worker.py all
```

## 不开新窗口会怎样？

主人用现有的 Edge？需要重启 Edge 加远程端口，会**中断主人现在用的窗口**（关掉所有标签页）。

**推荐开新窗口**（用 `--user-data-dir` 指定新 profile，不影响主人的）。

## 端口被占用

```bash
netstat -ano | findstr :9222
# 看谁在用
taskkill /F /PID <PID>
```

## 验证 CDP 通

主人开新 Edge 后，在主人**自己**的浏览器（任意浏览器）打开：

```
http://127.0.0.1:9222/json/version
```

看到一串 JSON = 通了。看到 `Connection refused` = 没开。

## 关掉 CDP 模式

直接关新开的 Edge 窗口就行。主人原来用的 Edge 不受影响。

## 安全提醒

- `--remote-debugging-port=9222` 等于开了一个**本地 HTTP 服务**
- **不要**绑到 0.0.0.0 或外网 IP（默认只绑 127.0.0.1，安全）
- 别人访问 `127.0.0.1:9222` = 完全控制这个 Edge（包括所有登录态）
- 跑完建议关掉 Edge 窗口
