from rich.panel import Panel


def _progress_bar(ratio: float, width: int = 20) -> str:
    """Return a simple textual progress bar."""
    done = int(ratio * width)
    remain = width - done
    return "[green]" + "█" * done + "[/green]" + "░" * remain


def dashboard_panel(stats_dict, width=20):
    """Construit un panel de progression et résumé d'avancement."""
    total = stats_dict["total"]
    progress = (stats_dict["fait"] / total) if total else 0
    bar = _progress_bar(progress, width=width)
    return Panel(
        f"{bar} {progress * 100:.0f}%"
        f"[bold] Avancement :[/bold] [green]{stats_dict['fait']} faits[/green] | "
        f"[yellow]{stats_dict['inter']} intermédiaires[/yellow] | "
        f"[magenta]{stats_dict['review']} à revoir[/magenta] | "
        f"[red]{stats_dict['todo']} à faire[/red] | [dim]{total} total[/dim]"
    )
