from rich.console import Console
from rich.table import Table
from config.flags import FLAG_DISPLAY

console = Console()


def _progress_bar(ratio: float, width: int = 20) -> str:
    """Return a simple textual progress bar."""
    done = int(ratio * width)
    remain = width - done
    return "[green]" + "█" * done + "[/green]" + "░" * remain


def dashboard_panel(stats_dict, width=20):
    """Construit un résumé d'avancement horizontal descriptif et organisé."""
    total = stats_dict["total"]
    progress = (stats_dict["fait"] / total) if total else 0
    bar = _progress_bar(progress, width=width)

    # separator = "=" * 60

    statuts = (
        f"[X] [green]{stats_dict['fait']} faits[/green]  "
        f"[~] [yellow]{stats_dict['inter']} en cours[/yellow]  "
        f"[?] [magenta]{stats_dict['review']} à revoir[/magenta]  "
        f"[ ] [red]{stats_dict['todo']} à faire[/red]  "
        f"[dim]Total: {total}[/dim]"
    )

    progression = f"{bar} [cyan bold]{progress * 100:.0f}%[/cyan bold]"

    return f"\nStatuts: {statuts}\nProgression: {progression}"


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
        console.print(f"📋 - [bold yellow]{clean_title}[/bold yellow]")
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
