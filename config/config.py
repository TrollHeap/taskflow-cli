import toml
from pathlib import Path
from copy import deepcopy

CONFIG_PATH = Path("taskflowrc.toml")

DEFAULT_CONFIG = {
    "last_checklist": {"filename": None, "selected_at": None},
    "ui": {
        "theme": "auto",
        "progress_style": "bar",
        "compact_mode": False,
        "show_focus": True,
    },
    "stats": {
        "total_checks": 0,
        "micro_victories_today": 0,
        "last_victory": None,
    },
    "profile": {
        "user": None,
        "adhd_mode": False,
    },
    "paths": {
        "checklist_dir": "checklists",
        "log_dir": "logs",
    },
    "custom": {}
}


def load_config():
    if CONFIG_PATH.exists():
        cfg = toml.load(CONFIG_PATH)
        # Ajout des clés manquantes (robustesse)
        merged = deepcopy(DEFAULT_CONFIG)
        for k, v in cfg.items():
            if isinstance(v, dict):
                merged[k].update(v)
            else:
                merged[k] = v
        return merged
    else:
        return deepcopy(DEFAULT_CONFIG)


def save_config(cfg):
    # Pas besoin de deepcopy, on écrit tel quel
    with open(CONFIG_PATH, "w") as f:
        toml.dump(cfg, f)


def get_checklist_dir():
    cfg = load_config()
    return Path(cfg.get("paths", {}).get("checklist_dir", "checklists"))


def get_log_dir():
    cfg = load_config()
    return Path(cfg.get("paths", {}).get("log_dir", "logs"))


def get_last_checklist():
    cfg = load_config()
    fname = cfg.get("last_checklist", {}).get("filename")
    return fname


def set_last_checklist(filename):
    from datetime import datetime
    cfg = load_config()
    cfg["last_checklist"]["filename"] = filename
    cfg["last_checklist"]["selected_at"] = datetime.now().isoformat(timespec="seconds")
    save_config(cfg)
