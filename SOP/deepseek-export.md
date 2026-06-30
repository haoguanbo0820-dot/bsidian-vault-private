# DeepSeek 对话导出 SOP

> 从 QQ 浏览器导出 DeepSeek 聊天记录到 vault

## 数据结构

DeepSeek 存储位置（QQ 浏览器 IndexedDB）：
- DB: `deepseek-chat`
- Store: `history-message`
- 消息内容在 `data.chat_messages[].fragments[].content`
- 会话信息在 `data.chat_session`

## 方法 A：浏览器 Console（需手动操作）

1. 打开 QQ 浏览器，访问 `https://chat.deepseek.com/`
2. 按 `F12` 打开开发者工具，切换到 **Console（控制台）** 标签
3. 粘贴以下代码，按回车执行：

```javascript
(() => {
  const dbReq = indexedDB.open("deepseek-chat");
  dbReq.onsuccess = () => {
    const db = dbReq.result;
    const tx = db.transaction(["history-message"], "readonly");
    const req = tx.objectStore("history-message").getAll();
    req.onsuccess = () => {
      const records = req.result;
      const output = records.map(r => {
        const d = r.data || r;
        const s = d.chat_session;
        const msgs = (d.chat_messages || []).sort((a,b) => a.message_id - b.message_id)
          .map(m => ({
            role: m.role,
            content: (m.fragments || []).map(f => f.content || "").join(""),
            status: m.status
          }));
        return {title: s.title, model: s.model_type, updated: new Date(s.updated_at * 1000).toISOString(), messages: msgs};
      });
      const json = JSON.stringify(output);
      console.log('RESULT:' + json);
      console.log('Total: ' + records.length + ' conversations, ' + json.length + ' chars');
    };
  };
})();
```

注意：QQ 浏览器不支持 `copy()`，需要手动从控制台复制输出。

## 方法 B：CDP 远程控制（推荐，全自动）

当无法手动操作时，通过 Chrome DevTools Protocol 远程控制：

```bash
# 1. 关闭 QQ 浏览器
powershell -Command "Get-Process -Name QQBrowser | Stop-Process -Force"

# 2. 以远程调试模式启动
"/d/LenovoSoftstore/Install/QQliulanqi/QQBrowser.exe" --remote-debugging-port=9222 &

# 3. 确认调试端口可用
curl http://127.0.0.1:9222/json

# 4. 用 chrome-remote-interface (npm) 连接并执行提取脚本
node -e "
const CDP = require('chrome-remote-interface');
(async () => {
  const client = await CDP({port: 9222});
  const {Page, Runtime} = client;
  await Page.enable();
  await Page.navigate({url: 'https://chat.deepseek.com/'});
  await new Promise(r => setTimeout(r, 5000)); // 等待页面加载
  const result = await Runtime.evaluate({
    expression: '(async()=>{/* 提取脚本 */})()',
    awaitPromise: true
  });
  require('fs').writeFileSync('output.json', result.result.value);
  await client.close();
})();
"

# 5. 关闭 QQ 浏览器调试实例
powershell -Command "Get-Process -Name QQBrowser | Stop-Process -Force"
```

## 导入 Vault

导出后将 JSON 交给 claude-desktop，由它整理到 `Imports/DeepSeek/` 目录：
- 每个对话一个 `.md` 文件
- `INDEX.md` 包含分类索引

已导入：2026-06-30，20 个对话，308KB → [[Imports/DeepSeek/INDEX|DeepSeek 对话导入]]
