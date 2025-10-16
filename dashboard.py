from core.back import read_checklist, stats
from ui.print_logs import print_logs_general
from ui.ui_cli import show_checklist_ui, console, dashboard_panel


def run_dashboard():
    result = read_checklist()

    # Extraction des données
    ck_file, items = result if isinstance(result, tuple) else (None, result)

    # Statistiques et affichage
    s = stats(items)
    console.rule("[bold green]Taskflow — Tableau de Bord")

    # Détermine le nom à afficher
    if isinstance(ck_file, list):
        rel_path = next(
            (
                line.strip().lstrip("#").strip()
                for line in ck_file
                if line.startswith("##")
            ),
            "<checklist courante>",
        )
    else:
        rel_path = "<checklist courante>"

    show_checklist_ui(items, title="Checklist Complète", current_file=rel_path)
    console.print(dashboard_panel(s, width=20))
    print_logs_general()


if __name__ == "__main__":
    run_dashboard()
