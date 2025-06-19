#  **Exploration un système inconnu (Unix/Linux)**

Checklist :

* [ ] Identification immédiate du contexte système (distro, version, kernel, arch, `uname`, `lsb_release`, `/etc/os-release`)
* [ ] Découverte et analyse des utilisateurs, sessions actives, connexions (`who`, `w`, `last`, `env`, `id`)
* [~] Inspection de l’environnement utilisateur (variables, shell, `echo $SHELL`, `printenv`, `set`)
* [ ] Observation et analyse des processus en cours (`ps aux`, `top`, statuts, priorités, `nice`, `renice`, kill signal)
* [ ] Navigation arborescente, découverte rapide des dossiers/fichiers critiques (`pwd`, `ls -lah`, `tree`, repérage des dotfiles)
* [ ] Recherche efficace de fichiers/chaînes (`find`, `grep`, options avancées, extraction de contexte, navigation rapide)
* [x] Lecture et exploration fine des fichiers volumineux/logs (`cat`, `head`, `tail`, `less`, recherche dans less, `zcat` sur logs compressés)
* [ ] Investigation du réseau (ports ouverts, connexions actives, `ss -tuln`, `netstat`, `lsof -i`, diagnostic connectivité, `ping`, `curl`, `traceroute`)
* [ ] Audit rapide de la planification des tâches système (`crontab -l`, `/etc/cron*`, `systemctl list-timers`, analyse des scripts automatisés)
* [x] Vérification de la sécurité, permissions et accès critiques (`ls -l`, `chmod`, `chown`, analyse des droits sur les dossiers stratégiques)
* [ ] Lecture, analyse et gestion des logs système (`/var/log/*`, rotation, recherche ciblée, identification d’anomalies)
* [ ] Traces et audit d’activité utilisateur (`history`, `script`, sauvegarde de session, export d’historique pour reporting)
* [ ] Sauvegarde de découvertes, extraction de preuves, partage reproductible (logs, exports, fichiers clés)
* [ ] Capacité à tout réaliser sans aucun outil tiers (coreutils, POSIX) et à identifier rapidement la présence/absence d’outils modernes
