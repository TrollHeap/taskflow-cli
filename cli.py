import sys
import argparse
from ui.ui_cli import console
from core import select_checklist
from modes.focus import run_focus_mode
from modes.classic import run_classic_mode
from modes.help import show_help


def main():
    parser = argparse.ArgumentParser(description="Unix Training Checklist")
    parser.add_argument('--switch', action='store_true', help='Choisir une checklist au démarrage')
    parser.add_argument('--focus', action='store_true', help='Mode Focus (révision rapide)')
    parser.add_argument('--aide', action='store_true', help='Afficher l’aide Taskflow CLI personnalisée')
    # parser.add_argument('--quiz', action='store_true', help='Mode quiz')  # etc.
    args = parser.parse_args()

    ck_file, log_file = select_checklist(force=args.switch)

    if args.focus:
        run_focus_mode(ck_file, log_file)
    elif args.aide:
        show_help()
    else:
        run_classic_mode(ck_file, log_file)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrompu (Ctrl+C)[/red]")
        sys.exit(0)
