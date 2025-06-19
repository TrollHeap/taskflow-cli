from core.back import read_checklist, update_status
from core.ui_cli import show_checklist, console
from core.model import Status
from config.flags import FLAGS_INPUT, FLAGS_HELP


def run_classic_mode():
    """
    Mode classique : navigation interactive,
    coche/décoche n’importe quelle tâche à la main.
    """
    while True:
        _, items = read_checklist()
        show_checklist(items)
        choix = console.input("[bold][cyan]Numéro à modifier[/cyan][/bold] ([dim]Entrée pour quitter[/dim]) : ").strip()
        if not choix:
            return  # sortie propre
        try:
            idx = int(choix) - 1
            if not (0 <= idx < len(items)):
                console.print("[red]Numéro invalide.[/red]\n")
                continue
            actuel = items[idx].statut
            console.print(f"Flag actuel : {actuel.value}")
            console.print(f"[cyan]Nouveau flag ?[/cyan] {FLAGS_HELP}")
            flag_choix = console.input("> ").strip()
            if not flag_choix:
                console.print("[yellow]Annulé.[/yellow]\n")
                continue
            if flag_choix not in FLAGS_INPUT:
                console.print("[dim]Flag invalide.[/dim]\n")
                continue
            new_flag = FLAGS_INPUT[flag_choix]
            note = ""
            if new_flag == Status.DONE:
                note = "🎉"
                console.print("[bold green]Bravo, tâche validée ![/bold green] :tada:")
            note_user = console.input("[dim]Note optionnelle (Entrée pour rien)[/dim] : ").strip()
            note = f"{note} {note_user}".strip() if note_user else note
            update_status(idx, new_flag, note or None)
            console.print("[dim]Checklist mise à jour.[/dim]\n")
        except ValueError:
            console.print("[red]Entrée non valide.[/red]\n")
