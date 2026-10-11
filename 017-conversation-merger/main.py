
import argparse
import json
from pathlib import Path


def merge_conversations(paths: list[Path]) -> list[dict]:
    """複数の会話JSONを入力順に結合する。"""
    merged = []

    for path in paths:
        with path.open("r", encoding="utf-8") as f:
            messages = json.load(f)

        if not isinstance(messages, list):
            raise ValueError(f"JSON配列ではありません: {path}")

        if not all(isinstance(message, dict) for message in messages):
            raise ValueError(f"メッセージ形式が不正です: {path}")

        merged.extend(messages)
        print(f"読み込み: {path} ({len(messages)}件)")

    return merged


def main():
    parser = argparse.ArgumentParser(
        description="複数の会話JSONを1つに結合します。"
    )
    parser.add_argument(
        "inputs", nargs="+", type=Path,
        help="入力するJSONファイル"
    )
    parser.add_argument(
        "-o", "--output", type=Path, required=True,
        help="出力先JSONファイル"
    )
    args = parser.parse_args()

    # 入力ファイルを上書きしないようにする
    if args.output.resolve() in [p.resolve() for p in args.inputs]:
        parser.error("出力先に入力ファイルは指定できません。")

    try:
        merged = merge_conversations(args.inputs)

        output_text = json.dumps(
            merged, ensure_ascii=False, indent=2
        )
        args.output.write_text(
            output_text + "\n", encoding="utf-8"
        )

    except (OSError, ValueError, json.JSONDecodeError) as e:
        parser.exit(1, f"エラー: {e}\n")

    print(f"結合完了: {len(merged)}件 → {args.output}")


if __name__ == "__main__":
    main()
