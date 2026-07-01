---
title: GitHub 国内克隆/下载路径
agent: claude-desktop
date: 2026-07-01
status: gh-proxy.com 12s 拉 2030 文件已验证
tags: [github, mirror, gh-proxy, fastgit, china]
---

# GitHub 国内拉取路径

## 验证过的方案

### 1. gh-proxy.com（首选）

```bash
git clone --depth 1 --single-branch --branch main \
  "https://gh-proxy.com/https://github.com/<owner>/<repo>.git" "<target>"
```

实测：`open-jarvis/OpenJarvis`，2030 文件 / 12s（git bash，沙盒外，本地终端）

备用前缀：`https://mirror.ghproxy.com/`

### 2. hub.fastgit.xyz（fallback）

```bash
git clone --depth 1 --single-branch --branch main \
  "https://hub.fastgit.xyz/<owner>/<repo>.git" "<target>"
```

未实测（gh-proxy 一次就过，没用到）

### 3. 走 gh API + tarball（最稳但要先 auth）

```bash
gh release download --repo <owner>/<repo> --pattern '*source*' --dir <target>
# 或
gh api repos/<owner>/<repo>/tarball -q > repo.tar.gz
```

要求 `gh auth status` 通过

### 4. 不用镜像，纯 pip wheel

只适用 Python 包：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple <pkg>`
清华源 0.3s，比 PyPI 官方 1.2s 快 4×

## 失败模式与回退

| 现象 | 原因 | 修法 |
|------|------|------|
| `git clone` 5min 卡死 | GitHub 直连被劫/丢包 | 切 gh-proxy |
| `git: error: RPC failed; curl 56 GnuTLS` | TLS 握手断 | 切 gh-proxy 或换 SSH |
| gh-proxy 也卡 | 该 mirror 临时限流 | 切 fastgit → tarball → 离线 |
| `Cloning into '...乱码...'` 红字 | console codepage 936 误把 UTF-8 路径当 GBK | **不是真错**，看结尾 `Updating files: 100%, done` 才是成功 |

## 关键经验

1. **沙盒内 GitHub 直连几乎都失败**——sandbox 出口走的是 datacenter IP，被 GitHub 风控
2. **gh-proxy 适合 git LFS 多的大仓库**——只对 `git/zip` 流量代理，**PyPI/npm/conda 不代理**
3. **gitee 镜像只对热门仓库自动同步**——小众项目（< 100 star）大概率没有
4. **沙盒 vs 本地终端要分清**——sandbox 不挂 G 盘时，`cd "G:\..."` 在 sandbox 里会失败但本地跑得通。要看 exit code 而不是只看命令"看起来在跑"
