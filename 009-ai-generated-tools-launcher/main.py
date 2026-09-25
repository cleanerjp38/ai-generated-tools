import json
import subprocess
import webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, simpledialog


BASE_DIR = Path(__file__).resolve().parent
TOOLS_FILE = BASE_DIR / "tools.json"


def load_tools():
    with open(TOOLS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def launch_tool(tool):
    tool_type = tool["type"]
    path = (BASE_DIR / tool["path"]).resolve()

    if not path.exists():
        messagebox.showerror(
            "Error",
            f"ファイルが見つかりません。\n{path}"
        )
        return

    try:
        if tool_type == "python":
            command = [
                "cmd",
                "/k",
                "python",
                str(path)
            ]

            if "argument" in tool:
                argument = simpledialog.askstring(
                    tool["name"],
                    f'{tool["argument"]} を入力してください'
                )

                if not argument:
                    return

                command.append(argument)

            subprocess.Popen(
                command,
                cwd=path.parent,
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )

        elif tool_type == "html":
            webbrowser.open(path.as_uri())

        elif tool_type == "extension":
            if "url" in tool:
                webbrowser.open(tool["url"])
            else:
                messagebox.showinfo(
                    tool["name"],
                    f"これはブラウザ拡張です。\n\nフォルダ:\n{path}"
                )

        else:
            messagebox.showerror(
                "Error",
                f"未対応の種類です: {tool_type}"
            )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def main():
    tools = load_tools()

    root = tk.Tk()
    root.title("AI Generated Tools Launcher")
    root.geometry("420x520")

    title = tk.Label(
        root,
        text="AI Generated Tools",
        font=("Arial", 20, "bold")
    )
    title.pack(pady=20)

    for tool in tools:
        button = tk.Button(
            root,
            text=f'{tool["id"]}  {tool["name"]}',
            width=35,
            height=2,
            command=lambda t=tool: launch_tool(t)
        )
        button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()