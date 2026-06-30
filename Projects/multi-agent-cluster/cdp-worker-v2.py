#!/usr/bin/env python
"""
Multi-agent CDP Worker v2
=========================
连主人 Edge 远程端口（9222），抓国内 4 平台热搜/搜索结果
v2 改进：用主人现有标签页 + 强制用主人的 page context（继承登录态）

用法：
    python cdp-worker-v2.py all      # 抓 4 平台
    python cdp-worker-v2.py zhihu    # 只抓知乎
    python cdp-worker-v2.py weibo    # 只抓微博
"""
import sys
import json
import time
from datetime import datetime
from playwright.sync_api import sync_playwright

CDP_URL = "http://127.0.0.1:9222"
OUTPUT_DIR = r"G:\个人项目\AI工具\codex\references\signals"


def fetch_zhihu(context):
    """知乎热榜 - 新开 tab，context 继承主人的 Cookie"""
    page = context.new_page()
    try:
        print("[知乎] 打开热榜页...")
        page.goto("https://www.zhihu.com/billboard", timeout=30000, wait_until="domcontentloaded")
        page.wait_for_timeout(8000)  # 等 JS 渲染 + API

        # 知乎热榜 30 条 - 用 .HotList-itemTitle（实际类名）
        titles = page.locator('.HotList-itemTitle').all()
        print(f"  找到 .HotList-itemTitle: {len(titles)}")

        # 备用：找所有问题链接
        if not titles:
            print("  备用：用问题链接")
            titles = page.locator('a[href*="/question/"]').all()
            print(f"  找到问题链接: {len(titles)}")

        results = []
        for i, t in enumerate(titles[:30], 1):
            try:
                if hasattr(t, "inner_text"):
                    text = t.inner_text().strip()
                else:
                    text = t.text_content() or ""
                if text and len(text) > 4:
                    results.append({"rank": i, "title": text[:100]})
            except Exception:
                pass
        return results
    finally:
        page.close()


def fetch_weibo(context):
    """微博热搜"""
    page = context.new_page()
    try:
        print("[微博] 打开热搜页...")
        page.goto("https://s.weibo.com/top/summary", timeout=30000, wait_until="domcontentloaded")
        page.wait_for_timeout(8000)

        # 微博热搜：td-02 是标题
        items = page.locator("td-02").all()
        print(f"  找到 td-02: {len(items)}")

        if not items:
            # 备用：a 标签找热搜词
            items = page.locator('a[href*="Refer=top"]').all()
            print(f"  备用: a[Refer=top] {len(items)}")
        if not items:
            items = page.locator('#pl_top_realtimehot table tbody tr').all()
            print(f"  备用2: #pl_top_realtimehot tr {len(items)}")

        results = []
        for i, item in enumerate(items[:30], 1):
            try:
                if hasattr(item, "inner_text"):
                    text = item.inner_text().strip()
                else:
                    text = item.text_content() or ""
                # 清理
                text = text.split("\n")[0].strip()
                if text and len(text) > 2:
                    results.append({"rank": i, "title": text[:100]})
            except Exception:
                pass
        return results
    finally:
        page.close()


def fetch_xhs(context):
    """小红书搜索"""
    page = context.new_page()
    try:
        print("[小红书] 搜索 'AI 副业'...")
        page.goto(
            "https://www.xiaohongshu.com/search_result?keyword=AI%E5%89%AF%E4%B8%9A&source=web_explore_feed",
            timeout=30000,
            wait_until="domcontentloaded",
        )
        page.wait_for_timeout(8000)
        items = page.locator('section.note-item').all()
        print(f"  找到 section.note-item: {len(items)}")
        if not items:
            items = page.locator('[class*="note-item"]').all()
            print(f"  备用: {len(items)}")
        results = []
        for i, item in enumerate(items[:30], 1):
            try:
                title_el = item.locator('[class*="title"]').first
                title = title_el.inner_text().strip() if title_el.count() > 0 else ""
                if not title:
                    title = item.inner_text().strip().split("\n")[0]
                if title and len(title) > 2:
                    results.append({"rank": i, "title": title[:100]})
            except Exception:
                pass
        return results
    finally:
        page.close()


def fetch_douyin(context):
    """抖音搜索"""
    page = context.new_page()
    try:
        print("[抖音] 搜索 'AI 副业'...")
        page.goto(
            "https://www.douyin.com/search/AI%E5%89%AF%E4%B8%9A?type=general",
            timeout=30000,
            wait_until="domcontentloaded",
        )
        page.wait_for_timeout(8000)
        items = page.locator('[class*="search-result-card"]').all()
        print(f"  找到 search-result-card: {len(items)}")
        if not items:
            items = page.locator('[class*="Card"]').all()
            print(f"  备用: {len(items)}")
        results = []
        for i, item in enumerate(items[:30], 1):
            try:
                title_el = item.locator('[class*="title"]').first
                title = title_el.inner_text().strip() if title_el.count() > 0 else ""
                if not title:
                    title = item.inner_text().strip().split("\n")[0]
                if title and len(title) > 2:
                    results.append({"rank": i, "title": title[:100]})
            except Exception:
                pass
        return results
    finally:
        page.close()


def main(platform="all"):
    ts = datetime.now()
    print(f"[{ts.strftime('%H:%M:%S')}] Worker v2 启动，目标: {platform}")
    print(f"[{ts.strftime('%H:%M:%S')}] 连 CDP: {CDP_URL}")

    results = {"ts": ts.isoformat(), "agent": "claude-desktop", "mode": "cdp-cluster-v2", "platforms": {}}

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(CDP_URL)
            print(f"[{ts.strftime('%H:%M:%S')}] CDP 连接成功")
            # 用主人第一个 context（继承所有 Cookie）
            context = browser.contexts[0] if browser.contexts else browser.new_context()
            print(f"[{ts.strftime('%H:%M:%S')}] 用主人 context（{len(context.cookies())} 个 Cookie）")
        except Exception as e:
            print(f"[ERR] CDP 连不上: {e}")
            return None

        tasks = {
            "zhihu": ("知乎热榜", fetch_zhihu),
            "weyin": ("微博热搜", fetch_weibo),
            "xhs": ("小红书", fetch_xhs),
            "douyin": ("抖音", fetch_douyin),
        }

        targets = list(tasks.keys()) if platform == "all" else [platform]

        for target in targets:
            name, fn = tasks[target]
            try:
                print(f"\n=== {name} ===")
                items = fn(context)
                results["platforms"][target] = {"status": "ok", "count": len(items), "items": items}
                print(f"[OK] {name} 抓到 {len(items)} 条")
                if items:
                    for it in items[:3]:
                        print(f"     - {it.get('title', '')[:60]}")
            except Exception as e:
                results["platforms"][target] = {"status": "err", "error": str(e)[:200]}
                print(f"[ERR] {name}: {str(e)[:200]}")
            time.sleep(2)

    stamp = ts.strftime("%Y-%m-%d-%H%M")
    out_path = f"{OUTPUT_DIR}/scan-{stamp}-cdp-cluster-v2.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n[{ts.strftime('%H:%M:%S')}] 保存: {out_path}")
    total = sum(p.get("count", 0) for p in results["platforms"].values())
    print(f"[{ts.strftime('%H:%M:%S')}] 总真信号: {total} 条")
    return results


if __name__ == "__main__":
    platform = sys.argv[1] if len(sys.argv) > 1 else "all"
    main(platform)
