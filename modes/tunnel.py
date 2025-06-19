from core.back import read_checklist, update_status
from core.ui_cli import show_checklist, console
from core.model import Status
from core.flags import FLAGS_INPUT, FLAGS_HELP


def run_tunnel_mode():
    _, items = read_checklist()
    tunnel_items = [item for item in items if item.statut in (Status.TODO, Status.REVIEW)]
    if not tunnel_items:
        console.print("[bold green]✅ Toutes les tâches sont cochées ou intermédiaires ![/bold green]")
        return
    for item in tunnel_items:
        console.rule("[bold blue]Mode Révision Rapide (Tunnel)")
        show_checklist([item])
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
        update_status(item.idx, new_flag, note or None)
        console.print("[dim]Tâche mise à jour.[/dim]\n")
    console.rule("[bold blue]Mode tunnel terminé[/bold blue]\n")
    return
