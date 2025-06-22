from core.back import read_checklist, stats, focus
from ui.print_logs import print_logs_general
from ui.ui_cli import show_checklist_ui, show_focus_ui, console
from ui.dashboard_ui import dashboard_panel


def run_dashboard():
    items = read_checklist()[1]
    s = stats(items)
    console.rule("[bold green]UNIX Roadmap — Tableau de Bord")
    console.print(dashboard_panel(s, width=20))
    show_checklist_ui(items, title="Checklist Complète")
    console.print()
    # show_focus_ui(focus(items, n=4))

    print_logs_general()

    to_review = [i for i in items if i.statut.name == "REVIEW"]
    if to_review:
        console.print("\n[bold magenta]Tâches à revoir spécifiquement :[/bold magenta]")
        for i in to_review:
            console.print(f"  {i.idx + 1}. [magenta]?[/magenta] {i.texte}")


if __name__ == "__main__":
    run_dashboard()
