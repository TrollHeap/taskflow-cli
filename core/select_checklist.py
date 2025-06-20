import sys
from datetime import datetime
from pathlib import Path
from config.config import load_config, save_config, get_checklist_dir, get_log_dir


def list_checklists():
    ck_dir = get_checklist_dir()
    # Inclut sous-dossiers
    files = sorted(ck_dir.glob("**/*.md"))
    return files


def relative_to_ckdir(f):
    ck_dir = get_checklist_dir().resolve()
    return str(f.resolve().relative_to(ck_dir))


def select_checklist(force=False):
    files = list_checklists()
    ck_dir = get_checklist_dir().resolve()
    cfg = load_config()
    last_ck = cfg.get("last_checklist", {}).get("filename")

    # Retrouve la checklist précédente, si valide
    if not force and last_ck:
        for f in files:
            rel_path = str(f.resolve().relative_to(ck_dir))
            if rel_path == last_ck:
                print(f"Checklist sélectionnée : {last_ck}")
                log_file = get_log_dir() / Path(last_ck).parent / f"log_{Path(last_ck).stem}.md"
                log_file.parent.mkdir(parents=True, exist_ok=True)
                return f, log_file

    # --- IMPORT ICI POUR CASSER LE CERCLE ---
    from ui.ui_cli import select_checklist_ui
    choix = select_checklist_ui(files, ck_dir)
    if not choix.isdigit() or not (1 <= int(choix) <= len(files)):
        print("Numéro invalide.")
        sys.exit(1)
    ck_file = files[int(choix) - 1]
    rel_path = str(ck_file.resolve().relative_to(ck_dir))
    log_file = get_log_dir() / Path(rel_path).parent / f"log_{Path(rel_path).stem}.md"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    cfg["last_checklist"] = {
        "filename": rel_path,
        "selected_at": datetime.now().isoformat(timespec="seconds"),
    }
    save_config(cfg)
    return ck_file, log_file
