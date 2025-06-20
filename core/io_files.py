import re
from .model import ChecklistItem, Status
from config.config import load_config, get_checklist_dir, get_log_dir
from pathlib import Path


def checklist_relative_path(ck_file):
    """
    Retourne le chemin relatif à checklists/ (ex: 'unix-training/automation-security.md')
    """
    ck_dir = get_checklist_dir().resolve()
    return str(Path(ck_file).resolve().relative_to(ck_dir))


def get_checklist_path(filename=None):
    """
    Retourne le chemin complet vers la checklist (supporte sous-dossiers).
    """
    ck_dir = get_checklist_dir()
    if not filename:
        cfg = load_config()
        filename = cfg.get("last_checklist", {}).get("filename")
        if not filename:
            raise ValueError("Aucune checklist sélectionnée.")
    return (ck_dir / filename).resolve()


def get_log_path(ck_file):
    ck_dir = get_checklist_dir().resolve()
    rel = Path(ck_file).resolve().relative_to(ck_dir)
    log_file = get_log_dir() / rel.parent / f"log_{rel.stem}.md"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    return log_file


def read_checklist(path=None):
    """
    Lis la checklist du path donné ou de la dernière sélectionnée.
    Retourne (lignes, items).
    """
    if path is None:
        path = get_checklist_path()
    with open(path, "r") as f:
        lignes = f.readlines()
    items = []
    for idx, line in enumerate(lignes):
        m = re.match(r"^(\s*\*\s*)\[([ x~?])\]\s*(.+)$", line)
        if m:
            stat = Status(m.group(2))
            items.append(ChecklistItem(idx=idx, statut=stat, texte=m.group(3)))
    return lignes, items


def write_checklist(lignes, path=None):
    if path is None:
        path = get_checklist_path()
    with open(path, "w") as f:
        f.writelines(lignes)


def append_journal(texte, statut, note=None, path=None):
    from datetime import datetime
    if path is None:
        path = get_log_path()
    date = datetime.now().isoformat(timespec="seconds")
    with open(path, "a") as f:
        ligne = f"{date}\t[{statut.value}]\t{texte}"
        if note:
            ligne += f"\t# {note}"
        f.write(ligne + "\n")


def read_journal(n=5, ck_file=None):
    if ck_file is None:
        # Par défaut, récupère la dernière checklist utilisée
        ck_file = get_checklist_path()
    path = get_log_path(ck_file)
    try:
        with open(path, "r") as f:
            lines = f.readlines()[-n:]
        return lines
    except FileNotFoundError:
        return []
