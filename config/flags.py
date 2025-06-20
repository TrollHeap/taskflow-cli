# flags.py
from core.model import Status

FLAGS_INPUT = {
    "1": Status.DONE,
    "2": Status.INTER,
    "3": Status.REVIEW,
    "4": Status.TODO,
}
FLAGS_HELP = "[1]=fait, [2]=intermédiaire, [3]=à revoir, [4]=non fait, [Entrée]=annuler"

FLAG_DISPLAY = {
    Status.DONE: "[green]✓[/green]",
    Status.INTER: "[yellow]~[/yellow]",
    Status.REVIEW: "[magenta]?[/magenta]",
    Status.TODO: "[red]…[/red]",
}
