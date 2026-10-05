import json
import sys
from pathlib import Path


VALID_ROLES = {"user", "assistant"}


def clean_messages(messages: list[dict]) -> list[dict]:
    """会話ログから不要なメッセージを取り除く。"""
    cleaned_messages = []

    for message in messages:
        role = message.get("role")
        text = message.get("text", "")

        if role not in VALID_ROLES:
            continue

        if not isinstance(text, str):
            continue

        text = text.strip()

        if not text:
            continue

        cleaned_messages.append({
            "role": role,
            "text": text,
        })

    return cleaned_messages


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

    cleaned_messages = clean_messages(messages)

    print(
        json.dumps(
            cleaned_messages,
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()