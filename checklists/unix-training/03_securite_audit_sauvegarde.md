## 3. **Sécurité, permissions, audit et sauvegarde**

* [ ] Inspection, modification, restauration de permissions/ownership (`ls -l`, `chmod`, `chown`, `chgrp`, usage symbolique/octal/récursif, ACL/`getfacl`/`setfacl`).
- [ ] Scénarios tendus (SUID, sticky, hard/symlinks) `chmod u+s fichier`, `chmod +t /tmp`, `ln -s /tmp/orig /tmp/lien`
* [ ] Audit de scripts: Fork abusif, quoting manquant, vulnérabilités glob/IFS, non-usage de `set -euo pipefail`
* [ ] Audit de scripts: Validation des entrées utilisateur (`[[ "$var" =~ regex ]]`, jamais de variable non-quotée).
* [ ] Surveillance/audit système : Fichiers critiques : `auditctl`, `ausearch`, `chkrootkit`, `tripwire`
* [ ] Surveillance/audit système : Historique (`history`, `script`, transmission des logs, session replay, export d’historique)
* [ ] Centralisation des logs, rotation (`logrotate`, suppression planifiée, `journalctl --vacuum-size`)
* [ ] Sauvegarde, restauration, automatisation : Outils natifs : `cp`, `tar`, `gzip`, `rsync` (tous les flags importants, gestion des pièges, slash terminal, delta, partial, delete, bidirectionnel, exclude, perms).
