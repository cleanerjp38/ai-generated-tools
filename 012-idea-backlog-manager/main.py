import json
import random
import re
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox


BASE_DIR = Path(__file__).resolve().parent
IDEAS_FILE = BASE_DIR / "ideas.md"
PROGRESS_FILE = BASE_DIR / "progress.json"

STATUSES = [
    "未着手",
    "次に作る",
    "作業中",
    "完成",
    "保留",
]


def parse_ideas(markdown_text):
    ideas = []

    current_category = ""
    current_idea = None

    lines = markdown_text.splitlines()

    for line in lines:
        stripped = line.strip()

        # 大カテゴリ
        category_match = re.match(r"^# (\d+)\.\s+(.+)$", stripped)

        if category_match:
            current_category = category_match.group(2).strip()
            continue

        # ツール候補
        idea_match = re.match(
            r"^## (\d+-[A-Z])\.\s+(.+)$",
            stripped
        )

        if idea_match:
            if current_idea:
                ideas.append(current_idea)

            current_idea = {
                "id": idea_match.group(1),
                "name": idea_match.group(2).strip(),
                "category": current_category,
                "description": "",
                "completion": "",
                "difficulty": "",
                "technology": "",
                "new_technology": "",
            }

            continue

        if not current_idea:
            continue

        if stripped.startswith("- 完成条件："):
            current_idea["completion"] = stripped.replace(
                "- 完成条件：", "", 1
            ).strip()

        elif stripped.startswith("- 難易度："):
            current_idea["difficulty"] = stripped.replace(
                "- 難易度：", "", 1
            ).strip()

        elif stripped.startswith("- 技術："):
            current_idea["technology"] = stripped.replace(
                "- 技術：", "", 1
            ).strip()

        elif stripped.startswith("- 新技術："):
            current_idea["new_technology"] = stripped.replace(
                "- 新技術：", "", 1
            ).strip()

        elif (
            stripped
            and not stripped.startswith("-")
            and not stripped.startswith("#")
            and not stripped.startswith("---")
        ):
            if current_idea["description"]:
                current_idea["description"] += " "

            current_idea["description"] += stripped

    if current_idea:
        ideas.append(current_idea)

    return ideas


def load_progress():
    if not PROGRESS_FILE.exists():
        return {}

    try:
        with PROGRESS_FILE.open(
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)

    except (json.JSONDecodeError, OSError):
        return {}


def save_progress(progress):
    with PROGRESS_FILE.open(
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            progress,
            f,
            ensure_ascii=False,
            indent=2
        )


class IdeaBacklogManager:
    def __init__(self, root):
        self.root = root

        self.root.title(
            "AI Generated Tools Idea Manager"
        )

        self.root.geometry("1150x720")
        self.root.minsize(900, 600)

        if not IDEAS_FILE.exists():
            messagebox.showerror(
                "エラー",
                "ideas.md が見つかりません。"
            )
            root.destroy()
            return

        markdown_text = IDEAS_FILE.read_text(
            encoding="utf-8"
        )

        self.ideas = parse_ideas(markdown_text)
        self.progress = load_progress()

        self.filtered_ideas = []
        self.selected_idea = None

        self.create_widgets()
        self.populate_filters()
        self.refresh_list()

    def create_widgets(self):
        # -------------------------
        # 上部統計
        # -------------------------

        stats_frame = ttk.Frame(
            self.root,
            padding=10
        )

        stats_frame.pack(
            fill="x"
        )

        title_label = ttk.Label(
            stats_frame,
            text="AI Generated Tools Idea Manager",
            font=(
                "",
                18,
                "bold"
            )
        )

        title_label.pack(
            side="left"
        )

        self.stats_label = ttk.Label(
            stats_frame,
            text=""
        )

        self.stats_label.pack(
            side="right"
        )

        # -------------------------
        # フィルター
        # -------------------------

        filter_frame = ttk.Frame(
            self.root,
            padding=10
        )

        filter_frame.pack(
            fill="x"
        )

        ttk.Label(
            filter_frame,
            text="検索"
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        self.search_var = tk.StringVar()

        search_entry = ttk.Entry(
            filter_frame,
            textvariable=self.search_var,
            width=25
        )

        search_entry.grid(
            row=0,
            column=1,
            padx=5
        )

        self.search_var.trace_add(
            "write",
            lambda *args: self.refresh_list()
        )

        ttk.Label(
            filter_frame,
            text="カテゴリ"
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        self.category_var = tk.StringVar(
            value="すべて"
        )

        self.category_combo = ttk.Combobox(
            filter_frame,
            textvariable=self.category_var,
            state="readonly",
            width=24
        )

        self.category_combo.grid(
            row=0,
            column=3,
            padx=5
        )

        self.category_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.refresh_list()
        )

        ttk.Label(
            filter_frame,
            text="難易度"
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        self.difficulty_var = tk.StringVar(
            value="すべて"
        )

        self.difficulty_combo = ttk.Combobox(
            filter_frame,
            textvariable=self.difficulty_var,
            state="readonly",
            width=10
        )

        self.difficulty_combo.grid(
            row=0,
            column=5,
            padx=5
        )

        self.difficulty_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.refresh_list()
        )

        ttk.Label(
            filter_frame,
            text="状態"
        ).grid(
            row=0,
            column=6,
            padx=5
        )

        self.status_filter_var = tk.StringVar(
            value="すべて"
        )

        self.status_filter_combo = ttk.Combobox(
            filter_frame,
            textvariable=self.status_filter_var,
            state="readonly",
            width=12
        )

        self.status_filter_combo["values"] = [
            "すべて"
        ] + STATUSES

        self.status_filter_combo.grid(
            row=0,
            column=7,
            padx=5
        )

        self.status_filter_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.refresh_list()
        )

        random_button = ttk.Button(
            filter_frame,
            text="🎲 ランダム選択",
            command=self.select_random_idea
        )

        random_button.grid(
            row=0,
            column=8,
            padx=10
        )
        # -------------------------
        # メインエリア
        # -------------------------

        main_frame = ttk.Panedwindow(
            self.root,
            orient=tk.HORIZONTAL
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # -------------------------
        # 左：一覧
        # -------------------------

        list_frame = ttk.Frame(
            main_frame
        )

        main_frame.add(
            list_frame,
            weight=3
        )

        columns = (
            "id",
            "name",
            "difficulty",
            "status"
        )

        self.tree = ttk.Treeview(
            list_frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading(
            "id",
            text="ID"
        )

        self.tree.heading(
            "name",
            text="ツール名"
        )

        self.tree.heading(
            "difficulty",
            text="難易度"
        )

        self.tree.heading(
            "status",
            text="状態"
        )

        self.tree.column(
            "id",
            width=70,
            anchor="center"
        )

        self.tree.column(
            "name",
            width=330
        )

        self.tree.column(
            "difficulty",
            width=80,
            anchor="center"
        )

        self.tree.column(
            "status",
            width=100,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            list_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_select
        )

        # -------------------------
        # 右：詳細
        # -------------------------

        detail_frame = ttk.Frame(
            main_frame,
            padding=15
        )

        main_frame.add(
            detail_frame,
            weight=2
        )

        self.detail_title = ttk.Label(
            detail_frame,
            text="候補を選択してください",
            font=(
                "",
                16,
                "bold"
            ),
            wraplength=380
        )

        self.detail_title.pack(
            anchor="w",
            pady=(
                0,
                15
            )
        )

        self.detail_text = tk.Text(
            detail_frame,
            wrap="word",
            height=20,
            state="disabled"
        )

        self.detail_text.pack(
            fill="both",
            expand=True
        )

        status_frame = ttk.Frame(
            detail_frame
        )

        status_frame.pack(
            fill="x",
            pady=10
        )

        ttk.Label(
            status_frame,
            text="状態:"
        ).pack(
            side="left"
        )

        self.status_var = tk.StringVar(
            value="未着手"
        )

        self.status_combo = ttk.Combobox(
            status_frame,
            textvariable=self.status_var,
            values=STATUSES,
            state="readonly",
            width=12
        )

        self.status_combo.pack(
            side="left",
            padx=10
        )

        self.status_combo.bind(
            "<<ComboboxSelected>>",
            self.change_status
        )

    def populate_filters(self):
        categories = sorted(
            {
                idea["category"]
                for idea in self.ideas
                if idea["category"]
            }
        )

        self.category_combo["values"] = [
            "すべて"
        ] + categories

        difficulties = sorted(
            {
                idea["difficulty"]
                for idea in self.ideas
                if idea["difficulty"]
            }
        )

        self.difficulty_combo["values"] = [
            "すべて"
        ] + difficulties

    def get_status(self, idea_id):
        return self.progress.get(
            idea_id,
            "未着手"
        )

    def refresh_list(self):
        search = self.search_var.get().lower()
        category = self.category_var.get()
        difficulty = self.difficulty_var.get()
        status_filter = self.status_filter_var.get()

        self.filtered_ideas = []

        for idea in self.ideas:
            status = self.get_status(
                idea["id"]
            )

            searchable_text = " ".join(
                [
                    idea["id"],
                    idea["name"],
                    idea["category"],
                    idea["description"],
                    idea["completion"],
                    idea["technology"],
                    idea["new_technology"],
                ]
            ).lower()

            if (
                search
                and search not in searchable_text
            ):
                continue

            if (
                category != "すべて"
                and idea["category"] != category
            ):
                continue

            if (
                difficulty != "すべて"
                and idea["difficulty"] != difficulty
            ):
                continue

            if (
                status_filter != "すべて"
                and status != status_filter
            ):
                continue

            self.filtered_ideas.append(
                idea
            )

        for item in self.tree.get_children():
            self.tree.delete(item)

        for idea in self.filtered_ideas:
            self.tree.insert(
                "",
                "end",
                iid=idea["id"],
                values=(
                    idea["id"],
                    idea["name"],
                    idea["difficulty"],
                    self.get_status(
                        idea["id"]
                    ),
                )
            )

        self.update_stats()

    def update_stats(self):
        total = len(self.ideas)

        status_counts = {
            status: 0
            for status in STATUSES
        }

        for idea in self.ideas:
            status = self.get_status(
                idea["id"]
            )

            if status in status_counts:
                status_counts[status] += 1

        text = (
            f"全 {total}件  |  "
            f"完成 {status_counts['完成']}  |  "
            f"作業中 {status_counts['作業中']}  |  "
            f"次に作る {status_counts['次に作る']}  |  "
            f"表示 {len(self.filtered_ideas)}件"
        )

        self.stats_label.config(
            text=text
        )

    def on_select(self, event):
        selection = self.tree.selection()

        if not selection:
            return

        idea_id = selection[0]

        self.selected_idea = next(
            (
                idea
                for idea in self.ideas
                if idea["id"] == idea_id
            ),
            None
        )

        if not self.selected_idea:
            return

        idea = self.selected_idea

        self.detail_title.config(
            text=f"{idea['id']}  {idea['name']}"
        )

        detail_lines = [
            f"{idea['id']} {idea['name']}",
            "",
            f"カテゴリ: {idea['category']}",
            "",
            idea["description"],
        ]

        if idea["completion"]:
            detail_lines.extend(
                [
                    "",
                    f"完成条件: {idea['completion']}"
                ]
            )

        if idea["difficulty"]:
            detail_lines.extend(
                [
                    "",
                    f"難易度: {idea['difficulty']}"
                ]
            )

        if idea["technology"]:
            detail_lines.extend(
                [
                    "",
                    f"技術: {idea['technology']}"
                ]
            )

        if idea["new_technology"]:
            detail_lines.extend(
                [
                    "",
                    f"新技術: {idea['new_technology']}"
                ]
            )

        self.detail_text.config(
            state="normal"
        )

        self.detail_text.delete(
            "1.0",
            "end"
        )

        self.detail_text.insert(
            "1.0",
            "\n".join(detail_lines)
        )

        self.detail_text.config(
            state="disabled"
        )

        self.status_var.set(
            self.get_status(
                idea["id"]
            )
        )

    def change_status(self, event):
        if not self.selected_idea:
            return

        idea_id = self.selected_idea["id"]
        new_status = self.status_var.get()

        self.progress[idea_id] = new_status

        save_progress(
            self.progress
        )

        self.refresh_list()

    def select_random_idea(self):
        if not self.filtered_ideas:
            messagebox.showinfo(
                "ランダム選択",
                "現在の条件に合う候補がありません。"
            )
            return

        idea = random.choice(
            self.filtered_ideas
        )

        idea_id = idea["id"]

        self.tree.selection_set(
            idea_id
        )

        self.tree.focus(
            idea_id
        )

        self.tree.see(
            idea_id
        )

        self.tree.event_generate(
            "<<TreeviewSelect>>"
        )

def main():
    root = tk.Tk()
    IdeaBacklogManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()