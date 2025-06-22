import re
from .model import Status
from typing import Iterable, List, Dict
from .io_files import read_checklist, write_checklist, append_journal


def update_status(
    idx: int,
    new_status: Status,
    note: str | None = None,
    ck_path: str | None = None,
    log_path: str | None = None,
) -> str:
    lignes, items = read_checklist(path=ck_path)
    item = items[idx]
    lignes[item.idx] = re.sub(r"\[[ x~?]\]", f"[{new_status.value}]", lignes[item.idx])
    write_checklist(lignes, path=ck_path)
    append_journal(item.texte, new_status, note, path=log_path)
    return item.texte


def stats(items: Iterable) -> Dict[str, int]:
    total = len(list(items))

    def count(s: Status) -> int:
        return sum(1 for i in items if i.statut == s)
    return {
        "total": total,
        "fait": count(Status.DONE),
        "inter": count(Status.INTER),
        "review": count(Status.REVIEW),
        "todo": count(Status.TODO),
    }


def focus(items: Iterable, n: int = 3) -> List:
    prio = (
        [i for i in items if i.statut == Status.REVIEW]
        + [i for i in items if i.statut == Status.TODO]
        + [i for i in items if i.statut == Status.INTER]
    )
    return prio[:n]
