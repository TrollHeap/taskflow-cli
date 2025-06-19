import sys
import argparse
from core.ui_cli import console
from modes.tunnel import run_tunnel_mode
from modes.classic import run_classic_mode


def main():
    parser = argparse.ArgumentParser(description="Unix Training Checklist")
    parser.add_argument('--tunnel', action='store_true', help='Mode tunnel (révision rapide)')
    # parser.add_argument('--quiz', action='store_true', help='Mode quiz')  # etc.
    args = parser.parse_args()

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
