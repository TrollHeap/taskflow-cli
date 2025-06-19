from core.model import Status

FLAGS_INPUT = {
    "1": Status.DONE,
    "2": Status.INTER,
    "3": Status.REVIEW,
    "4": Status.TODO,
}
FLAGS_HELP = "[1]=fait, [2]=intermédiaire, [3]=à revoir, [4]=non fait, [Entrée]=annuler"
