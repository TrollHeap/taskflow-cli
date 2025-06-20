from core.io_files import read_journal
from ui.ui_cli import console
from pathlib import Path


def print_logs_general(log_dir="logs", n=4, recursive=True):
    log_dir = Path(log_dir)
    logs = sorted(log_dir.glob("**/*.md") if recursive else log_dir.glob("*.md"))
    found = False
    for log_file in logs:
        lines = log_file.read_text(encoding="utf-8").splitlines()
        # Affiche les n dernières, ou toutes si < n
        chunk = lines[-n:] if n else lines
        if chunk:
            found = True
            console.print(f"\n[bold blue]{log_file.relative_to(log_dir)}[/bold blue]")
            for line in chunk:
                console.print("  [dim]" + line.strip() + "[/dim]")
    if not found:
        console.print("[dim](Aucune entrée de journal dans le dossier.)[/dim]")


def print_logs_files(nb_linelogs):
    recent = read_journal(n=nb_linelogs)
    if recent:
        console.print("\n[bold]Journal récent :[/bold]")
        for log in recent:
            console.print("  [dim]" + log.strip() + "[/dim]")
    else:
        console.print("\n[dim](Aucune entrée de journal récente)[/dim]")
