## 4. **Monitoring et diagnostic live**

* [ ] Surveillance et analyse sans GUI :
  * Disque : `df`, `du`, `ncdu`, `ls -lhS`, `find . -size`, usage `inodes`
  * RAM/CPU/process : `ps aux`, `top`, `htop`, `free`, `vmstat`, `iotop`, `glances`
  * Process ouverts : `lsof`, `fuser`, `ss`, `netstat`, `ip`, `nmap`
* [ ] Diagnostic réseau/connexion :
  * Diagnostic natif : `ping`, `traceroute`, `nc`, `curl`, `wget`, test connectivité/ports ouverts, `tcpdump`, `mtr`, `dig`, `bmon`
  * SSH et accès distants : clés SSH, tunnel, multiplex, autossh, restrictions, logs de connexion, `scp`, `rsync`, `sftp`.
* [ ] Logs et analyse avancée :
  * Lecture/navig rapide des logs (`cat`, `less`, `zcat`, `grep`, navigation dans gros fichiers)
  * Journalctl avancé (`journalctl -u`, `-f`, `--since`, `-p`, `--disk-usage`, export/logrotate)
  * Profiler le boot et les services systemd (`systemd-analyze`, `systemctl status`, timers, unit files, troubleshooting, override, templates, rescue/emergency mode)
  * Diagnostic et triage rapide d’incident : exporter, compresser, notifier.
