from rich.table import Table
from rich.console import Console

tasks = []
with open("unix-checklist.md") as f:
    for line in f:
        if line.startswith("* ["):
            state = line[2:5]
            desc = line[6:].strip()
            tasks.append((state, desc))

table = Table(title="Checklist Unix", show_lines=True)
table.add_column("N°")
table.add_column("État")
table.add_column("Tâche")
for i, (state, desc) in enumerate(tasks, 1):
    table.add_row(str(i), state, desc)

Console().print(table)
