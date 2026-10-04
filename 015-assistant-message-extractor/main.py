import json
import sys
from pathlib import Path


def extract_assistant_messages(messages: list[dict]) -> list[str]:
    """会話ログから role=assistant の発言だけを抽出する。"""
    assistant_messages = []

    for message in messages:
        if message.get("role") == "assistant":
            text = message.get("text", "").strip()
            if text:
                assistant_messages.append(text)

    return assistant_messages


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <conversation.json>")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"File not found: {input_path}")
        sys.exit(1)

    with input_path.open("r", encoding="utf-8") as f:
        messages = json.load(f)

    assistant_messages = extract_assistant_messages(messages)

    if not assistant_messages:
        print("Assistant messages were not found.")
        return

    for message in assistant_messages:
        print(message)
        print()


if __name__ == "__main__":
    main()