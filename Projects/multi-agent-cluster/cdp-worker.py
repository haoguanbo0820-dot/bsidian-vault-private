#!/usr/bin/env python
"""
Multi-agent CDP Worker
======================
连主人 Edge 远程端口（9222），抓国内 4 平台热搜/搜索结果

用法：
    # 1. 主人开 Edge 远程端口
    "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222

    # 2. 跑 worker
    python cdp-worker.py zhihu    # 抓知乎热榜
    python cdp-worker.py weibo    # 抓微博热搜
    python cdp-worker.py xhs      # 抓小红书
    python cdp-worker.py all      # 全部跑
"""
import sys
import json
import time
from datetime import datetime
from playwright.sync_api import sync_playwright

CDP_URL = "http://127.0.0.1:9222"
OUTPUT_DIR = r"G:\个人项目\AI工具\codex\references\signals"


def fetch_zhihu(page):
    """知乎热榜"""
    print("[知乎] 打开热榜页...")
    page.goto("https://www.zhihu.com/billboard", timeout=30000, wait_until="domcontentloaded")
    page.wait_for_timeout(5000)
    # 知乎热榜 50 条
    items = page.locator(".HotList-item").all()
    if not items:
        # 备用选择器
        items = page.locator('[class*="HotList"]').all()
    results = []
    for i, item in enumerate(items[:30], 1):
        try:
            title_el = item.locator(".HotList-itemTitle")
            if title_el.count() == 0:
                title_el = item.locator('[class*="Title"]')
            title = title_el.first.inner_text().strip() if title_el.count() > 0 else ""
            link_el = item.locator("a").first
            link = link_el.get_attribute("href") if link_el.count() > 0 else ""
            heat_el = item.locator(".HotList-itemMetrics")
            heat = heat_el.first.inner_text().strip() if heat_el.count() > 0 else ""
            if title:
                results.append({"rank": i, "title": title, "url": link, "heat": heat})
        except Exception:
            pass
    return results


def fetch_weibo(page):
    """微博热搜"""
    print("[微博] 打开热搜页...")
    page.goto("https://s.weibo.com/top/summary", timeout=30000, wait_until="domcontentloaded")
    page.wait_for_timeout(5000)
    items = page.locator("td-02").all()
    results = []
    for i, item in enumerate(items[:30], 1):
        try:
            a_el = item.locator("a").first
            title = a_el.inner_text().strip() if a_el.count() > 0 else ""
            link = a_el.get_attribute("href") if a_el.count() > 0 else ""
            span_el = item.locator("span").first
            heat = span_el.inner_text().strip() if span_el.count() > 0 else ""
            if title:
                results.append({"rank": i, "title": title, "url": link, "heat": heat})
        except Exception:
            pass
    return results


def fetch_xhs(page):
    """小红书搜索"""
    print("[小红书] 搜索 'AI 副业'...")
    page.goto(
        "https://www.xiaohongshu.com/search_result?keyword=AI%E5%89%AF%E4%B8%9A&source=web_explore_feed",
        timeout=30000,
        wait_until="domcontentloaded",
    )
    page.wait_for_timeout(5000)
    # 小红书笔记卡片
    items = page.locator('[class*="note-item"]').all()
    if not items:
        items = page.locator("section").all()
    results = []
    for i, item in enumerate(items[:30], 1):
        try:
            title_el = item.locator('[class*="title"]').first
            title = title_el.inner_text().strip() if title_el.count() > 0 else ""
            author_el = item.locator('[class*="author"]').first
            author = author_el.inner_text().strip() if author_el.count() > 0 else ""
            if title:
                results.append({"rank": i, "title": title, "author": author})
        except Exception:
            pass
    return results


def fetch_douyin(page):
    """抖音搜索"""
    print("[抖音] 搜索 'AI 副业'...")
    page.goto(
        "https://www.douyin.com/search/AI%E5%89%AF%E4%B8%9A?type=general",
        timeout=30000,
        wait_until="domcontentloaded",
    )
    page.wait_for_timeout(5000)
    # 抖音视频卡片
    items = page.locator('[class*="search-result-card"]').all()
    if not items:
        items = page.locator('[class*="Card"]').all()
    results = []
    for i, item in enumerate(items[:30], 1):
        try:
            title_el = item.locator('[class*="title"]').first
            title = title_el.inner_text().strip() if title_el.count() > 0 else ""
            if title:
                results.append({"rank": i, "title": title})
        except Exception:
            pass
    return results


def main(platform="all"):
    ts = datetime.now()
    print(f"[{ts.strftime('%H:%M:%S')}] Worker 启动，目标: {platform}")
    print(f"[{ts.strftime('%H:%M:%S')}] 连 CDP: {CDP_URL}")

    results = {"ts": ts.isoformat(), "agent": "claude-desktop", "mode": "cdp-cluster", "platforms": {}}

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(CDP_URL)
            print(f"[{ts.strftime('%H:%M:%S')}] CDP 连接成功")
            # 用主人已经在用的 page（已经有登录态）
            context = browser.contexts[0] if browser.contexts else browser.new_context()
            page = context.new_page() if not context.pages else context.pages[0]
        except Exception as e:
            print(f"[ERR] CDP 连不上: {e}")
            print("提示: 主人先开 Edge 远程端口：")
            print('  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --remote-debugging-port=9222')
            return None

        tasks = {
            "zhihu": ("知乎热榜", fetch_zhihu),
            "weibo": ("微博热搜", fetch_weibo),
            "xhs": ("小红书", fetch_xhs),
            "douyin": ("抖音", fetch_douyin),
        }

        targets = list(tasks.keys()) if platform == "all" else [platform]

        for target in targets:
            name, fn = tasks[target]
            try:
                print(f"\n=== {name} ===")
                items = fn(page)
                results["platforms"][target] = {"status": "ok", "count": len(items), "items": items}
                print(f"[OK] {name} 抓到 {len(items)} 条")
            except Exception as e:
                results["platforms"][target] = {"status": "err", "error": str(e)[:200]}
                print(f"[ERR] {name}: {str(e)[:200]}")
            time.sleep(2)  # 平台之间停 2s

        browser.close()

    # 落 json
    stamp = ts.strftime("%Y-%m-%d-%H%M")
    out_path = f"{OUTPUT_DIR}/scan-{stamp}-cdp-cluster.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n[{ts.strftime('%H:%M:%S')}] 保存: {out_path}")
    total = sum(p.get("count", 0) for p in results["platforms"].values())
    print(f"[{ts.strftime('%H:%M:%S')}] 总真信号: {total} 条")
    return results


if __name__ == "__main__":
    platform = sys.argv[1] if len(sys.argv) > 1 else "all"
    main(platform)
