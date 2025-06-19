#  **Sauvegarde & permissions**

Checklist :

* [~] Sauvegarde manuelle et automatisée de fichiers et dossiers critiques (`cp`, `tar`, `gzip`, `rsync`, scripts, cron/systemd timer)
* [~] Utilisation d’`rsync` : compréhension des concepts (delta transfer, partial, archive, preserve, exclude, delete, update…), flags essentiels, scénarios de backup/restauration
* [ ] Détection et gestion des pièges/finesses d’`rsync` (slash terminal, permissions, synchronisation bidirectionnelle, edge-cases)
* [ ] Gestion et rotation des sauvegardes (logrotate, scripts, archivage périodique, purge automatisée)
* [ ] Restauration rapide depuis des archives ou backups (décompression, restauration sélective, vérification d’intégrité)
* [x] Manipulation des permissions fichiers/dossiers (`ls -l`, `chmod`, `chown`, `chgrp`), octal/symbolique, scénarios classiques/complexes
* [~] Analyse et modification récursive des droits (`chmod -R`, `chown -R`)
* [~] Compréhension des liens symboliques/hardlinks, usages et limitations
* [x] Identification et résolution de problèmes de droits (“Permission denied”, ownership incorrect, gestion d’accès multi-utilisateurs)
* [x] Mise en œuvre de sauvegardes reproductibles/portables (backup cross-OS, script shell natif)
* [~] Automatisation de sauvegardes et restaurations (cron/systemd, alertes, reporting)
