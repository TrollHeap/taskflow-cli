## 2. **Manipulation de fichiers, flux, jobs, et automatisation**

* [ ] Pipes, redirections, duplication de flux (`|`, `>`, `>>`, `<`, `2>`, `2>&1`, `tee`, process substitution).
* [ ] Manipulation et transformation rapide de fichiers/textes :
  * Recherche/filtrage : `grep`, `egrep`, `fgrep`, regex POSIX/extended
  * Extraction/tri/déduplication : `sort`, `uniq`, `cut`, `awk`, `sed`, `tr`, `paste`
  * Statistiques rapides : `wc -l`, `head`, `tail`, `du -h`, `df -h`, `find`, `xargs`, `parallel`
* [ ] Traitement natif de CSV, JSON, structures complexes (`cut`, `awk`, `jq`, `csvkit` si natif, sinon fallback coreutils).
* [ ] Boucles, contrôle de flux shell (`for`, `while`, `case`, expansions paramétriques, pattern matching)
* [ ] Utilisation/écriture de scripts réutilisables, modularité, usage d’`env -i`, gestion de variables d’environnement, fallback natif si variables absentes.
* [ ] Automatisation : scripts, fonctions shell, alias, usage de `cron` et `systemd timers`.
