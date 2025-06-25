 **Diagnostic système & monitoring**

Checklist :

* [~] Diagnostic de l’espace disque sans GUI (`df`, `du`, outils alternatifs modernes type `ncdu`, `duf`, `disk` rust)
* [~] Analyse et surveillance des processus (`ps aux`, `top`, `htop`, `glances`, `procs`)
* [ ] Identification et gestion des ressources (CPU, RAM, swap, load average…) via outils natifs et alternatifs
* [ ] Usage de `jq`, `numfmt` pour manipuler/transformer des sorties JSON/numériques en shell
* [ ] Utilisation de `watch`, `while`/`for` shell, boucles de monitoring “pauvres” mais natives
* [ ] Automatisation de tâches répétitives : scripts shell, alias, fonctions shell, usage de `cron` natif (cron user, systemd timers)
* [ ] Détection automatique de la présence/disponibilité d’un outil (ex : test `command -v`, fallback)
* [ ] Intégration d’outils modernes (rust/binaire) sans casser la portabilité de workflow (ne pas rendre son shell dépendant)
* [~] Recherche et inspection rapide de logs via shell pur (`cat`, `less`, `zcat`, `grep`, navigation/filtres/visualisation dans gros fichiers)
* [x] Manipulation efficace de fichiers volumineux, paginés, compressés (`less`, `zless`, `head`, `tail`, options avancées)
* [ ] Accès rapide aux tâches planifiées système (`crontab -l`, `/etc/cron.*`, `systemctl list-timers`, inspection/édition)
* [ ] Vérification des connexions réseau actives/ports ouverts (`ss`, `netstat`, `lsof`, compréhension des arguments clés)
* [ ] Utilisation d’outils de test réseau natifs (`ping`, `traceroute`, `curl`, `wget`, diagnostic connectivité)
* [ ] Prise en main et usage des formats d’export : CSV, JSON (sortie outils/parse), traitements ad hoc (`cut`, `awk`, `sed`, `csvkit`…)
* [~] Sauvegarde, archivage, transfert de données sans GUI (`cp`, `mv`, `tar`, `gzip`, `rsync`…)
* [ ] Gestion de l’historique et de la reproductibilité des commandes (`history`, `script`, `tee`, export historique, session replay)
