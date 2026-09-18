const button = document.getElementById("randomButton");
const result = document.getElementById("result");

button.addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({
    active: true,
    currentWindow: true
  });

  const results = await chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: getRandomVideo
  });

  const url = results[0].result;

  if (url) {
    result.textContent = url;
  } else {
    result.textContent = "動画が見つかりませんでした";
  }
});

function getRandomVideo() {
  const links = [...document.querySelectorAll('a[href^="/watch?v="]')];

  const urls = [...new Set(
    links.map(link => link.href)
  )];

  if (urls.length === 0) {
    return null;
  }

  const randomIndex = Math.floor(Math.random() * urls.length);

  return urls[randomIndex];
}