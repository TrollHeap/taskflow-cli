from core.back import read_checklist, stats, focus
from ui.print_logs import print_logs_general
from ui.ui_cli import show_checklist_ui, show_focus_ui, console
from rich.progress import Progress


def afficher_dashboard():
    items = read_checklist()[1]
    s = stats(items)
    console.rule("[bold green]UNIX Roadmap — Tableau de Bord")
    progress = (s["fait"] / s["total"]) if s["total"] else 0
    with Progress(transient=True) as prog:
        prog.add_task("Progression", total=1.0, completed=progress)
    console.print(
        f"\n[bold]Avancement :[/bold] [green]{s['fait']} faits[/green] | "
        f"[yellow]{s['inter']} intermédiaires[/yellow] | "
        f"[magenta]{s['review']} à revoir[/magenta] | "
        f"[red]{s['todo']} à faire[/red] | [dim]{s['total']} total[/dim]\n"
    )
    show_checklist_ui(items, title="Checklist Complète")
    console.print()
    show_focus_ui(focus(items, n=3))

    print_logs_general()

    to_review = [i for i in items if i.statut.name == "REVIEW"]
    if to_review:
        console.print("\n[bold magenta]Tâches à revoir spécifiquement :[/bold magenta]")
        for i in to_review:
            console.print(f"  {i.idx + 1}. [magenta]?[/magenta] {i.texte}")


if __name__ == "__main__":
    afficher_dashboard()
