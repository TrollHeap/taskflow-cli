from core.back import update_status
from core.io_files import read_checklist
from core.model import Status
from ui.ui_cli import show_checklist_ui, console
from ui.print_logs import print_logs_files
from config.flags import FLAGS_INPUT, FLAGS_HELP


def run_classic_mode(ck_path, log_path):
    """
    Mode classique : navigation interactive, coche/décoche n’importe quelle tâche à la main.
    Prend en paramètre le chemin checklist et log.
    """
    while True:
        _, items = read_checklist(path=ck_path)
        show_checklist_ui(items)
        print_logs_files(8)
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
            # Ici on passe les paths
            update_status(idx, new_flag, note or None, ck_path=ck_path, log_path=log_path)
            console.print("[dim]Checklist mise à jour.[/dim]\n")
        except ValueError:
            console.print("[red]Entrée non valide.[/red]\n")
