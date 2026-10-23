import subprocess
import sys
import json
import tkinter as tk
import webbrowser
from pathlib import Path
from tkinter import messagebox


# フォルダの位置
APP_DIR = Path(__file__).resolve().parent
BASE_DIR = APP_DIR.parent
CONFIG_PATH = APP_DIR / "tools.json"


def load_tools():
    """tools.jsonからツール一覧を読み込む"""
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data["tools"]


def launch_tool(tool):
    """登録されたツールを起動する"""
    tool_type = tool["type"]
    tool_path = (BASE_DIR / tool["path"]).resolve()

    if not tool_path.is_file():
        messagebox.showerror(
            "起動エラー",
            f"ファイルが見つかりません:\n{tool_path}"
        )
        return

    try:
        if tool_type == "web":
            opened = webbrowser.open(tool_path.as_uri())
            if not opened:
                raise RuntimeError("ブラウザを起動できませんでした。")

        elif tool_type == "python-gui":
            python_exe = Path(sys.executable)

            # WindowsではGUI用Pythonを優先する
            if sys.platform == "win32" and python_exe.name.lower() == "python.exe":
                pythonw_exe = python_exe.with_name("pythonw.exe")
                if pythonw_exe.is_file():
                    python_exe = pythonw_exe

            subprocess.Popen(
                [str(python_exe), str(tool_path)],
                cwd=str(tool_path.parent)
            )

        else:
            raise ValueError(f"未対応のツール形式です: {tool_type}")

    except (OSError, RuntimeError, ValueError) as error:
        messagebox.showerror(
            "起動エラー",
            str(error)
        )

def main():
    try:
        tools = load_tools()
    except (OSError, ValueError, KeyError, TypeError) as error:
        messagebox.showerror(
            "設定エラー",
            f"tools.jsonを読み込めません:\n{error}"
        )
        return

    root = tk.Tk()
    root.title("AI Generated Tools Launcher v2")
    root.geometry("480x380")

    title = tk.Label(
        root,
        text="AI Generated Tools",
        font=("Segoe UI", 18, "bold")
    )
    title.pack(pady=25)

    subtitle = tk.Label(
        root,
        text="使いたいツールを選択",
        font=("Segoe UI", 10)
    )
    subtitle.pack(pady=5)

    for index, tool in enumerate(tools, start=1):
        button = tk.Button(
            root,
            text=f"{index}. {tool['name']}",
            font=("Segoe UI", 11),
            width=32,
            height=2,
            command=lambda selected=tool: launch_tool(selected)
        )
        button.pack(pady=6)

        # 数字キーでも起動
        if index <= 9:
            root.bind(
                str(index),
                lambda event, selected=tool: launch_tool(selected)
            )

    hint = tk.Label(
        root,
        text="クリック、または数字キーで起動",
        font=("Segoe UI", 9),
        fg="gray"
    )
    hint.pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    main()