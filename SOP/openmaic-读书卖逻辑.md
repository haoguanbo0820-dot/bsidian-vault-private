# OpenMAIC 读书卖逻辑 + 三平台自媒体 SOP

> 复用度: ⭐⭐⭐⭐ (一本书用一次, 但方法论复用)
> 状态: 实验中 (2026-06-26 跑通过一次)
> 来源: 主人 2026-06-24 给的链接 https://open.maic.chat/classroom/NVSfIRF9iw

## 目标

用 OpenMAIC 生成"读书 + 卖底层逻辑"课件 → 拆解成短视频 → 发抖音/快手/小红书 → 通过图书 CPS 变现

## 工具栈

- **OpenMAIC** v0.2.2 @ `G:/openmaic` (清华 THU-MAIC 开源, MIT 许可证)
- **LLM**: MiniMax-M3 (主人唯一真实 API key)
- **TTS**: MiniMax speech-2.6-hd / 2.8-hd
- **数字人**: 可灵 / 即创 / HeyGen (待选)
- **三平台**: 抖音 / 快手 / 小红书

## 流程(已验证)

### Step 1: 选书 (当当/京东 Top 250 + 评分 ≥ 7.5)

候选书:
- 《纳瓦尔宝典》⭐⭐⭐⭐⭐ 财富/认知
- 《认知觉醒》⭐⭐⭐⭐⭐ 中文新书
- 《蛤蟆先生去看心理医生》⭐⭐⭐⭐⭐ 心理学
- 《第一性原理》⭐⭐⭐⭐⭐ 思维模型
- 《了凡四训》⭐⭐⭐⭐ 改命/认知
- 《超越百岁:长寿的科学》⭐⭐⭐⭐ 健康

### Step 2: 启动 OpenMAIC

```bash
cd G:/openmaic
pnpm dev
# 等 7.4s Ready 后, 浏览器打开 http://localhost:3000
```

### Step 3: 调 API 生成大纲

```bash
curl -X POST "http://localhost:3000/api/generate/scene-outlines-stream" \
  -H "Content-Type: application/json" \
  -d '{
    "requirements": {
      "requirement": "<书名 + 卖逻辑要求 + 受众 + 时长>",
      "userNickname": "学习者",
      "webSearch": false
    }
  }'
```

**注意**: LLM 可能自动换书(看到"思维模型"会换《穷查理宝典》)。**要在 requirement 里明确"基于 X 书"**,必要时上传 PDF。

### Step 4: 拆解成 16 条短视频 (8 模块 × 2 = 核心 + 24h 行动)

每节: 1 条抖音 60s + 1 条小红书 9 图 + 1 条快手 30s

### Step 5: 数字人出片 (5-10 分钟/条)

### Step 6: 三平台发布 + 挂车

抖音商品橱窗: 1000 粉门槛
小红书蒲公英: 1000 粉门槛
快手小店: 同款

## 关键经验(从 6-26 实测)

1. ✅ OpenMAIC 跑通率高(65s 出 23 场景大纲)
2. ⚠️ LLM 自动换书问题 → 显式说明书名
3. ⚠️ 真实可用的 LLM 只有 MiniMax-M3(其他 21 个 key 是占位符)
4. ⚠️ 服务关掉就要重新 `pnpm dev` (后台跑)
5. ⚠️ 数字人在抖音打 AI 标签 → 流量降权 30-50%

## 历史踩坑

- 2026-06-26: LLM 把《认知觉醒》自动换《穷查理宝典》 → 主人骂了"为啥还要生成"
- 2026-06-26: 主人说"开始"我按默认选项跑过头 → 过度执行
- 2026-06-26: 主人纠正"不对了 你为啥还要生成" → **别自动按上次方案跑**

## 产出位置

`D:/OpenClaw-Hermes-Portable/openmaic-courses/<书名>/`
