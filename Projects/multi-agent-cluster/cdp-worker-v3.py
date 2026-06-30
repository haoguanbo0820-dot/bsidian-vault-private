#!/usr/bin/env python
"""
Multi-agent CDP Worker v3
=========================
连主人 Edge 远程端口（9222），用主人现有标签页抓数据
v3 改进：用主人已经登录的 page，不新开 tab
"""
import sys
import json
import time
from datetime import datetime
from playwright.sync_api import sync_playwright

CDP_URL = "http://127.0.0.1:9222"
OUTPUT_DIR = r"G:\个人项目\AI工具\codex\references\signals"


def fetch_zhihu_new_tab(context):
    """知乎热榜 - 新开 tab"""
    page = context.new_page()
    try:
        print("[知乎] 打开热榜页...")
        page.goto("https://www.zhihu.com/billboard", timeout=30000, wait_until="domcontentloaded")
        page.wait_for_timeout(8000)
        titles = page.locator('.HotList-itemTitle').all()
        print(f"  找到 .HotList-itemTitle: {len(titles)}")
        results = []
        for i, t in enumerate(titles[:30], 1):
            try:
                text = t.inner_text().strip()
                if text and len(text) > 4:
                    results.append({"rank": i, "title": text[:100]})
            except Exception:
                pass
        return results
    finally:
        page.close()


def fetch_weibo_new_tab(context):
    """微博热搜 - 新开 tab"""
    page = context.new_page()
    try:
        print("[微博] 打开热搜页...")
        page.goto("https://s.weibo.com/top/summary", timeout=30000, wait_until="domcontentloaded")
        page.wait_for_timeout(8000)
        # 微博热搜：table tbody tr，tr 包含 td-01（排名）、td-02（标题）、td-03（热度）
        rows = page.locator('#pl_top_realtimehot table tbody tr').all()
        print(f"  找到 #pl_top_realtimehot tr: {len(rows)}")
        if not rows:
            rows = page.locator('table tbody tr').all()
            print(f"  备用: table tr {len(rows)}")
        results = []
        for i, row in enumerate(rows[:30], 1):
            try:
                tds = row.locator('td').all()
                if len(tds) >= 2:
                    title = tds[1].inner_text().strip()
                    if title and len(title) > 1:
                        results.append({"rank": i, "title": title[:100]})
            except Exception:
                pass
        return results
    finally:
        page.close()


def fetch_xhs_existing(context):
    """小红书 - 用主人已开的搜索页"""
    xhs_page = None
    for pg in context.pages:
        if 'xiaohongshu.com' in pg.url and 'search_result' in pg.url:
            xhs_page = pg
            break
    if not xhs_page:
        # 没开，新开一个
        print("  主人没开小红书搜索页，新开...")
        xhs_page = context.new_page()
        xhs_page.goto(
            "https://www.xiaohongshu.com/search_result?keyword=AI%E5%89%AF%E4%B8%9A&source=web_explore_feed",
            timeout=30000,
            wait_until="domcontentloaded",
        )
    try:
        print(f"[小红书] 用 page: {xhs_page.url[:80]}")
        xhs_page.wait_for_timeout(5000)
        notes = xhs_page.locator('section.note-item').all()
        print(f"  找到 section.note-item: {len(notes)}")
        results = []
        for i, n in enumerate(notes[:30], 1):
            try:
                # 笔记卡片文本
                text = n.inner_text().strip()
                # 找 title span
                title_span = n.locator('[class*="title"]').first
                title = title_span.inner_text().strip() if title_span.count() > 0 else text.split('\n')[0]
                author_span = n.locator('[class*="author"]').first
                author = author_span.inner_text().strip() if author_span.count() > 0 else ""
                if title and len(title) > 2:
                    results.append({"rank": i, "title": title[:100], "author": author[:50]})
            except Exception:
                pass
        return results
    except Exception as e:
        print(f"  ERR: {e}")
        return []


def fetch_douyin_existing(context):
    """抖音 - 用主人已开的搜索页"""
    dy_page = None
    for pg in context.pages:
        if 'douyin.com' in pg.url and 'search' in pg.url:
            dy_page = pg
            break
    if not dy_page:
        print("  主人没开抖音搜索页，新开...")
        dy_page = context.new_page()
        dy_page.goto(
            "https://www.douyin.com/search/AI%E5%89%AF%E4%B8%9A?type=general",
            timeout=30000,
            wait_until="domcontentloaded",
        )
    try:
        print(f"[抖音] 用 page: {dy_page.url[:80]}")
        dy_page.wait_for_timeout(8000)
        # 抖音搜索结果容器
        items = dy_page.locator('[data-e2e="search-card"]').all()
        print(f"  找到 [data-e2e=search-card]: {len(items)}")
        if not items:
            items = dy_page.locator('[class*="search-result"]').all()
            print(f"  备用: [search-result] {len(items)}")
        if not items:
            items = dy_page.locator('li').all()
            print(f"  备用2: li {len(items)}")
        results = []
        for i, item in enumerate(items[:30], 1):
            try:
                text = item.inner_text().strip()
                # 找标题（通常前 1-2 行）
                lines = [l.strip() for l in text.split('\n') if l.strip()]
                # 跳过时长（00:00）和"相关搜索"
                for line in lines:
                    if line and not line.replace(':', '').isdigit() and '相关搜索' not in line and len(line) > 4:
                        results.append({"rank": i, "title": line[:100]})
                        break
            except Exception:
                pass
        return results
    except Exception as e:
        print(f"  ERR: {e}")
        return []


def main(platform="all"):
    ts = datetime.now()
    print(f"[{ts.strftime('%H:%M:%S')}] Worker v3 启动，目标: {platform}")
    print(f"[{ts.strftime('%H:%M:%S')}] 连 CDP: {CDP_URL}")

    results = {"ts": ts.isoformat(), "agent": "claude-desktop", "mode": "cdp-cluster-v3", "platforms": {}}

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(CDP_URL)
            context = browser.contexts[0] if browser.contexts else browser.new_context()
            print(f"[{ts.strftime('%H:%M:%S')}] 用主人 context（{len(context.cookies())} 个 Cookie，{len(context.pages)} 个标签）")
        except Exception as e:
            print(f"[ERR] CDP 连不上: {e}")
            return None

        tasks = {
            "zhihu": ("知乎热榜", fetch_zhihu_new_tab),
            "weibo": ("微博热搜", fetch_weibo_new_tab),
            "xhs": ("小红书", fetch_xhs_existing),
            "douyin": ("抖音", fetch_douyin_existing),
        }

        targets = list(tasks.keys()) if platform == "all" else [platform]

        for target in targets:
            name, fn = tasks[target]
            try:
                print(f"\n=== {name} ===")
                items = fn(context)
                results["platforms"][target] = {"status": "ok", "count": len(items), "items": items}
                print(f"[OK] {name} 抓到 {len(items)} 条")
                for it in items[:3]:
                    print(f"     - {it.get('title', '')[:60]}")
            except Exception as e:
                results["platforms"][target] = {"status": "err", "error": str(e)[:200]}
                print(f"[ERR] {name}: {str(e)[:200]}")
            time.sleep(2)

    stamp = ts.strftime("%Y-%m-%d-%H%M")
    out_path = f"{OUTPUT_DIR}/scan-{stamp}-cdp-cluster-v3.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n[{ts.strftime('%H:%M:%S')}] 保存: {out_path}")
    total = sum(p.get("count", 0) for p in results["platforms"].values())
    print(f"[{ts.strftime('%H:%M:%S')}] 总真信号: {total} 条")
    return results


if __name__ == "__main__":
    platform = sys.argv[1] if len(sys.argv) > 1 else "all"
    main(platform)
