from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def _get_percentage_color(progress):
    """Retourne la couleur selon le pourcentage."""
    if progress < 0.33:
        return "red"
    elif progress < 0.66:
        return "yellow"
    else:
        return "green"


def _progress_bar(ratio: float, width: int = 20) -> str:
    """Retourne une barre de progression textuelle simple."""
    done = int(ratio * width)
    remain = width - done
    # Dégradé adaptatif selon le ratio
    if ratio < 0.33:
        color = "red"
    elif ratio < 0.66:
        color = "yellow"
    else:
        color = "green"
    return f"[{color}]" + "█" * done + "[/]" + "░" * remain


def dashboard_panel(stats_dict, width=20):
    """Construit une ligne de résumé de progression (sans Panel)."""
    total = stats_dict["total"]
    progress = (stats_dict["fait"] / total) if total else 0
    bar = _progress_bar(progress, width=width)
    line = (
        f"[bold white]Avancement :[/bold white] "
        f"[green]{stats_dict['fait']} faits[/green] | "
        f"[yellow]{stats_dict['inter']} intermédiaires[/yellow] | "
        f"[magenta]{stats_dict['review']} à revoir[/magenta] | "
        f"[red]{stats_dict['todo']} à faire[/red] | "
        f"[dim]{total} total[/dim]  {bar} [white]{progress * 100:.0f}%[/white]"
    )
    # Ligne séparatrice propre
    console.print()
    console.print(line)


def create_summary_panel_horizontal(stats_dict):
    """Crée un panneau de résumé compact horizontal sur une seule ligne."""
    total = stats_dict["total"]
    progress = (stats_dict["fait"] / total) if total else 0
    bar_color = _get_percentage_color(progress)

    # Barre de progression compacte (12 caractères)
    width = 12
    done = int(progress * width)
    remain = width - done

    content = Text()

    # Stats compactes avec séparateurs
    content.append("✓ ", style="green bold")
    content.append(f"{stats_dict['fait']}", style="green bold")
    content.append(" │ ", style="dim")

    content.append("⟳ ", style="yellow bold")
    content.append(f"{stats_dict['inter']}", style="yellow bold")
    content.append(" │ ", style="dim")

    content.append("⚠ ", style="magenta bold")
    content.append(f"{stats_dict['review']}", style="magenta bold")
    content.append(" │ ", style="dim")

    content.append("○ ", style="red bold")
    content.append(f"{stats_dict['todo']}", style="red bold")
    content.append(" │ ", style="dim")

    # Barre de progression
    content.append("█" * done, style=f"{bar_color} bold")
    content.append("░" * remain, style="bright_black")
    content.append(" ", style="white")

    # Pourcentage
    content.append(f"{progress * 100:.0f}%", style=f"{bar_color} bold")

    return Panel(content, border_style="cyan", padding=(0, 1), expand=False)


def create_summary_panel(stats_dict):
    """Version verticale originale (gardée pour compatibilité)."""
    total = stats_dict["total"]
    progress = (stats_dict["fait"] / total) if total else 0
    bar_color = _get_percentage_color(progress)
    width = 16
    done = int(progress * width)
    remain = width - done

    content = Text()
    content.append("✓ ", style="green bold")
    content.append("Terminé   ", style="white")
    content.append(f"{stats_dict['fait']}", style="green bold")
    content.append(f"/{total}", style="dim")
    content.append("\n")

    content.append("⟳ ", style="yellow bold")
    content.append("En cours  ", style="white")
    content.append(f"{stats_dict['inter']}", style="yellow bold")
    content.append(f"/{total}\n", style="dim")

    content.append("⚠ ", style="magenta bold")
    content.append("À revoir  ", style="white")
    content.append(f"{stats_dict['review']}", style="magenta bold")
    content.append(f"/{total}\n", style="dim")

    content.append("○ ", style="red bold")
    content.append("Restant   ", style="white")
    content.append(f"{stats_dict['todo']}", style="red bold")
    content.append(f"/{total}", style="dim")

    content.append("\n")
    content.append("━" * 16, style="cyan dim")
    content.append("\n")

    pct_text = f"{progress * 100:.0f}%"
    content.append(pct_text.center(16), style=f"{bar_color} bold")
    content.append("█" * done, style=f"{bar_color} bold")
    content.append("░" * remain, style="bright_black")

    return Panel(
        content,
        title="[bold cyan]VUE D'ENSEMBLE[/bold cyan]",
        border_style="cyan",
        padding=(1, 1),
        width=20,
    )


# Exemple d'utilisation avec détection de largeur
def show_checklist_ui_adaptive(items, stats_dict=None):
    """Version adaptative qui choisit l'affichage selon la largeur du terminal."""
    from rich.columns import Columns
    from rich.table import Table
    from config.flags import FLAG_DISPLAY

    if not stats_dict:
        # Pas de stats, affichage simple
        table = Table(show_header=True, header_style="bold", show_lines=False)
        table.add_column("N", style="cyan", justify="center", width=1)
        table.add_column("Do", justify="center", width=3)
        table.add_column("Tâche", style="white", no_wrap=False)
        for i, item in enumerate(items):
            table.add_row(str(i + 1), FLAG_DISPLAY[item.statut], item.texte)
        console.print(table)
        return

    # Détecter la largeur du terminal
    terminal_width = console.width

    # Créer la table
    table = Table(show_header=True, header_style="bold", show_lines=False)
    table.add_column("N", style="cyan", justify="center", width=1)
    table.add_column("Do", justify="center", width=3)
    table.add_column("Tâche", style="white", no_wrap=False)
    for i, item in enumerate(items):
        table.add_row(str(i + 1), FLAG_DISPLAY[item.statut], item.texte)

    # Créer le panneau de statistiques
    summary_panel = create_summary_panel(stats_dict)

    # Choisir l'affichage selon la largeur
    if terminal_width < 200:
        # Terminal étroit : table puis panneau en dessous
        console.print(table)
        console.print(summary_panel)
    else:
        # Terminal large : panneau vertical à droite
        layout = Columns([table, summary_panel], align="left", expand=False)
        console.print(layout)
