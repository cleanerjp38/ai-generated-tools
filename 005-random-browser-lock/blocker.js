chrome.storage.local.get(["unlockTime"], (result) => {
  const unlockTime = result.unlockTime;

  if (!unlockTime) {
    return;
  }

  const now = Date.now();

  if (now < unlockTime) {
    document.documentElement.innerHTML = `
      <head>
        <title>Locked</title>
      </head>
      <body>
        <h1>Random Browser Lock</h1>
        <p>YouTube is currently locked.</p>
      </body>
    `;
  }
});