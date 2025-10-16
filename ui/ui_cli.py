from rich.console import Console
from rich.table import Table
from config.flags import FLAG_DISPLAY
from rich.panel import Panel
from rich.text import Text

console = Console()


def select_checklist_ui(files, ck_dir):
    table = Table(show_header=True, header_style="bold")
    table.add_column("No", style="cyan", justify="right", width=3)
    table.add_column("Checklist", style="white")
    for i, f in enumerate(files):
        rel_path = str(f.resolve().relative_to(ck_dir))
        table.add_row(str(i + 1), rel_path)
    console.print("\n== Checklists disponibles ==")
    console.print(table)
    choix = console.input("Numéro à ouvrir : ").strip()
    return choix


def show_checklist_ui(items, title="Checklist", current_file=None):
    if current_file:
        # nettoyage Markdown
        clean_title = (
            current_file.replace("##", "").replace("**", "").replace("1.", "").strip()
        )

        console.print(
            Panel(
                Text(clean_title, style="bold yellow"),
                border_style="yellow",
                title="📋Sujet",
                title_align="left",
                padding=(0, 2),
            )
        )

    table = Table(show_header=True, header_style="bold", show_lines=False)
    table.add_column("No", style="cyan", justify="right", width=3)
    table.add_column("Statut", justify="center", width=6)
    table.add_column("Tâche", style="white")

    for i, item in enumerate(items):
        table.add_row(str(i + 1), FLAG_DISPLAY[item.statut], item.texte)

    console.print(table)


def show_focus_ui(items):
    table = Table(title="Focus du jour", show_header=True, header_style="bold")
    table.add_column("No", width=4)
    table.add_column("Statut", width=6)
    table.add_column("Tâche")
    for item in items:
        table.add_row(str(item.idx + 1), FLAG_DISPLAY[item.statut], item.texte)
    console.print(table)
