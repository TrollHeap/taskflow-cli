from rich.console import Console
from rich.table import Table
from .model import Status

console = Console()

FLAG_DISPLAY = {
    Status.DONE: "[green]✓[/green]",
    Status.INTER: "[yellow]~[/yellow]",
    Status.REVIEW: "[magenta]?[/magenta]",
    Status.TODO: "[red]…[/red]",
}


def show_checklist(items, title="Checklist"):
    table = Table(show_header=True, header_style="bold", show_lines=False)
    table.add_column("No", style="cyan", justify="right", width=3)
    table.add_column("Statut", justify="center", width=6)
    table.add_column("Tâche", style="white")
    for i, item in enumerate(items):
        table.add_row(str(i + 1), FLAG_DISPLAY[item.statut], item.texte)
    console.print(table)


def show_focus(items):
    table = Table(title="Focus du jour", show_header=True, header_style="bold")
    table.add_column("No", width=4)
    table.add_column("Statut", width=6)
    table.add_column("Tâche")
    for item in items:
        table.add_row(str(item.idx + 1), FLAG_DISPLAY[item.statut], item.texte)
    console.print(table)
