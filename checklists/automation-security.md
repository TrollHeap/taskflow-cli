# **Automatisation & sécurité shell**

Checklist :

* [x] Versionnement systématique de tes configs (dotfiles, `.vimrc`, `.bashrc`, scripts shell) via Git ou équivalent
* [x] Documentation de tes principaux alias, scripts, raccourcis personnalisés, *sans* te reposer uniquement sur ta mémoire
* [~] Anticipation et gestion des commandes à risque (`rm -rf`, test de sécurité, dry-run, protections natives, alias safe…)
* [~] Capacité à restaurer rapidement un shell minimal sur machine vierge (config d’urgence, coreutils only, pas de plugin)
* [~] Automatisation des sauvegardes critiques (script shell, cron, rsync, snapshot)
* [ ] Analyse et gestion des logs systèmes en natif (rotation, archivage, suppression planifiée)
* [ ] Sécurisation de base d’un shell distant (SSH keys, configuration stricte, limitation des accès, logs de connexion)
* [~] Inspection, modification, restauration de permissions/ownership (`chmod`, `chown`, `chgrp`, scénarios d’usage “tendus”)
* [ ] Audit de sessions/actions (`script`, `history`, centralisation des logs, transmission à un tiers)
* [ ] Maîtrise des techniques de fallback/survie en environnement restreint (perte de SSH, shell limité, tty de secours)
* [ ] Préparation de “kits de secours” : liste de commandes/actions pour prise en main d’un système inconnu
