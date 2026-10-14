const button = document.getElementById("export");
const status = document.getElementById("status");

button.addEventListener("click", async () => {
  button.disabled = true;
  status.textContent = "会話を読み取り中...";

  try {
    // 現在開いているタブを取得
    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true
    });

    if (!tab?.id || !tab.url) {
      throw new Error("対象のタブが見つかりません。");
    }

    // ChatGPTのページか確認
    const url = new URL(tab.url);

    if (!["chatgpt.com", "chat.openai.com"].includes(url.hostname)) {
      throw new Error("ChatGPTの会話ページを開いてください。");
    }

    // ChatGPTの画面から会話を取得
    const results = await chrome.scripting.executeScript({
      target: { tabId: tab.id },

      func: () => {
        // 表示中のmain要素だけを対象にする
        const main = [...document.querySelectorAll("main")]
          .find(m =>
            m.getClientRects().length > 0 &&
            m.getBoundingClientRect().width > 0 &&
            m.querySelector("[data-turn-key]")
          );

        if (!main) return [];

        const turns = main.querySelectorAll("[data-turn-key]");
        const messages = [];

        for (const turn of turns) {
          const text = turn.innerText.trim();

          const userLabel = "あなたの発言:";
          const assistantLabel = "ChatGPT の発言:";

          if (!text.startsWith(userLabel)) continue;

          const separator = text.indexOf(
            assistantLabel,
            userLabel.length
          );

          if (separator === -1) continue;

          // ユーザーの発言
          const userText = text
            .slice(userLabel.length, separator)
            .trim();

          // GPTの発言
          const assistantText = text
            .slice(separator + assistantLabel.length)
            .replace(/\n\s*PDF に変換\s*$/, "")
            .trim();

          if (userText) {
            messages.push({
              role: "user",
              text: userText
            });
          }

          if (assistantText) {
            messages.push({
              role: "assistant",
              text: assistantText
            });
          }
        }

        return messages;
      }
    });

    const messages = results[0]?.result ?? [];

    if (messages.length === 0) {
      throw new Error(
        "発言が見つかりません。ChatGPTの会話ページを確認してください。"
      );
    }

    // JSONに変換
    const json = JSON.stringify(messages, null, 2);

    // ダウンロード用データを作成
    const blob = new Blob([json], {
      type: "application/json;charset=utf-8"
    });

    const downloadUrl = URL.createObjectURL(blob);

    const filename =
      "chatgpt-conversation-" +
      new Date().toISOString().replace(/[:.]/g, "-") +
      ".json";

    // JSONファイルを保存
    const link = document.createElement("a");
    link.href = downloadUrl;
    link.download = filename;

    document.body.appendChild(link);
    link.click();
    link.remove();

    setTimeout(() => {
      URL.revokeObjectURL(downloadUrl);
    }, 1000);

    // 件数を集計
    const users = messages.filter(
      m => m.role === "user"
    ).length;

    const assistants = messages.filter(
      m => m.role === "assistant"
    ).length;

    status.textContent =
      "保存処理を開始しました！\n" +
      `ユーザー: ${users}件\n` +
      `GPT: ${assistants}件\n` +
      `合計: ${messages.length}件`;

  } catch (error) {
    status.textContent = `エラー: ${error.message}`;

  } finally {
    button.disabled = false;
  }
});