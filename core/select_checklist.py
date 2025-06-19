from pathlib import Path
import sys
from core.ui_cli import select_checklist_ui

LAST_FILE = Path(".last_checklist")


def list_checklists():
    ck_dir = Path("checklists")
    files = sorted([f for f in ck_dir.glob("*.md")])
    return files


def select_checklist(force=False):
    files = list_checklists()
    if not force and LAST_FILE.exists():
        last = LAST_FILE.read_text().strip()
        for f in files:
            if f.name == last:
                print(f"Checklist sélectionnée : {f.name}")
                return f, Path("logs") / (f.stem + ".log")
    # Utilise la UI rich ici
    choix = select_checklist_ui(files)
    if not choix.isdigit() or not (1 <= int(choix) <= len(files)):
        print("Numéro invalide.")
        sys.exit(1)
    ck_file = files[int(choix) - 1]
    log_file = Path("logs") / (ck_file.stem + ".log")
    LAST_FILE.write_text(ck_file.name)
    return ck_file, log_file
