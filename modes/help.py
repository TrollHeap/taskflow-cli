from rich.console import Console

HELP_TEXT = """
[bold]Commandes principales :[/bold]
  [cyan]Entrée[/cyan]        — Quitter
  [cyan]1[/cyan]-[cyan]4[/cyan]         — Cocher/intermédiaire/à revoir/non fait
  [cyan]t[/cyan]             — Mode tunnel (révision rapide)
  [cyan]f[/cyan]             — Focus du jour
  [cyan]q[/cyan]             — Quitter à tout moment
  [cyan]--switch[/cyan]      — Changer de checklist
  [cyan]--help[/cyan]        — Afficher l’aide complète

[bold]Raccourcis avancés :[/bold]
  [cyan]--export[/cyan]      — Exporter en CSV/JSON
  [cyan]--stats[/cyan]       — Statistiques globales
"""


def show_help():
    Console().print(HELP_TEXT)
