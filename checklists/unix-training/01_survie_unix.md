## 1. **Survie Unix/CLI – “Prise en main d’un système inconnu ou cassé”**

* [ ] Identification immédiate du contexte système (`uname -a`, `cat /etc/os-release`, `lsb_release -a`, arch, kernel, etc.)
* [ ] Navigation sans plugin : `cd`, `ls -lah`, `tree`, repérage des dotfiles, navigation arborescente rapide.
* [ ] Edition et fallback minimal (`vi`, `nano`, `ed`), éditer/créer des fichiers config en environnement restreint.
* [ ] Restauration d’un shell minimal (coreutils only, busybox, vi, pas de plugins, pas de shell avancé).
* [ ] Gestion des sessions et tty de secours, usage de `screen`, `tmux`, ou “console root”.
* [ ] Commandes de secours : `mount`, `chroot`, `passwd`, rescue (root shell).
* [ ] Exporter/extraire des preuves/logs (via `scp`, `sftp`, `netcat`, `tar`, même sans outils modernes).
