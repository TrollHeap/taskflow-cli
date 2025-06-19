import re
from .model import ChecklistItem, Status


def read_checklist(path="unix-checklist.md"):
    with open(path, "r") as f:
        lignes = f.readlines()
    items = []
    for idx, line in enumerate(lignes):
        m = re.match(r"^(\s*\*\s*)\[([ x~?])\]\s*(.+)$", line)
        if m:
            stat = Status(m.group(2))
            items.append(ChecklistItem(idx=idx, statut=stat, texte=m.group(3)))
    return lignes, items


def write_checklist(lignes, path="unix-checklist.md"):
    with open(path, "w") as f:
        f.writelines(lignes)


def append_journal(texte, statut, note=None, path="log/journal/unix-journal.md"):
    from datetime import datetime
    date = datetime.now().isoformat(timespec="seconds")
    with open(path, "a") as f:
        ligne = f"{date}\t[{statut.value}]\t{texte}"
        if note:
            ligne += f"\t# {note}"
        f.write(ligne + "\n")


def read_journal(path="log/journal/unix-journal.md", n=5):
    try:
        with open(path, "r") as f:
            lines = f.readlines()[-n:]
        return lines
    except FileNotFoundError:
        return []
