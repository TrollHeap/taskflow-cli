import re
from .model import ChecklistItem, Status
from config.config import load_config, get_checklist_dir, get_log_dir
from pathlib import Path
from typing import List, Optional, Tuple


def checklist_relative_path(ck_file: Path | str) -> str:
    """Return the path relative to the checklist directory."""
    ck_dir = get_checklist_dir().resolve()
    return str(Path(ck_file).resolve().relative_to(ck_dir))


def get_checklist_path(filename: Optional[str] = None) -> Path:
    """Return the full path to a checklist (supports subfolders)."""
    ck_dir = get_checklist_dir()
    if not filename:
        cfg = load_config()
        filename = cfg.get("last_checklist", {}).get("filename")
        if not filename:
            raise ValueError("Aucune checklist sélectionnée.")
    return (ck_dir / filename).resolve()


def get_log_path(ck_file: Path | str) -> Path:
    ck_dir = get_checklist_dir().resolve()
    rel = Path(ck_file).resolve().relative_to(ck_dir)
    log_file = get_log_dir() / rel.parent / f"log_{rel.stem}.md"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    return log_file


def read_checklist(
    path: Optional[Path] = None,
) -> Tuple[List[str], List[ChecklistItem]]:
    """Read a checklist file and return its raw lines and parsed items."""
    if path is None:
        path = get_checklist_path()
    try:
        with open(path, "r", encoding="utf-8") as f:
            lignes = f.readlines()
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Checklist introuvable : {path}") from exc
    items = []
    for idx, line in enumerate(lignes):
        m = re.match(r"^(\s*[\*\-]\s*)\[([ x~?])\]\s*(.+)$", line)
        if m:
            stat = Status(m.group(2))
            items.append(ChecklistItem(idx=idx, statut=stat, texte=m.group(3)))
    return lignes, items


def write_checklist(lignes: List[str], path: Optional[Path] = None) -> None:
    if path is None:
        path = get_checklist_path()
    with open(path, "w", encoding="utf-8") as f:
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


def read_journal(n: int = 5, ck_file: Optional[Path] = None) -> List[str]:
    if ck_file is None:
        ck_file = get_checklist_path()
    path = get_log_path(ck_file)
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()[-n:]
        return lines
    except FileNotFoundError:
        return []
