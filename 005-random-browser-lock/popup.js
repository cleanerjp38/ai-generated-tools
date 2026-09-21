const lockButton = document.getElementById("lockButton");
const statusText = document.getElementById("status");

lockButton.addEventListener("click", () => {
  const lockMinutes = Math.floor(Math.random() * 60) + 1;

  const now = Date.now();
  const unlockTime = now + lockMinutes * 60 * 1000;

  chrome.storage.local.set({
    unlockTime: unlockTime
  });

  statusText.textContent = "Locked";
});