from core.back import update_status
from core.io_files import read_checklist
from core.model import Status
from ui.ui_cli import show_checklist_ui, console
from config.flags import FLAGS_INPUT, FLAGS_HELP
from ui.print_logs import print_logs_files


def run_focus_mode(ck_file=None, log_file=None):
    _, items = read_checklist(path=ck_file)
    focus_items = [item for item in items if item.statut in (Status.TODO, Status.REVIEW)]
    print_logs_files(8)
    if not focus_items:
        console.print("[bold green]✅ Toutes les tâches sont cochées ou intermédiaires ![/bold green]")
        return
    for item in focus_items:
        console.rule("[bold blue]Mode Révision Rapide (Tunnel)")
        show_checklist_ui([item])
        console.print(f"[dim]Nouveau flag ?[/dim] {FLAGS_HELP}, [q]=quitter")
        flag_choix = console.input("> ").strip()
        if flag_choix == "q":
            console.print("[dim]Arrêt du mode tunnel.[/dim]")
            break
        if not flag_choix:
            console.print("[yellow]Annulé, tâche inchangée.[/yellow]")
            continue
        if flag_choix not in FLAGS_INPUT:
            console.print("[red]Flag invalide.[/red]")
            continue
        new_flag = FLAGS_INPUT[flag_choix]
        note = ""
        if new_flag == Status.DONE:
            note = "🎉"
            console.print("[bold green]Bravo, tâche validée ![/bold green] :tada:")
        note_user = console.input("[dim]Note optionnelle (Entrée pour rien)[/dim] : ").strip()
        note = f"{note} {note_user}".strip() if note_user else note
        update_status(
            item.idx, new_flag, note or None, ck_path=ck_file, log_path=log_file
        )
        console.print("[dim]Tâche mise à jour.[/dim]\n")
    console.rule("[bold blue]Mode tunnel terminé[/bold blue]\n")
    return
