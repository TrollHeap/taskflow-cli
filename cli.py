import sys
import argparse
from core.ui_cli import console
from core.select_checklist import select_checklist
from modes.tunnel import run_tunnel_mode
from modes.classic import run_classic_mode


def main():
    parser = argparse.ArgumentParser(description="Unix Training Checklist")
    parser.add_argument('--switch', action='store_true', help='Choisir une checklist au démarrage')
    parser.add_argument('--tunnel', action='store_true', help='Mode tunnel (révision rapide)')
    # parser.add_argument('--quiz', action='store_true', help='Mode quiz')  # etc.
    args = parser.parse_args()

    checklist_path, log_path = select_checklist(force=args.switch)

    if args.tunnel:
        run_tunnel_mode()
    # elif args.quiz:
    #     run_quiz_mode()
    else:
        run_classic_mode()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrompu (Ctrl+C)[/red]")
        sys.exit(0)
