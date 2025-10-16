from pathlib import Path
from core.back import read_checklist, stats
from ui.print_logs import print_logs_general
from ui.ui_cli import show_checklist_ui, console
from ui.dashboard_ui import dashboard_panel


def run_dashboard():
    result = read_checklist()
    # Gestion des 2 cas : (chemin, items) OU (liste, items)
    if isinstance(result, tuple) and len(result) == 2:
        ck_file, items = result
    else:
        # fallback : ancien format → juste une liste
        ck_file, items = None, result

    s = stats(items)

    console.rule("[bold green]UNIX Roadmap — Tableau de Bord")
    console.print(dashboard_panel(s, width=20))

    # Détermine le nom du fichier à afficher
    if isinstance(ck_file, (str, Path)):
        ck_path = Path(ck_file)
        rel_path = f"{ck_path.parent.name}/{ck_path.name}"
    elif isinstance(ck_file, list) and len(ck_file) > 0:
        # extraire le titre markdown (## ...)
        title_line = next((l.strip() for l in ck_file if l.startswith("##")), None)
        rel_path = title_line or "<checklist courante>"
    else:
        rel_path = "<checklist inconnue>"

    show_checklist_ui(items, title="Checklist Complète", current_file=rel_path)

    print_logs_general()


if __name__ == "__main__":
    run_dashboard()
