import re
from .model import ChecklistItem, Status
from .io_files import read_checklist, write_checklist, append_journal


def update_status(idx, new_status: Status, note=None):
    lignes, items = read_checklist()
    item = items[idx]
    # Remplace le flag dans la ligne d'origine
    lignes[item.idx] = re.sub(r"\[[ x~?]\]", f"[{new_status.value}]", lignes[item.idx])
    write_checklist(lignes)
    append_journal(item.texte, new_status, note)
    return item.texte


def stats(items):
    total = len(items)
    def count(s): return sum(1 for i in items if i.statut == s)
    return {
        "total": total,
        "fait": count(Status.DONE),
        "inter": count(Status.INTER),
        "review": count(Status.REVIEW),
        "todo": count(Status.TODO),
    }


def focus(items, n=3):
    prio = (
        [i for i in items if i.statut == Status.REVIEW] +
        [i for i in items if i.statut == Status.TODO] +
        [i for i in items if i.statut == Status.INTER]
    )
    return prio[:n]
